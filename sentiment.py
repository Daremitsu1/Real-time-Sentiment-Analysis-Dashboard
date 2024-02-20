import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer

# Load CSV file
tweets_df = pd.read_csv("tweets.csv")

# Initialize SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()

# Perform sentiment analysis
sentiments = []
for text in tweets_df["text"]:
    sentiment_score = sia.polarity_scores(text)["compound"]
    if sentiment_score > 0.05:
        sentiment = "Positive"
    elif sentiment_score < -0.05:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
    sentiments.append(sentiment)

# Add sentiment column to DataFrame
tweets_df["sentiment"] = sentiments

# Save DataFrame with sentiment analysis results as a new CSV file
tweets_df.to_csv("tweets_with_sentiment.csv", index=False)
