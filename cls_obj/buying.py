from datetime import datetime
import sys
sys.path.append("../init_database_mongo.py") 
from init_database_mongo import InitDatabaseMongoDB
import pprint

class Buying():
    def __init__(self,amount,buy_status,tickets,owner_id):
        self.__amount = amount
        self.__buy_status = buy_status
        self.__transaction = ''
        self.__date = datetime.now().strftime("%m-%d-%Y")
        self.__tickets = tickets
        self.__owner_id = owner_id

    @property
    def amount(self):
        return self.__amount
    
    @property
    def buy_status(self):
        return self.__buy_status
    
    @property
    def transaction(self):
        return self.__transaction
    
    @property
    def date(self):
        return self.__date
    
    @property
    def tickets(self):
        return self.__tickets
    
    @property
    def owner_id(self):
        return self.__owner_id

    @amount.setter
    def amount(self, amount):
        self.__amount = amount

    @buy_status.setter
    def buy_status(self, buy_status):
        self.__buy_status = buy_status

    @transaction.setter
    def transaction(self, transaction):
        self.__transaction = transaction
    
    @date.setter
    def date(self, date):
        self.__date = date

    @tickets.setter
    def ticekt(self, tickets):
        self.__tickets= tickets

    @owner_id.setter
    def owner_id(self, owner_id):
        self.__owner_id = owner_id

    def create_docs(self):
        docs = {
        "amount" : self.__amount,
        "buy_status" : self.__buy_status,
        "transaction" : self.__transaction,
        "date" : self.__date,
        "tickets" : self.__tickets,
        "owner_id" : self.__owner_id
        }

        return docs
    
    def insert_data(self):
        buying_collection = InitDatabaseMongoDB().buying
        docs = self.create_docs()
        id = buying_collection.insert_one(docs).inserted_id
        pprint.pprint(docs)

        return id