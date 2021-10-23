from datetime import datetime
class TweetQuery:
    def __init__(self, query: str, start_date: datetime, end_date: datetime, max_results: int, next_api_token: str = None) -> None:
        self.query = query
        self.start_date = start_date
        self.end_date = end_date
        self.max_results = max_results
        self.next_token = next_api_token

    def __repr__(self) ->str:
        return 'TweetQuery(query: {}, start_date: {}, end_date: {}, max_results: {})'.format(self.query, self.start_date, self.end_date, self.max_results)
    def __str__(self) -> str:
        return 'TweetQuery(query: {}, start_date: {}, end_date: {}, max_results: {})'.format(self.query, self.start_date, self.end_date, self.max_results)
