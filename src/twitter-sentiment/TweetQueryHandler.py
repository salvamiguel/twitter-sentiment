from tweepy import *
from TweetQuery import TweetQuery
from TweetContainer import TweetContainer

class TweetQueryHandler:
    def __init__(self, twitter_client: Client, query: TweetQuery) -> None:
        self.client = twitter_client
        self.query = query
        self.next_token = query.next_token
    
    def pull(self) -> list[TweetContainer]:
        remaining_tweets = 15 #self.query.max_results
        tweets = []
        while(remaining_tweets > 0):
            data, includes, errors, meta = self.client.search_all_tweets(
                    self.query.query + " -is:retweet lang:es",
                    start_time = self.query.start_date,
                    end_time = self.query.end_date,
                    max_results = min(500, self.query.max_results),
                    next_token = self.next_token,
                ) 
            for tweet in data:
                tweets.append(TweetContainer(tweet))
            
            remaining_tweets = max(remaining_tweets - meta["result_count"], 0)
            self.next_token = meta["next_token"]
        return tweets
        

