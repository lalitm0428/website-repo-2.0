import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide",page_title="Mclaren Strategy Dashboard")

@st.cache_data
def get_data():
    return pd.read_csv('f1_clean_data.csv')

df = get_data()

st.sidebar.title("Race Controls")
race_filter = st.sidebar.selectbox("Select Grand Prix",df['Race'].unique())
compound_filter = st.sidebar.selectbox("Select Compounds",df['NOR_COMPOUND'].unique()),
default=df['NOR_COMPOUND'].unique()

filtered_df = df[(df['Race'] == race_filter)&(df['NOR_COMPOUND'].isin(compound_filter))]

st.title("Telemetry Analysis: {race_filter} GP")

col1,col2,col3,col4 = st.columns(4)
avg_pace = filtered_df['NOR_TIME'].mean()
best_lap = filtered_df['NOR_TIME'].min()

col1.metric("Avg Lap Time",f"{avg_pace:.3f}s")
col2.metric("Best Lap",f"{best_lap:.3f}s")
col3.metric("Laps Analyzed",f"{len(filtered_df)}")
col4.metric("Compounds Used", len(filtered_df['NOR_COMPOUND'].unique()))

tab1,tab2 = st.tabs(["Pace Evolution","Tire Deg"])

with tab1:
    st.subheader("Lap Time vs. Lap Number")
    fig_pace = px.line(filtered_df, x='LAP', y='NOR_TIME', color='NOR_COMPOUND', markers=True)
    fig_pace.update_yaxes(autorange="reversed") 
    st.plotly_chart(fig_pace, use_container_width=True)

with tab2:
    st.subheader("Tire Degradation Curve")
    fig_deg = px.scatter(filtered_df, x='NOR_TIRE_LIFE', y='NOR_TIME', color='NOR_COMPOUND', trendline="ols")
    st.plotly_chart(fig_deg, use_container_width=True)

with tab3:
    st.subheader("Sector Analysis")
    fig_sector = px.box(filtered_df, x='SECTOR', y='NOR_TIME', color='NOR_COMPOUND')
    st.plotly_chart(fig_sector, use_container_width=True)tab3: 

    