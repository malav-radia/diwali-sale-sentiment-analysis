# 📊 Diwali Sale Pulse: Twitter Sentiment Analysis

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](YOUR_STREAMLIT_APP_URL_HERE)

This is an end-to-end data science project that analyzes public sentiment on X (Twitter) regarding the major 2025 Indian e-commerce sales: Flipkart's "Big Billion Days" and Amazon's "Great Indian Festival."

The project covers the complete data pipeline: from live data collection and NLP preprocessing to building and deploying an interactive web dashboard.

## 🚀 Live Dashboard

You can view and interact with the live project here:
**[Click to open the Streamlit Dashboard](YOUR_STREAMLIT_APP_URL_HERE)**



---

## Core Features

* **Key Metrics:** View top-level metrics like total tweets analyzed, average sentiment score, and counts of positive vs. negative tweets.
* **Dynamic Filtering:** Filter the entire dashboard by sentiment (Positive, Negative, or Neutral) using the sidebar.
* **Interactive Visuals:** An interactive Plotly pie chart shows the sentiment distribution, and a dynamic word cloud displays the most common words.
* **Data Explorer:** Browse and search the raw tweet text and its corresponding sentiment score in a data table.

---

## 🛠️ Tech Stack & Libraries

* **Python:** Core programming language.
* **Data Collection:** Tweepy (for accessing the X API).
* **Data Manipulation:** Pandas & NumPy.
* **Text Preprocessing:** NLTK (tokenization, stopwords, lemmatization).
* **Sentiment Analysis:** VADER (Valence Aware Dictionary and sEntiment Reasoner).
* **Visualization:** Plotly (interactive charts), WordCloud, Matplotlib.
* **Deployment:** Streamlit & Streamlit Community Cloud.

---

## 🔬 Project Workflow

1.  **Data Collection:** Wrote a Python script using `tweepy` to connect to the X API and scrape 101 live tweets containing keywords like `#BigBillionDays` and `#GreatIndianFestival`. The data was limited due to the Free API tier's monthly cap.
2.  **Data Preprocessing:** Cleaned the raw tweet text by removing URLs, mentions, hashtags, and punctuation. Used NLTK to tokenize the text, remove stopwords, and lemmatize words to their root form.
3.  **Sentiment Analysis:** Applied the pre-trained VADER model to the cleaned text to assign a compound sentiment score (from -1 to +1) to each tweet. These scores were then classified as 'Positive', 'Negative', or 'Neutral'.
4.  **Deployment:** Built an interactive web application with `streamlit` to present the findings. The app was connected to the GitHub repository and deployed on Streamlit Community Cloud.

---

## 💡 Key Finding: Model Bias

A key insight from this project was discovering the limitations of a pre-trained model like VADER.

* **The Result:** The dashboard showed an overwhelmingly positive sentiment (89%).
* **The "Why":** Upon manual inspection, it was clear that VADER was misinterpreting **neutral marketing language** as genuinely positive. Tweets like "Don't miss out on **deals** for your **favorite** Hisense products" were flagged as "Positive" due to words like "deals" and "favorite," even though the tweet's *intent* is purely promotional.
* **Conclusion:** This highlights a critical challenge in sentiment analysis: distinguishing between genuine customer emotion and neutral brand advertising. A future improvement would be to train a custom ML model on labeled data to make this distinction.

---

## 🚀 How to Run This Locally

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/malav-radia/diwali-sale-sentiment-analysis.git](https://github.com/malav-radia/diwali-sale-sentiment-analysis.git)
    ```
2.  **Navigate to the project directory:**
    ```bash
    cd diwali-sale-sentiment-analysis
    ```
3.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    venv\Scripts\activate  # On Windows
    # source venv/bin/activate  # On macOS/Linux
    ```
4.  **Install the required libraries:**
    ```bash
    pip install -r requirements.txt
    ```
5.  **Run the Streamlit app:**
    ```bash
    streamlit run app.py
    ```
