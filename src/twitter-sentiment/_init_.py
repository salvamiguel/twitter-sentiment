from TweetExtractor import TweetExtractor
from TweetSentimentAnalizer import TweetSentimentAnalizer

extractor = TweetExtractor('', "./input.xlsx")
analizer = TweetSentimentAnalizer()
tweets = extractor.pull_queries(extractor.get_queries())
analizer.from_list(extractor.workbook, tweets)