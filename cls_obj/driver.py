from cls_old.account import Account
import sys
sys.path.append("../init_database_mongo.py") 
from init_database_mongo import InitDatabaseMongoDB
class Driver(Account):
    def __init__(self, email, phone, password, full_name, user_type, bus_driver):
        super().__init__(email, phone, password, full_name, user_type)
        self.__buss_driver = bus_driver 
    @property
    def bus_driver(self):
        return self.__bus_driver
    
    @bus_driver.setter
    def bus_driver(self, new_bus_driver):
        self.__bus_driver = new_bus_driver

    def __str__(self):
        return f"email : {self.__email}, phone : {self.__phone}, password : {self.__password}, first_name : {self.__first_name}, last_name : {self.__last_name}, user_type : {self.__user_type}, bus_driver : {self.__bus_driver}"
    
    def create_docs(self):
        docs = {
            "email" : self.email,
            "phone" : self.phone,
            "password" : self.password,
            "buss_driver" : self.__buss_driver,
            "full_name" : self.full_name,
            "user_type" : self.user_type
        }
        return docs
    
    def insert_data(self):
        docs = self.create_docs()
        bus_collection = InitDatabaseMongoDB().driver
        bus_collection.insert_one(docs)
        return "ADD DRIVER SUCESS!"