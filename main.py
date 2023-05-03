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
    a = user
    print(a)
    return render_template('home_company.html', id_company = a)

@app.route("/add_bus/<id_company>",  methods=["GET"])
def add_bus_page(id_company):
    id_company = id_company
    return render_template('add_bus_page.html',id_company = id_company)

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
    return render_template('add_driver_page.html',id_company = id_company)

@app.route("/add_driver", methods=["POST"])
def add_driver():
    id_company = request.form['idcompany']
    bus_number = request.form['busnumber']
    fullname = request.form['fullname']
    email = request.form['email']
    password = request.form['password']
    phone = request.form['phone']
    driver = Driver(email, phone, password, fullname, 3, bus_number)
    message = {"message" : driver.insert_data()}
    resp = jsonify(message)
    return resp

@app.route("/login", methods=["POST"])
def login():
    email = request.form['email']
    password = request.form['password']
    company_collection = InitDatabaseMongoDB().company
    count_accout = company_collection.find({"email" : email, "password" : password}).count()
    if count_accout == 0:
        resp = jsonify({"message":"Not Have Accout"})
        return resp
    company = company_collection.find({"email" : email, "password" : password})
    print('------------------------------------------')
    id = str(company[0]['_id'])
    print('------------------------------------------')
    # return render_template('home_company.html', current_user = a)
    resp = jsonify({"id" : id})
    return resp

@app.route("/login_page")
def login_page():
    return render_template('login_page.html')

if __name__ == "__main__":
    app.run(debug=True)