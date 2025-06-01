import tweepy
import pandas as pd
import datetime

# Twitter API credentials
API_KEY = "PGQ83tDpr2IoAQ0mKDghZzOD8"
API_SECRET_KEY = "QTRAXwrGHiT4I5q3wh23j3gP2Bq8kmnNura8wHBplqubcPafDb"
ACCESS_TOKEN = "1868350774910283776-NczRTgkl3mog0mZBg98KRsexnFRwcZ"
ACCESS_TOKEN_SECRET = "R9I6QkOcxVXBoTTFcHbiYppKAWsYoNDf2lg1sTCqOod11"

# Authenticate with Twitter API
auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

def collect_tweets_from_twitter(keywords, max_tweets_per_keyword=20):
    """
    Collects tweets based on multiple keywords using the Twitter API.
    """
    tweets_data = []
    try:
        # Loop through each keyword and collect tweets
        for keyword in keywords:
            for tweet in tweepy.Cursor(api.search_tweets, q=keyword, lang="en", tweet_mode="extended").items(max_tweets_per_keyword):
                tweets_data.append({
                    "created_at": tweet.created_at,
                    "user": tweet.user.screen_name,
                    "text": tweet.full_text,
                    "likes": tweet.favorite_count,
                    "retweets": tweet.retweet_count,
                    "location": tweet.user.location or "Unknown",
                    "keyword": keyword  # Add the keyword for reference
                })

        # Convert to DataFrame
        df = pd.DataFrame(tweets_data)
        return df

    except tweepy.TweepyException as e:
        print(f"Error: {e}")
        return pd.DataFrame()

# List of keywords to search tweets
keywords = [
    "The future of technology is here with AI advancements.",
    "Excited about the new breakthroughs in quantum computing!",
    "5G networks are reshaping connectivity like never before.",
    "Artificial intelligence is driving the tech world forward.",
    "Cloud computing ensures scalability for businesses globally.",
    "Digital transformation is crucial for modern enterprises.",
    "Quantum algorithms are the next big leap for tech.",
    "Cybersecurity remains the top priority for organizations.",
    "IoT is revolutionizing smart home devices worldwide.",
    "Robotics is creating efficiencies in industrial workflows."
]

# Number of tweets to fetch per keyword
max_tweets_per_keyword = 20  # Adjust as needed

# Collect tweets
tweets_df = collect_tweets_from_twitter(keywords, max_tweets_per_keyword)

# Save tweets to a CSV file
output_file = f"twitter_data_keywords_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.csv"
tweets_df.to_csv(output_file, index=False)
print(f"Data collected and saved to {output_file}")

# Display sample data
print(tweets_df.head())
