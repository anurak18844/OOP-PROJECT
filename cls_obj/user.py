from .account import Account
import sys
sys.path.append("../init_database_mongo.py") 
from init_database_mongo import InitDatabaseMongoDB
class User(Account):
    def __init__(self, email, phone, password, fullname, user_type):
        super().__init__(email, phone, password, fullname, user_type)

    def check_count_email(self):
        user_collection = InitDatabaseMongoDB().account
        count = user_collection.find({"email" : self.email}).count()
        print(count)
        return count
    
    def create_docs(self):
        docs = {
            "email": self.email,
            "phone": self.phone,
            "password": self.password,
            "full_name":self.fullname,
            "user_type": self.user_type
        }

        return docs

    def insert_data(self):
        user_collection = InitDatabaseMongoDB().account
        docs = self.create_docs()
        user_collection.insert_one(docs)
        return "REGISTER SUCCESS!"
