import pymongo
from dotenv import load_dotenv
import os

def InitDatabaseMongoDB():
    load_dotenv()
    pass_word = os.environ['PASSWORD_DB']
    string_connect = f"mongodb+srv://65015166:{pass_word}@kmitl-cluster.7zb2wsc.mongodb.net/?retryWrites=true&w=majority"
    myclient = pymongo.MongoClient(string_connect)
    database = myclient.BusTicket
    return database
