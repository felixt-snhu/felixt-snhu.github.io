import json
                          
from pymongo import MongoClient, errors
import dbcfg


class DbConnection():
    def __init__(self, db_name, collection):
        self.connection = MongoClient(dbcfg.SERVER_CONNECTION_STRING)
        self.db = self.connection[db_name]
        self.collection = self.db[collection]

    def create_document(self, document):
                                          
                                                            
                  
        print("attempting to insert document %s into collection" % document)

        try:
            result = self.collection.insert_one(json.loads(document))
        except errors.OperationFailure as e:
            return e.details

        return result.acknowledged

    def update_volume(self, ticker, volume):
        if len(ticker) == 0:
            print("Please provide a valid ticker name")
            return
        if int(volume) <= 0:
            print("Volume value must be greater than 0")
            return
        print("Update ticker %s volume to %s" % (ticker, volume))

        try:
            self.collection.update_one({"Ticker": ticker}, {"$set": {"Volume": volume}})
        except errors.OperationFailure as e:
            return e.details

        find = self.collection.find_one({"Ticker": ticker})
        return find

    def update_recommendation(self, ticker, score):
        if len(ticker) == 0:
            print("Please provide a valid ticker name")
            return
        if int(score) <= 0:
            print("Score value must be greater than 0")
            return
        print("Update ticker %s score to %s" % (ticker, score))

        try:
            self.collection.update_one({"Ticker": ticker}, {"$set": {"Analyst Recom": score}})
        except errors.OperationFailure as e:
            return e.details

        find = self.collection.find_one({"Ticker": ticker})
        return find

    def delete_document(self, ticker):
        print("Delete ticker %s" % ticker)

        try:
            result = self.collection.find_one_and_delete({"Ticker": ticker})
        except errors.OperationFailure as e:
            return e.details

        print("Ticker %s deleted" % ticker)
        return result

                                                        
                                    

    def get_industry_tickers(self, industry):
        try:
            results = self.collection.find({"Industry": "%s" % industry}, {"Ticker": 1, "_id": 0})
        except errors.OperationFailure as e:
            return e.details

        response = []
        for doc in results:
            response.append(str(doc['Ticker']))
        return response

    def get_countries(self):
        try:
            results = self.collection.find({}, {"Country": 1, "_id": 0})
        except errors.OperationFailure as e:
            return e.details

        response = []
        for doc in results:
            try:
                if str(doc['Country']) not in response:    # eliminate duplicates
                    response.append(str(doc['Country']))
            except:
                pass
        return response

    def get_sectors(self):
        try:
            results = self.collection.find({}, {"Sector": 1, "_id": 0})
        except errors.OperationFailure as e:
            return e.details

        response = []
        for doc in results:
            try:
                if str(doc['Sector']) not in response:    # eliminate duplicates
                    response.append(str(doc['Sector']))
            except:
                pass
        return response

    def get_industries(self):
        try:
            results = self.collection.find({}, {"Industry": 1, "_id": 0})
        except errors.OperationFailure as e:
            return e.details

        response = []
        for doc in results:
            try:
                if str(doc['Industry']) not in response:    # eliminate duplicates
                    response.append(str(doc['Industry']))
            except:
                pass
        return response

    def get_50_day_simple_moving_avg_count(self, low, high):
        query = {"50-Day Simple Moving Average": {"$lt": high, "$gt": low}}
        try:
            results = self.collection.find(query)
        except errors.OperationFailure as e:
            return e.details
        return results.count()

    def get_total_outstanding_shares_by_sector(self, sector):
        pipeline = [{"$project": {"Sector": 1, "Industry": 1, "Shares Outstanding": 1}},
                    {"$match": {"Sector": "%s" % sector}},
                    {"$group": {"_id": "null", "Shares Outstanding": {"$sum": "$Shares Outstanding"}}}]
        try:
            results = self.collection.aggregate(pipeline)
        except errors.OperationFailure as e:
            return e.details
        return list(results)

    def get_stock_price_by_sector_by_country(self, sector, country):
        pipeline = [{"$project": {"Sector": 1, "Country": 1, "Price": 1, "Ticker": 1, "_id": 0}},
                    {"$match": {"Sector": "%s" % sector, "Country": "%s" % country}}]
        try:
            results = self.collection.aggregate(pipeline)
        except errors.OperationFailure as e:
            return e.details
        return list(results)

    def get_stock_price_by_industry_by_country(self, sector, country):
        pipeline = [{"$project": {"Industry": 1, "Country": 1, "Price": 1, "Ticker": 1, "_id": 0}},
                    {"$match": {"Industry": "%s" % sector, "Country": "%s" % country}}]
        try:
            results = self.collection.aggregate(pipeline)
        except errors.OperationFailure as e:
            return e.details
        return list(results)

    def get_stock_recommendation_score_by_sector_by_country(self, sector, country):
        pipeline = [{"$project": {"Sector": 1, "Country": 1, "Analyst Recom": 1, "Ticker": 1, "_id": 0}},
                    {"$match": {"Sector": "%s" % sector, "Country": "%s" % country}}]
        try:
            results = self.collection.aggregate(pipeline)
        except errors.OperationFailure as e:
            return e.details
        return list(results)

    def get_stock_recommendation_score_by_industry_by_country(self, sector, country):
        pipeline = [{"$project": {"Industry": 1, "Country": 1, "Analyst Recom": 1, "Ticker": 1, "_id": 0}},
                    {"$match": {"Industry": "%s" % sector, "Country": "%s" % country}}]
        try:
            results = self.collection.aggregate(pipeline)
        except errors.OperationFailure as e:
            return e.details
        return list(results)

    def get_analyst_recommendation_score(self, ticker):
        try:
            results = self.collection.find({"Ticker": "%s" % ticker}, {"Analyst Recom": 1, "_id": 0})
        except errors.OperationFailure as e:
            return e.details

        response = []
        for doc in results:
            response.append(str(doc['Analyst Recom']))
        return response
