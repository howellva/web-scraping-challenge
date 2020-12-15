from flask import Flask, jsonify, render_template, redirect 
from scrape_mars import scrape 
import pymongo 
from flask_pymongo import PyMongo  
import os 
import scrape_mars 
#from scrape_mars import mars 

app = Flask(__name__) 
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)  

print(mars)

# @app.route('/')
# def home():  
#     mars = mongo.db.mars.find_one() 
#     return render_template('index.html', mars = mars) 
# @app.route("/scrape") 
# def scrape(): 
#     mars = mongo.db.mars 
#     mars_data = scrape_mars.scrape_all() 
#     mars.update({}, mars_update, upsert = True) 
#     return "succesful"

# if __name__ == "__main__":
#     app.run(debug=True)

