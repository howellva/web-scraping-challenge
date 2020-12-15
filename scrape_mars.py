
#pip3 install flask
from flask import Flask, render_template

# Import our pymon#go library, which lets us connect our Flask app to our Mongo database.
import pymongo

from splinter import Browser  
from bs4 import BeautifulSoup as bs 
import requests  
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd 
import time 

mars = {}

def scrape(): 
    #path = r'C:\Users\vhowell\Downloads\chromedriver_win32 (2)\\chromedriver.exe'
    #path = r'/Users/vanessahowell/Desktop/chromedriver.exe' 
    path = r'/usr/local/bin/chromedriver.exe'

    browser = Browser('chrome', executable_path = path, headless = False)
    url = "https://mars.nasa.gov/news/"
    browser.visit(url) 
    html = browser.html
    soup = bs(html, 'html.parser')
    news_title = soup.find('div', class_='bottom_gradient').text
    news_p = soup.find('div', class_='article_teaser_body').text

    mars['news title'] = news_title
    mars['news paragraph'] = news_p 
    scrape_mars = mars 
    return mars  



