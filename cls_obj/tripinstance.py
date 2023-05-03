import sys
sys.path.append("../init_database_mongo.py") 
from init_database_mongo import InitDatabaseMongoDB
class TripInStance:
    def __init__(self, date_time, trip,id_bus):
        self.__id = None
        self.__trip = trip
        self.__date_time = date_time
        self.__id_bus= id_bus

    @property
    def id(self):
        return self.__id
    
    @property
    def trip(self):
        return self.__trip
        
    @property
    def date_time(self):
        return self.__date_time
    
    @property
    def id_bus(self):
        return self.__id_bus
    
    @id.setter
    def id(self, id):
        self.__id = id

    @trip.setter
    def trip(self, trip):
        self.__trip = trip

    @date_time.setter
    def date_time(self, date_time):
        self.__date_time = date_time

    @id_bus.setter
    def id_bus(self, id_bus):
        self.__id_bus = id_bus

    def create_docs(self):
        docs = {
            "date_time": self.__date_time,
            "id_bus": self.__id_bus,
            "trip": self.__trip
        }

        return docs
    
    def insert_data(self):
        docs = self.create_docs()
        trip_instance_collectipn = InitDatabaseMongoDB().trip_instance
        trip_instance_collectipn.insert_one(docs)

        return "INSERT TRIP INSTANCE SUCCESS!"
        