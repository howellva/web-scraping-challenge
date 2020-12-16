from flask import Flask, jsonify, render_template, redirect 
import pymongo 
from flask_pymongo import PyMongo  
import os 
import scrape_mars 


app = Flask(__name__) 
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)  


#home page 
@app.route('/')
def home():  
    mars = mongo.db.mars.find_one() 
    return render_template('index.html', mars = mars) 

#scrape the data
@app.route("/scrape") 
def scrape(): 
    mars = mongo.db.mars 
    mars_data = scrape_mars.scrape() 
    mars.update({}, mars_data, upsert = True) 
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)

