from DbConnection import DbConnection
import json

class Trader:
    def __init__(self):
        self.__str__ = "Trader"
        self.email = ""
        self.company = ""
        self.db = DbConnection('market', 'stocks')    # create database connection object
        self.menu_options = [x for x in dir(self) if x.startswith("m_")]  # create options menu for user using class attributes

        #menu = {}
        #menu_item_number = 0
        #for item in self.menu_options:
        #    menu[menu_item_number] = item
        #    menu_item_number += 1
        #for option_num, option_name in menu.items():
        #    print("%s. %s" % (option_num, option_name))

        while True:
            # get input from user prompt and call the appropriate function name 
            menu = input("\nOptions:\n=============\nEnter name of option and press ENTER, or 'q' to quit:\n\n%s\n>" % "\n".join(self.menu_options))
            if menu == "q":
                print("Good bye!")
                return
            try:
                func = getattr(self, menu)
                print(func())
            except AttributeError:
                print("Invalid option name")

    def m_get_industry_tickers(self):
        """Get Industry tickers"""
        industry = input("Enter name of industry and press ENTER: ")
        return self.db.get_industry_tickers(industry)

    def m_get_50_day_simple_moving_avg_count(self):
        """Get 50 day simple moving average count"""
        low = input("Enter lower threshold value for 50 day average count and press ENTER: ")
        high = input("Enter high threshold value for 50 day average count and press ENTER: ")
        return self.db.get_50_day_simple_moving_avg_count(low, high)

    def m_get_total_outstanding_shares_by_sector(self):
        """Get total outstanding shares by sector"""
        sector = input("Enter name of sector and press ENTER: ")
        return self.db.get_total_outstanding_shares_by_sector(sector)

    def m_get_analyst_recommendation_score(self):  # new function
        """Get tickers recommended by analysts where score greater than low"""
        ticker = input("Enter name of ticker and press ENTER: ")
        return self.db.get_analyst_recommendation_score(ticker)


class Manager(Trader):
    def __init__(self):
        super().__init__()
        self.__str__ = "Hedge Fund Manager"
                                 

    def m_create_document(self):
        """Create document"""
        document = input("Enter Document in key, value pair format and press ENTER: ")
        return self.db.create_document(document)

    def m_update_volume(self):
        """Update ticker volume"""
        ticker = input("Enter ticker symbol and press ENTER: ")
        volume = input("Enter volume for ticker and press ENTER: ")
        return self.db.update_volume(ticker, volume)

    def m_update_document(self):  # new function
        """Update document"""
        document = input("Enter Document in key, value pair format and press ENTER: ")
        return self.db.update_document(document)

    def m_delete_document(self):
        """Delete document"""
        ticker = input("Enter ticker symbol and press ENTER: ")
        return self.db.delete_document(ticker)



