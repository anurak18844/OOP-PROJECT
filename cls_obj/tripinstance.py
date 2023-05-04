import sys
sys.path.append("../init_database_mongo.py") 
from init_database_mongo import InitDatabaseMongoDB
class TripInStance:
    def __init__(self, date, time, trip,id_bus):
        self.__id = None
        self.__trip = trip
        self.__date = date
        self.__time = time
        self.__id_bus= id_bus

    @property
    def id(self):
        return self.__id
    
    @property
    def trip(self):
        return self.__trip
        
    @property
    def date(self):
        return self.__date
    
    @property
    def time(self):
        return self.__time
    
    @property
    def id_bus(self):
        return self.__id_bus
    
    @id.setter
    def id(self, id):
        self.__id = id

    @trip.setter
    def trip(self, trip):
        self.__trip = trip

    @date.setter
    def date(self, date):
        self.__date = date

    @time.setter
    def time(self, time):
        self.__time = time

    @id_bus.setter
    def id_bus(self, id_bus):
        self.__id_bus = id_bus

    def create_docs(self):
        docs = {
            "date": self.__date,
            "time": self.__time,
            "id_bus": self.__id_bus,
            "trip": self.__trip
        }

        return docs
    
    def insert_data(self):
        docs = self.create_docs()
        trip_instance_collectipn = InitDatabaseMongoDB().trip_instance
        trip_instance_collectipn.insert_one(docs)

        return "INSERT TRIP INSTANCE SUCCESS!"
        