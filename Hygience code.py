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

## Code Snippet to get all yelp links
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

## Snippet to get Restaurant Info
data = []
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
        
# Snippet to get all the reviews and stats
## To run the function. We need to create empty lists first:
rest_names_list = []
rating_list = []
user_id_list = []
review_id_list = []
text_list = []
dates_list = []

def get_reviews_info(app_links):
    num1 = 0
    num2 = 0
    for app_link in app_links:
        num1 += 1
        print("Collecting info of the restaurant #{}".format(num1))
             # rest with most reviews have 436 pages
        url_base = 'http://www.yelp.com'
        url_base += app_link[:-26] + '?start=' + str(1)
        source_restaurant = requests.get(url_base)
        time.sleep(0.2 + 0.5 * random.randint(1, 30))
        restaurant = bs4.BeautifulSoup(source_restaurant.text, 'lxml')
       
        try:
            pages_no = restaurant.find('div',{'class':'page-of-pages arrange_unit arrange_unit--fill'}).text.strip()
        except:
            continue
        #### Restaurant Names
        rest_names = []
        try:
            try:
                rest_name = restaurant.find(('div', {'class': 'u-space-t1'}) and 'h1').text.strip()
                rest_names.append([rest_name]*int(restaurant.find('span',{'class': 'review-count rating-qualifier'}).text.strip()[:-7]))
            except:
                rest_name = restaurant.find('h1', {'class': 'biz-page-title embossed-text-white'}).text.strip()
                rest_names.append([rest_name]*int(restaurant.find('span',{'class': 'review-count rating-qualifier'}).text.strip()[:-7]))
        except:
            try:
                rest_names.append(['NIL']*int(restaurant.find('span',{'class': 'review-count rating-qualifier'}).text.strip()[:-7]))
            except:
                continue
                
        rest_names_list.append(rest_names)
        
        if len(pages_no) > 11:
            for j in range(int(pages_no[-3:])):
                url_base2 = 'http://www.yelp.com'
                url_base2 += app_link[:-26] + '?start=' + str(j*20)
                source_restaurant2 = requests.get(url_base2)
            
                num2 += 1
                print("Crawling info of #{} pages of the restaurant ".format(num2))                
                time.sleep(0.2 + 0.4 * random.randint(1, 35))
        
                reviews = bs4.BeautifulSoup(source_restaurant2.text, 'lxml')
            
                review_id = []          #All review ids
                for x in reviews.findAll('div', {'class': 'review review--with-sidebar'}):
                    try:
                        review_id.append(x['data-review-id'])
                    except:
                        review_id.append('NIL')
                text = []
                for x in reviews.findAll('p', {'lang': 'en'}): #All reviews text
                    try:
                        text.append(x.text.strip())
                    except:
                        text.append('NIL')
                dates = []
                for x in reviews.findAll('div',{'class': 'review-content'}):
                    try: 
                        a = x.find('span',{'class': 'rating-qualifier'})
                        dates.append(a.text.strip())
                    except:
                        dates.append('NIL')
                rating = []
                for x in reviews.findAll('div',{'class': 'review-content'}): #All Stars ratings
                    try: 
                        a= x.find('div',{'class': 'i-stars'})['title']
                        rating.append(a[0:3])  
                    except:
                        rating.append('NIL')
                user_id = []
                for x in reviews.findAll('li', {'class': 'user-name'}):   #All user names in one pages
                    try: 
                        user_id.append(x.text.strip())
                    except:
                        user_id.append('NIL')
                
                review_id_list.append(review_id)
                text_list.append(text)
                dates_list.append(dates)
                rating_list.append(rating)
                user_id_list.append(user_id)




    





