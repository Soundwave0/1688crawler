
#import statements
import requests
import selenium
from bs4 import BeautifulSoup
#go to 1668 website
homeurl = 'https://www.1688.com/'
homepage= requests.get(url=homeurl)
homeresult = BeautifulSoup(homepage.content, 'html.parser')
print(homeresult)




#navigate to products and get information

#write into excel

#add appropiate code to product

