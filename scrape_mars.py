
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

#chromedriver 
def init_browser():
    executable_path = {'executable_path': ChromeDriverManager().install()}

    return Browser("chrome", **executable_path, headless=False)



def scrape(): 
    #uncomment if on mac 
    #path = r"chromedriver.exe" 
    

    browser = init_browser()

    #find news title and news paragraph 
    url = "https://mars.nasa.gov/news/"
    browser.visit(url) 
    html = browser.html
    soup = bs(html, 'html.parser')
    news_title = soup.find('div', class_='bottom_gradient').text
    news_p = soup.find('div', class_='article_teaser_body').text
   

    #find URL of Space image 
    image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars" 
    browser.visit(image_url)
    browser.links.find_by_partial_text('FULL IMAGE').click()
    browser.links.find_by_partial_text('more info').click()
    html_photo = browser.html
    soup = bs(html_photo, 'html.parser')
    whole_page = soup.find('div', id="page")
    image = whole_page.find('figure', class_ = 'lede')
    image = image.find('img')['src']
    scrape_url = image_url+image


    #get the html of the table 
    facts = 'https://space-facts.com/mars/'
    tables = pd.read_html(facts)[0] 
    tables= tables.rename(columns = {0:'Parameter',1:'Value'})
    tables = tables.to_html(index = False)
   


    #get the hemisphere URLs 
    hemispheres_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(hemispheres_url)
    html_hemispheres = browser.html

    soup = bs(html_hemispheres, 'html.parser')

    items = soup.find_all('div', class_='item')

    hemisphere_image_urls = []

    hemispheres_main_url = 'https://astrogeology.usgs.gov'

    for item in items: 
   
        title = item.find('h3').text
    
        image_url = item.find('a', class_='itemLink product-item')['href']

        browser.visit(hemispheres_main_url + image_url)

        image_html = browser.html

        soup = bs( image_html, 'html.parser')
        image_url = hemispheres_main_url + soup.find('img', class_='wide-image')['src']

        hemisphere_image_urls.append({"Title" : title, "Image_URL" : image_url})

    scrape_hemisphere = hemisphere_image_urls

    #save everything in a dictionary 
    mars_dict = {'news_title': news_title,
                 'news_p': news_p,
                 'featured_image_url': scrape_url,
                 'mars_facts': tables,
                 'hemisphere_image_urls': scrape_hemisphere}

    browser.quit()
    
    return mars_dict





