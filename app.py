import streamlit as st
import pandas as pd
import plotly.express as px

# Title
st.title("🎬 Netflix AI Dashboard")

# Load Dataset
df = pd.read_csv("netflix_titles.csv")

# Data Cleaning
df.drop_duplicates(inplace=True)
df.fillna("Unknown", inplace=True)

# Sidebar Filter
st.sidebar.header("Filters")

selected_type = st.sidebar.selectbox(
    "Select Content Type",
    ["All"] + list(df["type"].unique())
)

if selected_type != "All":
    df = df[df["type"] == selected_type]

# Dataset Overview
st.header("Dataset Overview")

st.write("Rows:", df.shape[0])
st.write("Columns:", df.shape[1])

st.dataframe(df.head())

# KPIs
st.header("Key Metrics (KPIs)")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Titles", len(df))
col2.metric("Movies", len(df[df["type"] == "Movie"]))
col3.metric("TV Shows", len(df[df["type"] == "TV Show"]))
col4.metric("Countries", df["country"].nunique())

# Visualization 1
st.header("Movies vs TV Shows")

fig1 = px.pie(
    df,
    names="type",
    title="Movies vs TV Shows"
)

st.plotly_chart(fig1)

# Visualization 2
st.header("Netflix Content Released Over Years")

year_count = df["release_year"].value_counts().sort_index()

fig2 = px.line(
    x=year_count.index,
    y=year_count.values,
    labels={"x":"Release Year","y":"Number of Titles"},
    title="Netflix Content Released Over Years"
)

st.plotly_chart(fig2)

# Visualization 3
st.header("Top 10 Countries")

top_countries = df["country"].value_counts().head(10)

fig3 = px.bar(
    x=top_countries.index,
    y=top_countries.values,
    labels={"x":"Country","y":"Number of Titles"},
    title="Top 10 Countries by Netflix Content"
)

st.plotly_chart(fig3)

# Visualization 4
st.header("Content Rating Distribution")

fig4 = px.histogram(
    df,
    x="rating",
    title="Distribution of Ratings"
)

st.plotly_chart(fig4)

# Visualization 5
st.header("Movies and TV Shows Across Years")

fig5 = px.scatter(
    df,
    x="release_year",
    y="type",
    title="Movies and TV Shows Across Years"
)

st.plotly_chart(fig5)