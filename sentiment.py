import pandas as pd
from textblob import TextBlob

def perform_sentiment_analysis(tweets_df):
    sentiments = []
    for text in tweets_df["text"]:
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity
        if polarity > 0:
            sentiment = "Positive"
        elif polarity < 0:
            sentiment = "Negative"
        else:
            sentiment = "Neutral"
        sentiments.append(sentiment)
    tweets_df["sentiment"] = sentiments
    return tweets_df

def save_sentiment_analysis_results(tweets_df, output_file):
    tweets_df.to_csv(output_file, index=False)

# Load tweets data from CSV
try:
    tweets_df = pd.read_csv("tweets.csv")
except FileNotFoundError:
    print("Error: File not found")
    exit(1)

# Perform sentiment analysis
try:
    tweets_df = perform_sentiment_analysis(tweets_df)
except Exception as e:
    print("Error:", e)
    exit(1)

# Save sentiment analysis results
try:
    save_sentiment_analysis_results(tweets_df, "tweets_with_sentiment.csv")
    print("Sentiment analysis results saved successfully")
except Exception as e:
    print("Error:", e)
    exit(1)
