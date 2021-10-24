from TweetExtractor import TweetExtractor
from TweetSentimentAnalyzer import TweetSentimentAnalyzer

analizer = TweetSentimentAnalyzer()
tweets = extractor.pull_queries(extractor.get_queries())
analizer.from_list(extractor.workbook, tweets)