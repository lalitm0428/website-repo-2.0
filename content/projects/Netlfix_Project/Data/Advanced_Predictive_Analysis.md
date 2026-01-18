# Advanced Netflix Data Analysis Guide

This guide covers advanced predictive modeling and unsupervised learning techniques to extract deeper insights from the Netflix dataset.

## Notebook 5: Advanced Machine Learning

**Goal:** Move beyond simple regression/classification to multi-class classification and content recommendation systems.

### Step 1: Setup and Imports
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.metrics.pairwise import linear_kernel

# Load data
df = pd.read_csv('../Output/netflix_cleaned.csv')

# Drop rows with missing descriptions or ratings just in case
df.dropna(subset=['description', 'rating'], inplace=True)
```

### Step 2: Feature Engineering (Target Grouping)
The raw ratings (TV-MA, R, PG-13, etc.) are too fragmented. Let's group them into broader target audiences for better prediction accuracy.

```python
def group_ratings(rating):
    if rating in ['TV-MA', 'R', 'NC-17']:
        return 'Adults'
    elif rating in ['TV-14', 'PG-13']:
        return 'Teens'
    elif rating in ['TV-PG', 'PG', 'TV-Y7', 'TV-Y7-FV']:
        return 'Older Kids'
    elif rating in ['TV-Y', 'G']:
        return 'Kids'
    else:
        return 'Unknown'

df['target_audience'] = df['rating'].apply(group_ratings)
# Remove 'Unknown' or 'NR' ratings
df = df[df['target_audience'] != 'Unknown']
df = df[df['target_audience'] != 'Unknown'].copy()

print(df['target_audience'].value_counts())
```

### Step 3: Advanced Classification (Predicting Audience)
Can we predict the target audience solely based on the description?

```python
# 1. Text Vectorization (TF-IDF)
# We remove stop words to focus on meaningful keywords
tfidf = TfidfVectorizer(stop_words='english', max_features=5000)
X = tfidf.fit_transform(df['description'])
y = df['target_audience']

# 2. Split Data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Train Random Forest Model
# Random Forest is often more robust than Logistic Regression for complex multi-class problems
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

# 4. Evaluate
y_pred = rf_model.predict(X_test)
print(classification_report(y_test, y_pred))
```

### Step 4: Content-Based Recommendation System
This uses unsupervised learning to find similarities between titles based on their plot descriptions.

```python
# 1. Compute Cosine Similarity Matrix
# This calculates the similarity of every movie description to every other movie description
cosine_sim = linear_kernel(X, X)

# 2. Create a reverse mapping of indices and movie titles
indices = pd.Series(df.index, index=df['title']).drop_duplicates()

# 3. Function to get recommendations
def get_recommendations(title, cosine_sim=cosine_sim):
    if title not in indices:
        return "Title not found."
    
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11] # Top 10 similar (excluding itself)
    movie_indices = [i[0] for i in sim_scores]
    return df['title'].iloc[movie_indices]

# Test the system
# Replace '3 Idiots' with any title from your dataset
print("Recommendations for '3 Idiots':")
print(get_recommendations('3 Idiots'))
```
