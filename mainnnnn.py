from flask import Flask, request, jsonify, render_template
from datetime import datetime
import pymongo
from cls_old.account import Account
from company import Company
from cls_old.bus import Bus
from driver import Driver
from seat import Seat
from trip import Trip
from station import Stations
import pprint
from bson.objectid import ObjectId

def init_database_mongo():
    myclient = pymongo.MongoClient("mongodb+srv://65015166:B_as180844@kmitl-cluster.7zb2wsc.mongodb.net/?retryWrites=true&w=majority")
    database = myclient.BusTicket
    return database

app = Flask(__name__)

@app.route('/register_account')
def register_account():
    account = Account("65015166@kmitl.ac.th", "082-3632737", "65015166", "Anurak", "Siwaboonya", 1)
    account_docs = account.create_account()
    account_collection = init_database_mongo().account
    account_collection.insert_one(account_docs)
    return "Hello World"

@app.route('/add_company')
def add_company():
    company = Company("company1@gmail.com", "0xx-xxxxxxx", "11111111" ,"imag.png", "company1", 2)
    company_docs = company.create_company_docs()
    company_collection = init_database_mongo().company
    company_collection.insert_one(company_docs)
    return "add_company"

@app.route('/add_bus')
def add_bus():
    _id = ObjectId("644ccbc4e29a3e1a6dc5a361")
    bus = Bus("BK101", "RED", _id)
    for i in range(1,11):
        bus.add_seat(Seat(i, True))
    bus_docs = bus.create_bus_docs()
    bus_collection = init_database_mongo().bus
    bus_collection.insert_one(bus_docs)
    return "add_bus"

@app.route('/add_driver')
def add_driver():
    id_bus = ObjectId("644d01807ec49ffeba7a2983")
    driver = Driver("65015166@kmitl.ac.th", "082-3632737", "65015166", "hannae", "888", 3, id_bus)
    driver_docs = driver.create_driver()
    pprint.pprint(driver_docs)
    driver_collection = init_database_mongo().driver
    driver_collection.insert_one(driver_docs)
    return "Creat driver"

@app.route('/')
def find_account():
    driver_collection = init_database_mongo().driver
    a = driver_collection.find_one({'_id': ObjectId('644d15e1f0b52864cf4b0856')})
    pprint.pprint(a)

    bus_collection = init_database_mongo().bus
    b = bus_collection.find_one({'_id': a['bus_driver']})
    pprint.pprint(b['seats'][0])
    return "Creat driver"

@app.route('/add_trip')
def add_trip():
    company_collection = init_database_mongo().company
    company = company_collection.find_one({'_id': ObjectId('644ccbc4e29a3e1a6dc5a361')})
    trip = Trip(500, "กรุงเทพ", "เชียงใหม่", 90, company)
    trip_docs = trip.creat_doc()
    trip_collection = init_database_mongo().trip
    trip_collection.insert_one(trip_docs)
    return "Creat trip"

@app.route('/add_departure_station')
def add_departure_station():
    _id_trip = ObjectId("644d2b856f0a21ef09296d52")
    departure_station = Stations("ท่ารถ 2", 30)
    departure_station_docs = departure_station.create_departure_docs()
    
    trip_collection = init_database_mongo().trip
    # coll.update({'ref': ref}, {'$push': {'tags': new_tag}})

    trip_collection.update({'_id' : _id_trip}, {'$push' : {'departure_stations' : departure_station_docs}})
    return "Add Departure Station"
    
@app.route('/add_terminal_stations')
def add_terminal_station():
    _id_trip = ObjectId("644d2b856f0a21ef09296d52")
    terminal_station = Stations("ท่ารถเชียงใหม่", 420)
    terminal_station_docs = terminal_station.create_departure_docs()
    
    trip_collection = init_database_mongo().trip
    # coll.update({'ref': ref}, {'$push': {'tags': new_tag}})

    trip_collection.update({'_id' : _id_trip}, {'$push' : {'terminal_stations' : terminal_station_docs}})
    return "Add Terminal Station"

if __name__ == "__main__":
    app.run(debug=True)