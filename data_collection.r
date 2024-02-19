library(rtweet, help, pos = 2, lib.loc = NULL)

# Authenticate with Twitter API
api_key <- "aiv1GCTX8YbG5qFIjZwdiOVW6"
api_secret <- "trm7utKb6lJ6BOjhLQoMurllOVvTsuozWaxzfCw2xBFefM8Dum"
access_token <- "1457242372606103554-zzAQ6B9anWJsd3icaoaBNjegss84lF"
access_secret <- "S7A2OZLzkVZtQmthJl9bxOJQ6SoDrBsdwEBBLZoL9ZQ6c"

create_token(
  app = "Twitter_Sentiment_aviparna",
  consumer_key = api_key,
  consumer_secret = api_secret,
  access_token = access_token,
  access_secret = access_secret
)

# Search for tweets containing specific keywords
tweets <- search_tweets(
  "data science",  # Replace with your desired keywords
  n = 1000,  # Number of tweets to retrieve
  include_rts = FALSE
)

# Basic preprocessing
clean_tweets <- tweets %>%
  select(text) %>%
  mutate(clean_text = gsub("http\\S+|www\\S+|[^[:alnum:][:space:]_]", "", text)) %>%
  select(clean_text)

# View the preprocessed data
head(clean_tweets)