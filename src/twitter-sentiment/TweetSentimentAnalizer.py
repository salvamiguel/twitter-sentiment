from sentiment_analysis_spanish import sentiment_analysis
from TweetQueryHandler import TweetQueryHandler
from TweetContainer import TweetContainer
import openpyxl

class TweetSentimentAnalizer:
    
    def __init__(self, lang: str = "es") -> None:
        self.analizer = self.get_analizer(lang)

    def get_analizer(self, lang: str):
        if lang == "es":
            return sentiment_analysis.SentimentAnalysisSpanish().sentiment
        else:
            return False
            #TODO ADD OTHER LANGS

    def from_list(
            self,
            wb: openpyxl.Workbook,  
            queries: list[dict[TweetQueryHandler, list[TweetContainer]]]
        ):
        for query in queries:
            title = query["handler"].query.query
            sheet = None
            if title in wb.sheetnames:
                sheet = wb[title]
            else:
                sheet = wb.create_sheet(title)
                sheet.append(
                        (
                            "tweet_id",
                            "lang",
                            "date",
                            "text",
                            "filtered_text",
                            "evaluation",
                            "result"
                        )
                    )
            for tweet in query["result"]:
                if(isinstance(tweet, TweetContainer)):
                    evaluation = self.analizer(tweet.filtered_text())
                    result = "positive" if evaluation > 0.6 else "neutal" if evaluation > 0.3 else "negative" 
                    sheet.append(
                        tweet.get_row() + (evaluation, result)
                    )
        wb.save("output.xlsx")




