# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 18:54:32 2018

@author: Tran Pro
"""

from IPython.display import HTML
from IPython.display import Image
import numpy as np
import requests
import bs4 
import time
import operator
import socket
import re # regular expressions
import random

from pandas import Series
import pandas as pd
from pandas import DataFrame

import matplotlib
import matplotlib.pyplot as plt
#%matplotlib inline

import seaborn as sns
sns.set_context("talk")
sns.set_style("white")

import csv
import numpy as np
import pandas as pd

import matplotlib
import matplotlib.pyplot as plt

## Code Snippet to get 100 resume links
def get_app_links():
    app_links = []
    for i in range(2): #do range(num_pages) if you want them all, here we just need two pages as each page displays 50 resumes
        url = 'https://www.yelp.com/search?find_desc=Restaurants&find_loc=San+Francisco,+CA&start=' + str(i*10) #base url + appending the url of each page
        source = requests.get(url) #reads the data from this url using urllib library
    
        yelp = bs4.BeautifulSoup(source.text, 'html.parser') # Get the HTML code of the Page
  
    # FIND ALL RESUMES
    
        for link in yelp.findAll('a', {'class': 'biz-name js-analytics-click'}):
            try:
                app_links.append(link['href'])
    
    
            except KeyError:
                pass
    
    print("Total number of resume links scraped: {}".format(len(app_links)))
    return app_links

app_links = get_app_links()    
data_yelp = []

url_base = 'https://www.yelp.com/biz/fog-harbor-fish-house-san-francisco-2?frvs=True&osq=Restaurants'
source_restaurant = requests.get(url_base, timeout = 5)
restaurant = bs4.BeautifulSoup(source_restaurant.text, 'lxml')
details = []
details.append(restaurant.find('h1', {'class': 'biz-page-title embossed-text-white'}).text.strip()) # Append name
details.append(restaurant.find('span',{'class': 'neighborhood-str-list'}).string.strip()) #Append Price $$
details.append(restaurant.find('strong', {'class': 'street-address'}).text.strip()) #Append Price $$
details.append(restaurant.find('div',{'class': 'i-stars'})['title']) #Append Stars Rating
details.append(restaurant.find('span',{'class': 'review-count rating-qualifier'}).string[13:17]) #Append Stars Rating
details.append(restaurant.find('span',{'class': 'business-attribute price-range'}).string) #Append Price $$
details.append(restaurant.find('dd',{'class': 'nowrap price-description'}).string.strip()) #Append Price $$
details.append(restaurant.find('span',{'class': 'category-str-list'}).text.strip()) #Append Price $$
details.append(restaurant.find('div',{'class': 'score-block'}).string.strip()) #Append Stars Rating
details.append(restaurant.find('dt',{'class': 'attribute-key'}).text.strip()) #Append Stars Rating
print(details)
restaurant.find('div',{'class': 'short-def-list'},)

<span class="category-str-list">
                    <a href="/c/sf/vietnamese">Vietnamese</a>,
                    <a href="/c/sf/sandwiches">Sandwiches</a>
    </span>



restaurant.find('div',{'class': 'i-stars'})['title']
restaurant.find('h1', {'class': 'biz-page-title embossed-text-white'}).text.strip()
<span class="review-count rating-qualifier">
            3838 reviews
    </span>
def get_info(app_links):
    num = 0
    for app_link in app_links:
        num += 1
        print("Collecting information for restaurant #{}".format(num))
        details = []
        url_base = 'http://www.yelp.com'
        url_base += app_link
        source_restaurant = requests.get(url_base)
        
        time.sleep(0.5 + 0.1 * random.randint(0, 25))
        
        restaurant = bs4.BeautifulSoup(source_restaurant.text)
        
    #GET NAME AND WORK DETAILS
    
        try:
            details.append(restaurant.find('h1', {'class': 'biz-page-title embossed-text-white shortenough'}).string) # Append name
        except:
            details.append('NIL')
        try:
            details.append(restaurant.find('div',{'class'}: 'i-stars i-stars--large-4-half rating-very-large'}).title) #Append Stars Rating
        except:
            details.append('NIL')
        try:
            details.append(restaurant.find('div',{'class'}: 'i-stars i-stars--large-4-half rating-very-large'}).title) #Append Stars Rating
        except:
            details.append('NIL')
        work_exps = restaurant.findAll('div', {'class': 'work-experience-section'})[:5]
        if len(work_exps) != 0:
            for exps in work_exps:
                try:
                    work_title = exps.find('p',{'class': 'work_title title'}).string
                except:
                    work_title = 'NIL'
                try:
                    work_company = exps.find('span',{'class':'bold'}).string
                except:
                    work_company = 'NIL'
                try:
                    work_date = exps.find('p',{'class': 'work_dates'}).string
                except:
                    work_date = 'NIL'
                details.append(work_title)
                details.append(work_company)    
                details.append(work_date)
        else:
            details.append('NIL')
    
    #GET EDUCATION
    
        education = candidate.findAll('div', {'class': 'section-item education-content'})[:2]
        if len(education) != 0:
            for ed in education:
                try:
                    edu_title = ed.find('p',{'class': 'edu_title'}).string
                except:
                    edu_title = 'NIL'
                try:
                    edu_school = ed.find('div',{'class':'edu_school'}).string
                except:
                    edu_school = 'NIL'
    
                details.append(edu_title)
                details.append(edu_school)
    
        else:
            details.append('NIL')
        data.append(details)
        print("Finished collecting information for resume #{}".format(num))
        

    





