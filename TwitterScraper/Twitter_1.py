# Script Author: Martin Beck
# Medium Article Follow-Along: https://medium.com/better-pr  ogramming/how-to-scrape-tweets-with-snscrape-90124ed006af

# Pip install the command below if you don't have the development version of snscrape 
# !pip install git+https://github.com/JustAnotherArchivist/snscrape.git

# Imports
import snscrape.modules.twitter as sntwitter
import pandas as pd
from datetime import datetime
import os

path = "/Users/shaoc/Desktop/Twitter"
os.chdir(path)

def get_tweets(ticker):
    
    print(ticker, " Start")
    start_time = datetime.now()

    # Creating list to append tweet data to
    tweets_list = []    

    # Define search string
    search_str = "$" + str(ticker) + " since:2019-01-01 until:2020-01-01" 
    
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(search_str).get_items()):
        tweets_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
        print(tweet.date)

    print(ticker, " End")    
    print("Duration: {}".format(datetime.now() - start_time))
    
    # Creating a dataframe from the tweets list above
    tweets_df = pd.DataFrame(tweets_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
    
    # Set file name for exporting
    file_name = str(ticker) + "_tweets_2019.csv"
    
    # Export dataframe into a CSV
    tweets_df.to_csv(file_name , sep = ',', index = False)
    
tickers = ["GOOGL", "NFLX", "AMZN"]

for ticker in tickers[1:]:
    get_tweets(ticker)
    
