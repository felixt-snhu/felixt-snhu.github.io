from DbConnection import DbConnection


class Trader:
    def __init__(self):
        self.__str__ = "Trader"
        self.email = ""
        self.company = ""
        self.db = DbConnection('market', 'stocks')

    def get_industry_tickers(self, industry):
        """Get Industry tickers"""
        return self.db.get_industry_tickers(industry)

    def get_50_day_simple_moving_avg_count(self, low, high):
        """Get 50 day simple moving average count"""
        return self.db.get_50_day_simple_moving_avg_count(low, high)

    def get_total_outstanding_shares_by_sector(self, sector):
        """Get total outstanding shares by sector"""
        return self.db.get_total_outstanding_shares_by_sector(sector)

    def get_analyst_recommendation_score(self, ticker):  # new function
        """Get tickers recommended by analysts where score greater than low"""
        return self.db.get_analyst_recommendation_score(ticker)


class Manager(Trader):
    def __init__(self):
        super().__init__()
        self.__str__ = "Hedge Fund Manager"
        self.managed_tickers = []

    def create_document(self, document):
        """Create document"""
        return self.db.create_document(document)

    def update_volume(self, ticker, volume):
        """Update ticker volume"""
        return self.db.update_volume(ticker, volume)

    def update_document(self, document):  # new function
        """Update document"""
        return self.db.update_document(document)

    def delete_document(self, ticker):
        """Delete document"""
        return self.db.delete_document(ticker)
