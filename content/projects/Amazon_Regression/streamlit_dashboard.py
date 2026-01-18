import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import json

# Page configuration
st.set_page_config(
    page_title="E-Commerce Analytics",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

COLORS = {
    'background': '#000000',
    'card_bg': '#1C1C1E',
    'card_hover': '#2C2C2E',
    'primary': '#0A84FF',
    'secondary': '#5E5CE6',
    'accent': '#30D158',
    'text_primary': '#FFFFFF',
    'text_secondary': '#98989D',
    'border': '#38383A',
    'chart_1': '#0A84FF',
    'chart_2': '#5E5CE6',
    'chart_3': '#BF5AF2',
    'chart_4': '#FF375F',
    'chart_5': '#FF9F0A',
}

# Custom CSS for professional minimalistic design
st.markdown(f"""
    <style>
        /* Main background */
        .stApp {{
            background-color: {COLORS['background']};
        }}

        /* Sidebar styling */
        [data-testid="stSidebar"] {{
            background-color: {COLORS['card_bg']};
            border-right: 1px solid {COLORS['border']};
        }}

        [data-testid="stSidebar"] .css-1d391kg {{
            color: {COLORS['text_primary']};
        }}

        /* Headers */
        h1, h2, h3 {{
            color: {COLORS['text_primary']} !important;
            font-weight: 600 !important;
            letter-spacing: -0.5px !important;
        }}

        h1 {{
            font-size: 2.5rem !important;
            margin-bottom: 0.5rem !important;
        }}

        h2 {{
            font-size: 1.75rem !important;
            margin-top: 2rem !important;
            margin-bottom: 1rem !important;
        }}

        h3 {{
            font-size: 1.25rem !important;
            font-weight: 500 !important;
            color: {COLORS['text_secondary']} !important;
        }}

        /* Metric cards */
        [data-testid="stMetricValue"] {{
            color: {COLORS['text_primary']};
            font-size: 2rem !important;
            font-weight: 600 !important;
        }}

        [data-testid="stMetricLabel"] {{
            color: {COLORS['text_secondary']};
            font-size: 0.875rem !important;
            text-transform: uppercase;
            letter-spacing: 1px;
            font-weight: 500;
        }}

        /* Cards */
        .metric-card {{
            background: {COLORS['card_bg']};
            border: 1px solid {COLORS['border']};
            border-radius: 12px;
            padding: 1.5rem;
            transition: all 0.2s ease;
        }}

        .metric-card:hover {{
            background: {COLORS['card_hover']};
            border-color: {COLORS['primary']};
        }}

        /* Tables */
        .dataframe {{
            background-color: {COLORS['card_bg']} !important;
            color: {COLORS['text_primary']} !important;
            border: 1px solid {COLORS['border']} !important;
        }}

        .dataframe th {{
            background-color: {COLORS['card_hover']} !important;
            color: {COLORS['text_secondary']} !important;
            text-transform: uppercase;
            font-size: 0.75rem;
            letter-spacing: 1px;
            font-weight: 600;
            padding: 1rem !important;
        }}

        .dataframe td {{
            color: {COLORS['text_primary']} !important;
            padding: 0.75rem !important;
            border-bottom: 1px solid {COLORS['border']} !important;
        }}

        /* Buttons */
        .stButton button {{
            background-color: {COLORS['primary']};
            color: {COLORS['text_primary']};
            border: none;
            border-radius: 8px;
            padding: 0.5rem 1.5rem;
            font-weight: 500;
            transition: all 0.2s ease;
        }}

        .stButton button:hover {{
            background-color: {COLORS['secondary']};
            transform: translateY(-1px);
        }}

        /* Divider */
        hr {{
            border-color: {COLORS['border']};
            margin: 2rem 0;
        }}

        /* Text */
        p, span, label {{
            color: {COLORS['text_secondary']} !important;
        }}

        /* Remove default padding */
        .block-container {{
            padding-top: 2rem;
            padding-bottom: 2rem;
        }}

        /* Selectbox */
        .stSelectbox {{
            color: {COLORS['text_primary']};
        }}

        /* Chart containers */
        .plotly {{
            background-color: {COLORS['card_bg']};
            border-radius: 12px;
            border: 1px solid {COLORS['border']};
        }}
    </style>
""", unsafe_allow_html=True)

# Load data
@st.cache_data
def load_data():
    feature_importance = pd.read_csv('feature_importance.csv')
    powerbi_data = pd.read_csv('powerbi_data.csv')
    return feature_importance, powerbi_data

try:
    feature_importance, powerbi_data = load_data()

    # Sidebar navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.radio(
        "",
        ["Overview", "Product Analysis", "Pricing Intelligence", "Feature Insights", "Data Explorer"],
        label_visibility="collapsed"
    )

    st.sidebar.markdown("---")
    st.sidebar.markdown(f"**Total Products:** {len(powerbi_data):,}")
    st.sidebar.markdown(f"**Data Points:** {len(powerbi_data) * len(powerbi_data.columns):,}")

    # OVERVIEW PAGE
    if page == "Overview":
        st.title("Analytics Overview")
        st.markdown("### Key Performance Metrics")

        # Top metrics
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric(
                label="Total Products",
                value=f"{len(powerbi_data):,}",
                delta=None
            )

        with col2:
            avg_rating = powerbi_data['rating'].mean()
            st.metric(
                label="Average Rating",
                value=f"{avg_rating:.2f}",
                delta=None
            )

        with col3:
            avg_discount = powerbi_data['discount_percentage'].mean()
            st.metric(
                label="Average Discount",
                value=f"{avg_discount:.1f}%",
                delta=None
            )

        with col4:
            avg_price = powerbi_data['discounted_price'].mean()
            st.metric(
                label="Average Price",
                value=f"₹{avg_price:,.0f}",
                delta=None
            )

        st.markdown("---")

        # Charts
        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### Rating Distribution")
            rating_counts = powerbi_data['rating'].value_counts().sort_index()
            fig = go.Figure(data=[
                go.Bar(
                    x=rating_counts.index,
                    y=rating_counts.values,
                    marker_color=COLORS['chart_1'],
                    marker_line_color=COLORS['border'],
                    marker_line_width=1
                )
            ])
            fig.update_layout(
                plot_bgcolor=COLORS['card_bg'],
                paper_bgcolor=COLORS['card_bg'],
                font_color=COLORS['text_secondary'],
                xaxis=dict(title="Rating", gridcolor=COLORS['border']),
                yaxis=dict(title="Count", gridcolor=COLORS['border']),
                margin=dict(l=20, r=20, t=20, b=20),
                height=350
            )
            st.plotly_chart(fig, use_container_width=True)

        with col2:
            st.markdown("### Price Range Distribution")
            price_bins = [0, 500, 1000, 2000, 5000, 10000, 100000]
            price_labels = ['0-500', '501-1K', '1K-2K', '2K-5K', '5K-10K', '10K+']
            powerbi_data['price_range'] = pd.cut(powerbi_data['discounted_price'], bins=price_bins, labels=price_labels)
            price_dist = powerbi_data['price_range'].value_counts()

            fig = go.Figure(data=[
                go.Pie(
                    labels=price_dist.index,
                    values=price_dist.values,
                    hole=0.5,
                    marker=dict(
                        colors=[COLORS['chart_1'], COLORS['chart_2'], COLORS['chart_3'], 
                               COLORS['chart_4'], COLORS['chart_5'], COLORS['secondary']],
                        line=dict(color=COLORS['background'], width=2)
                    )
                )
            ])
            fig.update_layout(
                plot_bgcolor=COLORS['card_bg'],
                paper_bgcolor=COLORS['card_bg'],
                font_color=COLORS['text_secondary'],
                showlegend=True,
                margin=dict(l=20, r=20, t=20, b=20),
                height=350
            )
            st.plotly_chart(fig, use_container_width=True)

        st.markdown("### Category Performance")
        category_stats = powerbi_data.groupby('main_category').agg({
            'product_id': 'count',
            'rating': 'mean',
            'discounted_price': 'mean',
            'discount_percentage': 'mean'
        }).round(2).reset_index()
        category_stats.columns = ['Category', 'Count', 'Avg Rating', 'Avg Price', 'Avg Discount']

        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=category_stats['Category'],
            y=category_stats['Count'],
            name='Product Count',
            marker_color=COLORS['chart_1'],
            yaxis='y'
        ))
        fig.add_trace(go.Scatter(
            x=category_stats['Category'],
            y=category_stats['Avg Rating'],
            name='Avg Rating',
            marker_color=COLORS['chart_4'],
            yaxis='y2',
            mode='lines+markers',
            line=dict(width=3)
        ))

        fig.update_layout(
            plot_bgcolor=COLORS['card_bg'],
            paper_bgcolor=COLORS['card_bg'],
            font_color=COLORS['text_secondary'],
            xaxis=dict(title="", gridcolor=COLORS['border']),
            yaxis=dict(title="Product Count", gridcolor=COLORS['border'], side='left'),
            yaxis2=dict(title="Average Rating", overlaying='y', side='right', range=[0, 5]),
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
            margin=dict(l=20, r=20, t=40, b=20),
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)

    # PRODUCT ANALYSIS PAGE
    elif page == "Product Analysis":
        st.title("Product Analysis")

        st.markdown("### Top Rated Products")
        top_rated = powerbi_data.nlargest(10, 'rating')[['product_name', 'rating', 'rating_count', 'discounted_price']].copy()
        top_rated.columns = ['Product Name', 'Rating', 'Reviews', 'Price']
        top_rated['Price'] = top_rated['Price'].apply(lambda x: f"₹{x:,.0f}")
        top_rated.index = range(1, len(top_rated) + 1)
        st.dataframe(top_rated, use_container_width=True, height=400)

        st.markdown("---")

        st.markdown("### Category Statistics")
        category_stats = powerbi_data.groupby('main_category').agg({
            'product_id': 'count',
            'rating': 'mean',
            'discounted_price': 'mean',
            'discount_percentage': 'mean'
        }).round(2).reset_index()
        category_stats.columns = ['Category', 'Products', 'Avg Rating', 'Avg Price', 'Avg Discount %']
        category_stats['Avg Price'] = category_stats['Avg Price'].apply(lambda x: f"₹{x:,.0f}")
        category_stats.index = range(1, len(category_stats) + 1)
        st.dataframe(category_stats, use_container_width=True)

        st.markdown("---")

        st.markdown("### Rating vs Review Count")
        sample_data = powerbi_data.sample(min(500, len(powerbi_data)))
        fig = px.scatter(
            sample_data,
            x='rating_count',
            y='rating',
            color='discount_percentage',
            size='discounted_price',
            hover_data=['product_name'],
            color_continuous_scale=['#0A84FF', '#BF5AF2', '#FF375F']
        )
        fig.update_layout(
            plot_bgcolor=COLORS['card_bg'],
            paper_bgcolor=COLORS['card_bg'],
            font_color=COLORS['text_secondary'],
            xaxis=dict(title="Review Count", gridcolor=COLORS['border'], type='log'),
            yaxis=dict(title="Rating", gridcolor=COLORS['border']),
            margin=dict(l=20, r=20, t=20, b=20),
            height=500
        )
        st.plotly_chart(fig, use_container_width=True)

    # PRICING INTELLIGENCE PAGE
    elif page == "Pricing Intelligence":
        st.title("Pricing Intelligence")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Median Price", f"₹{powerbi_data['discounted_price'].median():,.0f}")
        with col2:
            st.metric("Max Discount", f"{powerbi_data['discount_percentage'].max():.0f}%")
        with col3:
            savings = (powerbi_data['actual_price'] - powerbi_data['discounted_price']).sum()
            st.metric("Total Savings", f"₹{savings:,.0f}")

        st.markdown("---")

        st.markdown("### Top Discounted Products")
        top_discounts = powerbi_data.nlargest(10, 'discount_percentage')[
            ['product_name', 'discount_percentage', 'actual_price', 'discounted_price']
        ].copy()
        top_discounts['Savings'] = top_discounts['actual_price'] - top_discounts['discounted_price']
        top_discounts.columns = ['Product Name', 'Discount %', 'Original Price', 'Discounted Price', 'Savings']
        top_discounts['Original Price'] = top_discounts['Original Price'].apply(lambda x: f"₹{x:,.0f}")
        top_discounts['Discounted Price'] = top_discounts['Discounted Price'].apply(lambda x: f"₹{x:,.0f}")
        top_discounts['Savings'] = top_discounts['Savings'].apply(lambda x: f"₹{x:,.0f}")
        top_discounts['Discount %'] = top_discounts['Discount %'].apply(lambda x: f"{x:.0f}%")
        top_discounts.index = range(1, len(top_discounts) + 1)
        st.dataframe(top_discounts, use_container_width=True, height=400)

        st.markdown("---")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### Price Distribution")
            fig = go.Figure(data=[
                go.Histogram(
                    x=powerbi_data['discounted_price'],
                    nbinsx=50,
                    marker_color=COLORS['chart_1'],
                    marker_line_color=COLORS['border'],
                    marker_line_width=1
                )
            ])
            fig.update_layout(
                plot_bgcolor=COLORS['card_bg'],
                paper_bgcolor=COLORS['card_bg'],
                font_color=COLORS['text_secondary'],
                xaxis=dict(title="Price", gridcolor=COLORS['border']),
                yaxis=dict(title="Frequency", gridcolor=COLORS['border']),
                margin=dict(l=20, r=20, t=20, b=20),
                height=350
            )
            st.plotly_chart(fig, use_container_width=True)

        with col2:
            st.markdown("### Discount Distribution")
            fig = go.Figure(data=[
                go.Histogram(
                    x=powerbi_data['discount_percentage'],
                    nbinsx=30,
                    marker_color=COLORS['chart_3'],
                    marker_line_color=COLORS['border'],
                    marker_line_width=1
                )
            ])
            fig.update_layout(
                plot_bgcolor=COLORS['card_bg'],
                paper_bgcolor=COLORS['card_bg'],
                font_color=COLORS['text_secondary'],
                xaxis=dict(title="Discount %", gridcolor=COLORS['border']),
                yaxis=dict(title="Frequency", gridcolor=COLORS['border']),
                margin=dict(l=20, r=20, t=20, b=20),
                height=350
            )
            st.plotly_chart(fig, use_container_width=True)

    # FEATURE INSIGHTS PAGE
    elif page == "Feature Insights":
        st.title("Feature Insights")

        st.markdown("### Feature Importance Analysis")

        col1, col2 = st.columns([1, 1])

        with col1:
            fig = go.Figure(data=[
                go.Bar(
                    y=feature_importance['Feature'],
                    x=feature_importance['Importance'] * 100,
                    orientation='h',
                    marker=dict(
                        color=feature_importance['Importance'] * 100,
                        colorscale=[[0, COLORS['chart_1']], [1, COLORS['chart_4']]],
                        line=dict(color=COLORS['border'], width=1)
                    )
                )
            ])
            fig.update_layout(
                plot_bgcolor=COLORS['card_bg'],
                paper_bgcolor=COLORS['card_bg'],
                font_color=COLORS['text_secondary'],
                xaxis=dict(title="Importance (%)", gridcolor=COLORS['border']),
                yaxis=dict(title="", gridcolor=COLORS['border']),
                margin=dict(l=20, r=20, t=20, b=20),
                height=400
            )
            st.plotly_chart(fig, use_container_width=True)

        with col2:
            fig = go.Figure(data=[
                go.Pie(
                    labels=feature_importance['Feature'],
                    values=feature_importance['Importance'],
                    hole=0.4,
                    marker=dict(
                        colors=[COLORS['chart_1'], COLORS['chart_2'], COLORS['chart_3'], 
                               COLORS['chart_4'], COLORS['chart_5']],
                        line=dict(color=COLORS['background'], width=2)
                    )
                )
            ])
            fig.update_layout(
                plot_bgcolor=COLORS['card_bg'],
                paper_bgcolor=COLORS['card_bg'],
                font_color=COLORS['text_secondary'],
                showlegend=True,
                margin=dict(l=20, r=20, t=20, b=20),
                height=400
            )
            st.plotly_chart(fig, use_container_width=True)

        st.markdown("---")

        st.markdown("### Feature Statistics")
        feature_stats = feature_importance.copy()
        feature_stats['Importance (%)'] = (feature_stats['Importance'] * 100).round(2)
        feature_stats = feature_stats.sort_values('Importance', ascending=False)
        feature_stats.index = range(1, len(feature_stats) + 1)
        st.dataframe(feature_stats[['Feature', 'Importance (%)']], use_container_width=True)

        st.markdown("---")

        st.markdown("### Key Insights")
        col1, col2, col3 = st.columns(3)

        with col1:
            st.info(f"**Primary Feature**: {feature_importance.iloc[0]['Feature']} contributes {feature_importance.iloc[0]['Importance']*100:.1f}% to predictions")

        with col2:
            price_importance = feature_importance[feature_importance['Feature'].str.contains('price')]['Importance'].sum()
            st.info(f"**Price Features**: Combined importance of {price_importance*100:.1f}%")

        with col3:
            st.info(f"**Rating Impact**: {feature_importance[feature_importance['Feature']=='rating']['Importance'].values[0]*100:.1f}% importance in model")

    # DATA EXPLORER PAGE
    else:
        st.title("Data Explorer")

        st.markdown("### Dataset Overview")

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Total Records", f"{len(powerbi_data):,}")
        with col2:
            st.metric("Total Columns", len(powerbi_data.columns))
        with col3:
            st.metric("Categories", powerbi_data['main_category'].nunique())
        with col4:
            st.metric("Price Range", f"₹{powerbi_data['discounted_price'].min():.0f} - ₹{powerbi_data['discounted_price'].max():,.0f}")

        st.markdown("---")

        # Filters
        st.markdown("### Filters")
        col1, col2, col3 = st.columns(3)

        with col1:
            categories = ['All'] + list(powerbi_data['main_category'].unique())
            selected_category = st.selectbox("Category", categories)

        with col2:
            min_rating = st.slider("Minimum Rating", 0.0, 5.0, 0.0, 0.1)

        with col3:
            max_price = st.slider("Maximum Price", 0, int(powerbi_data['discounted_price'].max()), 
                                 int(powerbi_data['discounted_price'].max()))

        # Filter data
        filtered_data = powerbi_data.copy()
        if selected_category != 'All':
            filtered_data = filtered_data[filtered_data['main_category'] == selected_category]
        filtered_data = filtered_data[
            (filtered_data['rating'] >= min_rating) & 
            (filtered_data['discounted_price'] <= max_price)
        ]

        st.markdown(f"### Filtered Results: {len(filtered_data):,} products")

        # Display filtered data
        display_columns = ['product_name', 'rating', 'rating_count', 'discounted_price', 
                          'actual_price', 'discount_percentage', 'main_category']
        display_data = filtered_data[display_columns].copy()
        display_data.columns = ['Product', 'Rating', 'Reviews', 'Price', 'Original Price', 'Discount %', 'Category']
        display_data.index = range(1, len(display_data) + 1)

        st.dataframe(display_data, use_container_width=True, height=500)

        # Download button
        csv = filtered_data.to_csv(index=False)
        st.download_button(
            label="Download Filtered Data",
            data=csv,
            file_name="filtered_products.csv",
            mime="text/csv"
        )

except Exception as e:
    st.error(f"Error loading data: {str(e)}")
    st.info("Please ensure 'feature_importance.csv' and 'powerbi_data.csv' are in the same directory as this script.")
