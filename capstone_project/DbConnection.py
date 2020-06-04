import json
from bson import json_util
from pymongo import MongoClient
import dbcfg


class DbConnection():
    def __init__(self, db_name, collection):
        self.connection = MongoClient(dbcfg.SERVER_CONNECTION_STRING)
        self.db = self.connection[db_name]
        self.collection = self.db[collection]

    def create_document(self, document):
        if not isinstance(document, dict):
            print("Input parameter is not a valid document")
            return
        print("attempting to insert document %s into collection" % document)

        try:
            result = self.collection.insert_one(document)
        except errors.OperationFailure as e:
            return e.details

        return result.acknowledged

    def update_volume(self, ticker, volume):
        if len(ticker) == 0:
            print("Please provide a valid ticker name")
            return
        if volume <= 0:
            print("Volume value must be greater than 0")
            return
        print("Update ticker %s volume to %s" % (ticker, volume))

        try:
            update = self.collection.update_one({"Ticker": ticker}, {"$set": {"Volume": volume}})
        except errors.OperationFailure as e:
            return e.details

        find = self.collection.find_one({"Ticker": ticker})
        return json.dumps(find, sort_keys=True, indent=4, default=json_util.default)

    def update_recommendation(self, ticker, score):  # new function
        if len(ticker) == 0:
            print("Please provide a valid ticker name")
            return
        if score <= 0:
            print("Score value must be greater than 0")
            return
        print("Update ticker %s score to %s" % (ticker, score))

        try:
            update = self.collection.update_one({"Ticker": ticker}, {"$set": {"Analyst Recom": score}})
        except errors.OperationFailure as e:
            return e.details

        find = self.collection.find_one({"Ticker": ticker})
        return json.dumps(find, sort_keys=True, indent=4, default=json_util.default)

    def delete_document(self, ticker):
        print("Delete ticker %s" % ticker)

        try:
            result = self.collection.find_one_and_delete({"Ticker": ticker})
        except errors.OperationFailure as e:
            return e.details

        print("Ticker %s deleted" % ticker)
        return result

    def update_document(self, document):  # new function
        return "not yet implemented"

    def get_industry_tickers(self, industry):
        try:
            results = self.collection.find({"Industry": "%s" % industry}, {"Ticker": 1, "_id": 0})
        except errors.OperationFailure as e:
            return e.details

        response = []
        for doc in results:
            response.append(str(doc['Ticker']))
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

    def get_analyst_recommendation_score(self, ticker):  # new function
        try:
            results = self.collection.find({"Ticker": "%s" % ticker}, {"Analyst Recom": 1, "_id": 0})
        except errors.OperationFailure as e:
            return e.details

        response = []
        for doc in results:
            response.append(str(doc['Analyst Recom']))
        return response
