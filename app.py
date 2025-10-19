import streamlit as st
import pandas as pd
import plotly.express as px
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# -----------------
# PAGE CONFIGURATION
# -----------------
# This sets the layout of your page. "wide" uses the full screen.
st.set_page_config(layout="wide", page_title="Diwali Sale Pulse")


# -----------------
# DATA LOADING
# -----------------
# We use @st.cache_data to load the data once and store it.
# This makes the app much faster.
@st.cache_data
def load_data():
    try:
        df = pd.read_csv('data/processed_tweets.csv')
        # Convert CreatedAt to datetime so we can sort by it
        df['CreatedAt'] = pd.to_datetime(df['CreatedAt'])
        return df
    except FileNotFoundError:
        st.error("ERROR: 'processed_tweets.csv' not found.")
        st.error("Please run the notebook '2_data_processing_and_eda.ipynb' first.")
        return pd.DataFrame() # Return an empty dataframe if file not found

df = load_data()

# Stop the app if data is not loaded
if df.empty:
    st.stop()

# -----------------
# MAIN APP
# -----------------
st.title("📊 Diwali Sale Pulse: Twitter Sentiment Analysis")
st.markdown(f"This dashboard analyzes sentiment from **{len(df)}** tweets about the 2025 Diwali e-commerce sales.")
st.markdown("---") # Adds a horizontal line

# -----------------
# SIDEBAR FILTERS
# -----------------
# The sidebar is great for filters.
st.sidebar.header("Filter Data")
sentiment_filter = st.sidebar.multiselect(
    "Select Sentiment",
    options=df['Sentiment'].unique(),  # Gets all unique values (Positive, Negative, Neutral)
    default=df['Sentiment'].unique()   # By default, all are selected
)

# Filter the dataframe based on the user's selection
df_selection = df[df['Sentiment'].isin(sentiment_filter)]

# Stop the app if the selection is empty
if df_selection.empty:
    st.warning("No data selected. Please choose at least one sentiment from the sidebar.")
    st.stop() # Halts the app from running further

# -----------------
# KEY METRICS
# -----------------
# Displaying top-level numbers
total_tweets = len(df_selection)
avg_sentiment_score = round(df_selection['SentimentScore'].mean(), 2)
positive_count = len(df_selection[df_selection['Sentiment'] == 'Positive'])
negative_count = len(df_selection[df_selection['Sentiment'] == 'Negative'])

st.subheader("Selected Data Metrics")
col1, col2, col3, col4 = st.columns(4) # Create 4 columns
with col1:
    st.metric("Total Tweets", f"{total_tweets}")
with col2:
    st.metric("Avg. Sentiment", f"{avg_sentiment_score}")
with col3:
    st.metric("Positive Tweets", f"{positive_count}", delta_color="normal")
with col4:
    st.metric("Negative Tweets", f"{negative_count}", delta_color="inverse")

st.markdown("---") # Horizontal line

# -----------------
# VISUALIZATIONS
# -----------------
# We'll put our pie chart and word cloud side-by-side in 2 columns
viz_col1, viz_col2 = st.columns(2)

with viz_col1:
    # --- PIE CHART ---
    st.subheader("Sentiment Distribution")
    sentiment_counts = df_selection['Sentiment'].value_counts()
    fig_pie = px.pie(values=sentiment_counts.values,
                     names=sentiment_counts.index,
                     color=sentiment_counts.index,
                     color_discrete_map={'Positive':'#34A853', 'Negative':'#EA4335', 'Neutral':'#FBBC05'})
    st.plotly_chart(fig_pie, use_container_width=True) # Display the chart

with viz_col2:
    # --- WORD CLOUD ---
    st.subheader("Most Common Words")
    # Join all text into one big string
    all_text = " ".join(tweet for tweet in df_selection['CleanedText'].astype(str))
    
    if all_text.strip():
        # Create the word cloud
        wordcloud = WordCloud(width=400, height=200, background_color='white').generate(all_text)
        
        # Display with matplotlib
        fig_wc, ax = plt.subplots(figsize=(10,5))
        ax.imshow(wordcloud, interpolation='bilinear')
        ax.axis('off')
        st.pyplot(fig_wc) # Use st.pyplot() to show matplotlib plots
    else:
        st.write("No words to display for this selection.")

# -----------------
# DATA TABLE
# -----------------
st.subheader("Tweet Data Explorer")
st.markdown("View the raw tweets, sentiment, and scores.")
# Show the dataframe on the page
st.dataframe(df_selection[['CreatedAt', 'Text', 'Sentiment', 'SentimentScore']], use_container_width=True)

# --- Your Project Insight ---
st.subheader("Project Insights")
st.info(
    "**Observation:** The sentiment is overwhelmingly positive (89%).\n\n"
    "**Reasoning:** This is likely due to the VADER model misinterpreting neutral advertising language "
    "(e.g., 'deals', 'favorite', 'extraordinary') as genuinely positive customer sentiment. "
    "A future improvement would be to train a custom model to distinguish between promotional content and real user opinions."
)