import sys
sys.path.append("../init_database_mongo.py") 
from init_database_mongo import InitDatabaseMongoDB
class Trip:
    def __init__(self, price, departure_point, destination_point, departure_point_station, destination_point_station,company):
        self.__id = None
        self.__price = price
        self.__departure_point = departure_point
        self.__destination_point = destination_point
        self.__departure_point_station = departure_point_station
        self.__destination_point_station = destination_point_station
        self.__company = company

    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, new_id):
        self.__id = new_id

    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, new_price):
        self.__price = new_price

    @property
    def departure_point(self):
        return self.__departure_point
    
    @departure_point.setter
    def departure_point(self, new_departure_point):
        self.__departure_point = new_departure_point
    
    @property
    def destination_point(self):
        return self.__destination_point
    
    @destination_point.setter
    def destination_point(self, new_destination_pont):
        self.__destination_point = new_destination_pont

    @property
    def departure_point_station(self):
        return self.__departure_point_station
    
    @property
    def destination_point_station(self):
        return self.__destination_point_station
    
    @departure_point_station.setter
    def departure_point_station(self, new_departure_point_station):
        self.__departure_point_station = new_departure_point_station

    @destination_point_station.setter
    def destination_point_station(self, new_destination_station):
        self.__destination_point_station = new_destination_station

    def create_docs(self):
        docs = {
            "price" : self.__price,
            "departure_point": self.__departure_point,
            "destination_point": self.__destination_point,
            "departure_station": self.__departure_point_station,
            "destination_station": self.__destination_point_station,
            "company": self.__company
        }

        return docs
    
    def insert_data(self):
        docs = self.create_docs()
        trip_collection = InitDatabaseMongoDB().trip
        trip_collection.insert_one(docs)

        return "INSERT TRIP SUCCESS"
