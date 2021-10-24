from pysentimiento.preprocessing import preprocess_tweet
from datetime import datetime
from typing import Tuple
from tweepy import Tweet
import re

class TweetContainer:
    def __init__(self, tweet:Tweet) -> None:
        self.tweet = tweet

    def remove_emoji(self, text):
        regrex_pattern = re.compile(pattern = "["
                u"\U0001F600-\U0001F64F"  # emoticons
                u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                u"\U0001F680-\U0001F6FF"  # transport & map symbols
                u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                u"\U00002702-\U000027B0"
                u"\U000024C2-\U0001F251"
                u"\U0001f926-\U0001f937"
                u'\U00010000-\U0010ffff'
                u"\u200d"
                u"\u2640-\u2642"
                u"\u2600-\u2B55"
                u"\u23cf"
                u"\u23e9"
                u"\u231a"
                u"\u3030"
                u"\ufe0f"
                            "]+", flags = re.UNICODE)
        return regrex_pattern.sub(r'',text)

    def filtered_text(self):
        return preprocess_tweet(self.tweet.text)
    
    def get_row(self) -> Tuple[int, str, datetime, str, str]:
        return (
            self.tweet.id,
            self.tweet.lang,
            self.tweet.created_at,
            self.tweet.text,
            self.filtered_text(),
        )


    def __repr__(self) ->str:
        return 'TweetContainer(filtered_text: {}, text: {}, date: {}, id: {})'.format(self.filtered_text(), self.tweet.text, self.tweet.created_at, self.tweet.data)
    def __str__(self) -> str:
        return 'TweetContainer(filtered_text: {}, text: {}, date: {}, id: {})'.format(self.filtered_text(), self.tweet.text, self.tweet.created_at, self.tweet.data)
