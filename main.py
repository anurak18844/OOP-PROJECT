import json
import os
from flask import Flask, redirect, url_for, render_template, request, jsonify
from datetime import datetime
import pymongo
import pprint
from bson.objectid import ObjectId
from cls_obj.company import Company
from cls_obj.driver import Driver
from werkzeug.utils import  secure_filename
from init_database_mongo import InitDatabaseMongoDB
from cls_obj.bus import Bus
from cls_obj.trip import Trip
from cls_obj.tripinstance import TripInStance
from cls_obj.user import User

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = "cairocoders-tutorial101"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS   

@app.route("/add_company")
def home():
    return render_template("add_company.html")

@app.route("/add_company_post", methods=["POST"])
def add_company():
    img_name = []
    email = request.form['email']
    password = request.form['password']
    phone = request.form['phone']
    full_name = request.form['fullname']
    files = request.files.getlist('files[]')
    for file in files:
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            img_name.append(filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    company = Company(email, phone, password, full_name, 2,img_name[0])

    count_email = company.check_count_email()
    if count_email > 0 :
        message = {"message":"Email Not Unique"}
        resp = jsonify(message)
        return resp
    
    message = {"message" : company.insert_data()}
    resp = jsonify(message)
    return resp

@app.route("/home_company/<user>", methods=["GET"])
def home_company(user):
    id = user
    print("_id", id)
    company_collection = InitDatabaseMongoDB().account
    company = company_collection.find({"_id": ObjectId(id)})
    return render_template('home_company.html', id_company = id)

@app.route("/add_bus/<id_company>",  methods=["GET"])
def add_bus_page(id_company):
    id_company = id_company
    return render_template('add_bus_page.html',id_company = id_company)

@app.route("/add_trip/<id_company>", methods=['GET'])
def add_trip_page(id_company):
    id_company = id_company
    return render_template('add_trip_page.html', id_company = id_company)

@app.route("/add_trip", methods=['POST'])
def add_trip():
    id_company = request.form['idcompany']
    price = request.form['price']
    departure_point = request.form['departure_point']
    destination_point = request.form['destination_point']
    departure_station = request.form['departure_station']
    destination_station = request.form['destination_station']
    company_collection = InitDatabaseMongoDB().account
    companies = company_collection.find({"_id": ObjectId(id_company)})
    
    company = {
        "_id": str(companies[0]["_id"]),
        "phone": companies[0]['phone'],
        "img":companies[0]['img'],
        "company_name": companies[0]['company_name'],
    }
    trip = Trip(price, departure_point, destination_point, departure_station, destination_station, company)
    message = trip.insert_data()
    return jsonify({"message": message})

@app.route("/add_bus", methods=["POST"])
def add_bus():
    id_company = request.form['idcompany']
    bus_number = request.form['busnumber']
    bus_color = request.form['buscolor']
    bus = Bus(bus_number, bus_color, id_company)
    message = {"message" : bus.insert_data()}
    resp = jsonify(message)
    return resp

@app.route("/add_driver/<id_company>",  methods=["GET"])
def add_driver_page(id_company):
    id_company = id_company
    bus_collection = InitDatabaseMongoDB().bus
    bus = bus_collection.find({"owner_id": id_company})
    return render_template('add_driver_page.html',id_company = id_company, bus = bus)

@app.route("/add_driver", methods=["POST"])
def add_driver():
    id_company = request.form['idcompany']
    bus_number = request.form['busnumber']
    print("busnumber is ", bus_number)
    fullname = request.form['fullname']
    email = request.form['email']
    password = request.form['password']
    phone = request.form['phone']
    driver = Driver(email, phone, password, fullname, 3, bus_number)
    message = {"message" : driver.insert_data()}
    resp = jsonify(message)
    return resp

@app.route("/add_trip_instance_page/<id_company>",  methods=["GET"])
def add_trip_instance_page(id_company):
    id_company = id_company
    trip_collection = InitDatabaseMongoDB().trip
    trips = trip_collection.find({"company._id" : id_company})
    return render_template('add_trip_instance_page.html',trips = trips)

@app.route("/add_trip_instance/<id_trip>", methods=["GET"])
def add_trip_instance(id_trip):
    id_trip = id_trip
    trip_collection = InitDatabaseMongoDB().trip
    trips = trip_collection.find({"_id" : ObjectId(id_trip)})
    trip = trips[0]
    bus_collection = InitDatabaseMongoDB().bus
    id_company = trip['company']['_id']
    buss = bus_collection.find({"owner_id" : id_company})
    trip_instance_collecton = InitDatabaseMongoDB().trip_instance
    trip_instances = trip_instance_collecton.find({"trip._id" : ObjectId(id_trip),'trip.company._id' : id_company})
    # p = trip_instance_collecton.find({'trip[_id]' : '6452254fdadf26f7fccf7c74'})
    # for i in p:
    #     pprint.pprint(i)
    return render_template("add_trip_instance.html", trip = trip, buss = buss, trip_instances = trip_instances)

@app.route("/add_trip_instance_post", methods=['POST'])
def add_trip_instance_post():
    id_trip = request.form['id_trip']
    date = request.form['date']
    time = request.form['time']
    id_bus = request.form['id_bus']
    print(id_bus)
    trip__collection = InitDatabaseMongoDB().trip
    trip = trip__collection.find({'_id' : ObjectId(id_trip)})
    pprint.pprint(trip[0])
    trip_instance = TripInStance(date, time, trip[0], id_bus)
    return jsonify({"message" : trip_instance.insert_data()})


@app.route("/login", methods=["POST"])
def login():
    email = request.form['email']
    password = request.form['password']
    caccount_collection = InitDatabaseMongoDB().account
    count_accout = caccount_collection.find({"email" : email, "password" : password}).count()
    if count_accout == 0:
        resp = jsonify({"message":"Not Have Accout"})
        return resp
    account = caccount_collection.find({"email" : email, "password" : password})
    print('------------------------------------------')
    id = str(account[0]['_id'])
    user_type = account[0]['user_type']
    print('------------------------------------------')
    resp = jsonify({"id" : id, "user_type" : user_type})
    return resp

@app.route('/register_page')
def register_page():
    return render_template("register_page.html")

@app.route('/register', methods=['POST'])
def register():
    email = request.form['email']
    password = request.form['password']
    phone = request.form['phone']
    name = request.form['name']
    lastname = request.form['lastname']
    full_name = f"{name} {lastname}"
    user = User(email, phone, password, full_name, 4)
    count_email = user.check_count_email()
    if count_email > 0 :
        message = {"message":"Email Not Unique"}
        resp = jsonify(message)
        return resp
    
    message = {"message" : user.insert_data()}
    resp = jsonify(message)
    return resp

@app.route("/home_user/<user>", methods=["GET"])
def home_user(user):
    id = user
    trip_collection = InitDatabaseMongoDB().trip
    trips = trip_collection.find()
    departure_point = []
    destination_point = []
    for trip in trips:
        departure_point.append(trip['departure_point'])
        destination_point.append(trip['destination_point'])
    print(departure_point)
    print(destination_point)
    return render_template('home_user_page.html', user_id = id, departure_point = departure_point, destination_point = destination_point)

@app.route('/search_trip_instance', methods=['POST'])
def search_trip_instance():
    departure_point = request.form['departure_point']
    destination_point = request.form['destination_point']
    date = request.form['date']
    trip_instance_collecntion = InitDatabaseMongoDB().trip_instance
    # count_accout = caccount_collection.find({"email" : email, "password" : password}).count()
    count_trip_instance = trip_instance_collecntion.find({"trip.departure_point" : departure_point, "trip.destination_point" : destination_point, "date" : date}).count()
    if count_trip_instance == 0:
        return jsonify({'count' : count_trip_instance, 'message' : 'ไม่พบข้อมูลการเดินทางที่ท่านต้องการ'})
    
    path = f"{departure_point}/{destination_point}/{date}"
    return jsonify({"path" : path})

@app.route('/<user_id>/searched_trip_instance/<departure_point>/<destination_point>/<date>', methods=['GET'])
def searhed_trip_instance(user_id, departure_point, destination_point, date):
    user_id = user_id
    departure_point = departure_point
    destination_point = destination_point
    date = date
    trip_instance_collecntion = InitDatabaseMongoDB().trip_instance
    trip_instances = trip_instance_collecntion.find({"trip.departure_point" : departure_point, "trip.destination_point" : destination_point, "date" : date})
    return render_template("select_trip_instance.html",trip_instances = trip_instances, user_id = user_id)

@app.route('/select_seat/<user_id>/<trip_instance_id>', methods=['GET'])
def select_seat_page(user_id, trip_instance_id):
    user_id = user_id
    trip_instance_id = trip_instance_id
    trip_instance_collection = InitDatabaseMongoDB().trip_instance
    trips = trip_instance_collection.find({'_id': ObjectId(trip_instance_id)})
    trip = trips[0]
    bus_collection = InitDatabaseMongoDB().bus
    buss = bus_collection.find({"_id":ObjectId(trip['id_bus'])})
    bus = buss[0]
    list_seates = bus['seats']
     # TEST INSERT TICKET
    ticket_collection = InitDatabaseMongoDB().ticket
    # ticket_collection.insert_one({'seat' : 'A1', 'trip_instance' : trip})
     # TEST INSERT TICKET
    print(trip_instance_id)
    tickets = ticket_collection.find({"trip_instance._id" : ObjectId(trip_instance_id)})
    list_seates_from_ticket = []
    for i in tickets:
        list_seates_from_ticket.append(i['seat'])

    for i in list_seates:
        if i in list_seates_from_ticket:
            print(i)
    return render_template('select_seate_page.html',user_id = user_id, trip_instance_id = trip_instance_id, list_seates = list_seates, list_seates_from_ticket = list_seates_from_ticket)

@app.route("/login_page")
def login_page():
    return render_template('login_page.html')


if __name__ == "__main__":
    app.run(debug=True)