import json
import os
from flask import Flask, redirect, url_for, render_template, request, jsonify
from datetime import datetime
import pymongo
import pprint
from bson.objectid import ObjectId
from cls_obj.company import Company
from werkzeug.utils import  secure_filename
from init_database_mongo import InitDatabaseMongoDB

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

@app.route("/home_company")
def home_company(company):
    pprint.pprint(company)
    return render_template('home_company.html')

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
    a = company[0]
    print('------------------------------------------')
    # return render_template('home_company.html', current_user = a)
    return home_company(a)

@app.route("/login_page")
def login_page():
    return render_template('login_page.html')

if __name__ == "__main__":
    app.run(debug=True)