import sys
sys.path.append("../init_database_mongo.py") 
from init_database_mongo import InitDatabaseMongoDB
class Ticket():
    def __init__(self, seat, trip_instance):
        self.__seat = seat
        self.__trip_instance = trip_instance

    @property
    def seat(self):
        return self.__seat
    
    @property
    def trip_instance(self):
        return self.__trip_instance
    
    @seat.setter
    def seat(self, seat):
        self.__seat = seat

    @trip_instance.setter
    def trip_instance(self, trip_instance):
        self.__trip_instance = trip_instance

    def create_docs(self):
        docs = {
            "seat": self.__seat,
            "trip_instance": self.__trip_instance
        }

        return docs
    
    def insert_data(self):
        ticket_collection = InitDatabaseMongoDB().ticket
        docs = self.create_docs()
        ticket_collection.insert_one(docs)

        return "SUCCESS"
        