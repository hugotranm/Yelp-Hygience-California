# Yelp-Hygience-California
Initially by my professor from UC Irvine, this is a project following step-by-step approach to analyzing restaurant data from Yelp

1. What questions need to be answered. In this case: Hygience issue
2. What types of data available
3. Choose Attributes and Parameters to research
4. Tools pick. In this case: Python - BeautifulSoup, Request module
5. Model the database
6. Design data pipeline
7. Extract data from Yelp

The code here reflects step 7: the extracting step. Let's start!

# Three functions will be used in my framework:
- First one to crawl all the links into list named "app_links"
- Second, feed "app_links" into the get_info function to get all the restaurants info
- Third, feed "app_links" into the get_reviews_info function to get all the text data.

