import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.decomposition import TruncatedSVD

# Load the dataset
df = pd.read_csv('netflix_cleaned.csv')

# Drop rows with missing descriptions to avoid errors
df = df.dropna(subset=['description']).copy()

# 1. Text Vectorization (TF-IDF)
# Convert the descriptions into numerical vectors.
# We remove common English stop words (like 'the', 'and') and limit to top 5000 words.
tfidf = TfidfVectorizer(stop_words='english', max_features=5000)
X = tfidf.fit_transform(df['description'])

# 2. K-Means Clustering
# We'll use 10 clusters to group similar content.
# You can adjust n_clusters to find more specific or broader groups.
num_clusters = 10
kmeans = KMeans(n_clusters=num_clusters, random_state=42)
df['cluster'] = kmeans.fit_predict(X)

# 3. Visualize Clusters using TruncatedSVD (LSA)
# Since TF-IDF creates a sparse matrix, we use TruncatedSVD to reduce it to 2 dimensions for plotting.
svd = TruncatedSVD(n_components=2, random_state=42)
X_pca = svd.fit_transform(X)

# Plotting
plt.figure(figsize=(12, 8))
sns.scatterplot(x=X_pca[:, 0], y=X_pca[:, 1], hue=df['cluster'], palette='tab10', legend='full')
plt.title('Netflix Content Clusters based on Description')
plt.xlabel('Component 1')
plt.ylabel('Component 2')
plt.show()

# 4. Inspect Clusters
# Print a few titles from each cluster to see what themes emerged
for i in range(num_clusters):
    print(f"\nCluster {i} Examples:")
    print(df[df['cluster'] == i]['title'].head(5).tolist())