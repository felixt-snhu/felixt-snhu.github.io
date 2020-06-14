from DbConnection import DbConnection
import pandas as pd
import matplotlib.pyplot as plot


class Trader:
    def __init__(self):
        self.__str__ = "Trader"
        self.email = ""
        self.company = ""
        self.db = DbConnection('market', 'stocks')    # create database connection object
        self.menu_options = [x for x in dir(self) if x.startswith("m_")]  # create options menu for user using class attributes

        while True:
            self._menu()
            # get input from user prompt and call the appropriate function name
            try:
                option_num = int(input("Enter option number and press ENTER, or 0 to quit: "))
                if option_num == 0:
                    print("Good bye!")
                    return
                try:
                    func = getattr(self, self.menu[option_num])
                    print(func())
                except AttributeError:
                    print("Unable to retrieve function name %s from menu option" % self.menu[option_num])
            except:
                print("Invalid option")

    def _menu(self):
        print("\nMenu\n====")
        self.menu = {}
        menu_item_number = 1
        for item in self.menu_options:
            self.menu[menu_item_number] = item
            menu_item_number += 1
        for option_num, option_name in self.menu.items():
            print("%s. %s" % (option_num, option_name))

    def m_get_industry_tickers(self):
        """Get Industry tickers"""
        industry = input("Enter name of industry and press ENTER: ")
        return self.db.get_industry_tickers(industry)

    def m_get_countries(self):
        """Get list of countries"""
        countries = self.db.get_countries()
        print("\nCountries\n=======")
        for country in countries:
            print(country)

    def m_get_sectors(self):
        """Get list of sectors"""
        sectors = self.db.get_sectors()
        print("\nSectors\n=======")
        for sector in sectors:
            print(sector)

    def m_get_industries(self):
        """Get list of industries"""
        industries = self.db.get_industries()
        print("\nIndustries\n=======")
        for industry in industries:
            print(industry)

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

    def m_plot_stock_price_by_sector_by_country(self):
        """Generate box plot for stock prices by sector by country"""
        sector = input("Enter name of sector and press ENTER: ")
        country = input("Enter name of country and press ENTER: ")
        dataset = self.db.get_stock_price_by_sector_by_country(sector, country)
        data_frame = pd.DataFrame(dataset, columns=['Price', 'Ticker'])
        try:
            data_frame.plot.bar(x='Ticker', y='Price', rot=90, title="Stock prices for %s sector in %s" % (sector, country))
            plot.show(block=True)
        except TypeError:
            print("No data to plot")

    def m_plot_stock_price_by_industry_by_country(self):
        """Generate box plot for stock prices by industry by country"""
        industry = input("Enter name of industry and press ENTER: ")
        country = input("Enter name of country and press ENTER: ")
        dataset = self.db.get_stock_price_by_industry_by_country(industry, country)
        data_frame = pd.DataFrame(dataset, columns=['Price', 'Ticker'])
        try:
            data_frame.plot.bar(x='Ticker', y='Price', rot=90,
                                title="Stock prices for %s industry in %s" % (industry, country))
            plot.show(block=True)
        except TypeError:
            print("No data to plot")

    def m_plot_stock_recommendation_score_by_sector_by_country(self):
        """Generate box plot for stock recommendation scores by sector by country"""
        sector = input("Enter name of sector and press ENTER: ")
        country = input("Enter name of country and press ENTER: ")
        dataset = self.db.get_stock_recommendation_score_by_sector_by_country(sector, country)
        data_frame = pd.DataFrame(dataset, columns=['Analyst Recom', 'Ticker'])
        try:
            data_frame.plot.bar(x='Ticker', y='Analyst Recom', rot=90, title="Analyst recommendation scores for %s sector in %s" % (sector, country))
            plot.show(block=True)
        except TypeError:
            print("No Data to plot")

    def m_plot_stock_recommendation_score_by_industry_by_country(self):
        """Generate box plot for stock recommendation scores by sector by country"""
        industry = input("Enter name of industry and press ENTER: ")
        country = input("Enter name of country and press ENTER: ")
        dataset = self.db.get_stock_recommendation_score_by_industry_by_country(industry, country)
        data_frame = pd.DataFrame(dataset, columns=['Analyst Recom', 'Ticker'])
        try:
            data_frame.plot.bar(x='Ticker', y='Analyst Recom', rot=90,
                                title="Analyst recommendation scores for %s industry in %s" % (industry, country))
            plot.show(block=True)
        except TypeError:
            print("No Data to plot")


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

                                                        
                             
                                                

    def m_delete_document(self):
        """Delete document"""
        ticker = input("Enter ticker symbol and press ENTER: ")
        return self.db.delete_document(ticker)

    def m_update_analyst_recommendation_score(self):
        """Update analyst recommendation score"""
        ticker = input("Enter ticker symbol and press ENTER: ")
        score = input("Enter new score: ")
        return self.db.update_recommendation(ticker, score)



