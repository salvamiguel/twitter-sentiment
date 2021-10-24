from tweepy import *
from TweetQuery import TweetQuery
from TweetContainer import TweetContainer
from tqdm import tqdm
class TweetQueryHandler:
    def __init__(self, twitter_client: Client, query: TweetQuery) -> None:
        self.client = twitter_client
        self.query = query
        self.next_token = query.next_token
    
    def pull(self) -> list[TweetContainer]:
        remaining_tweets = min(self.query.max_results, 1048575) #max num rows excel sheet
        tweets = []
        while(remaining_tweets > 0):
            data, includes, errors, meta = self.client.search_all_tweets(
                    self.query.query + " -is:retweet lang:es",
                    start_time = self.query.start_date,
                    end_time = self.query.end_date,
                    max_results = min(500, remaining_tweets),
                    next_token = self.next_token,
                ) 
                
            for tweet in tqdm(data, "Guardando tweets"):
                tweets.append(TweetContainer(tweet))
            
            remaining_tweets = remaining_tweets - meta["result_count"]
            print("Pulling {} tweets. {} tweets remaining.".format(self.query.query, remaining_tweets))
            if "next_token" in meta.keys():
                self.next_token = meta["next_token"]
            else:
                remaining_tweets = 0

        return tweets
        

