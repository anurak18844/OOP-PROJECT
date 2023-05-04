import sys
sys.path.append("../init_database_mongo.py") 
from init_database_mongo import InitDatabaseMongoDB
from pymongo import MongoClient
from .account import Account
import io

class Company(Account):
    def __init__(self, email, phone, password, fullname, user_type, img):
        super().__init__(email, phone, password, fullname, user_type)
        self.__img = img

    @property
    def img(self):
        return self.__img

    @img.setter
    def img(self, new_img):
        self.__img = new_img
    
    def __str__(self):
        return f"email : {self.__email}, phone : {self.__phone}, password : {self.__password}, fullname: {self.__fullname},user_type : {self.__user_type}, img : {self.__img}"
    
    def check_count_email(self):
        company_collection = InitDatabaseMongoDB().account
        count = company_collection.find({"email" : self.email}).count()
        print(count)
        return count

    def create_company_docs(self):
        company_docs = {
            "email" : self.email,
            "phone" : self.phone,
            "password" : self.password,
            "img" : self.__img,
            "company_name" : self.fullname,
            "user_type" : self.user_type
        }
        return company_docs
    
    def insert_data(self):
        company_docs = self.create_company_docs()
        company_collection = InitDatabaseMongoDB().account
        company_collection.insert_one(company_docs)
        return "ADD COMPANY SUCESS!"
        