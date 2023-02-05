
#import statements
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
'''
#go to 1668 website
homeurl = 'https://www.1688.com/'
homepage= requests.get(url=homeurl)
homeresult = BeautifulSoup(homepage.content, 'html.parser')
print(homeresult)'''

#selenium webdriver using

pathtowebdriver= Service('C:\\Users\\konch\\OneDrive\\Desktop\\chromedriver.exe')
driver = webdriver.Chrome(service=pathtowebdriver)
driver.get("https://google.com")
time.sleep(1000)




#navigate to products and get information

#write into excel

#add appropiate code to product

