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
from translate import Translator
import pyautogui as pg
from selenium.webdriver.support import expected_conditions as EC

#create rotating proxies
proxydict = {}
homeurl = input("enter the url for the product:  ")

'''page= requests.get(url=homeurl)
pageresult = homeurl.'''
time.sleep(1)

pathtowebdriver= ('C:\\Users\\konch\\OneDrive\\Desktop\\chromedriver.exe')
driver = webdriver.Chrome(pathtowebdriver)
driver.get(url=homeurl)
curl=requests.get(driver.current_url)

soup = BeautifulSoup(curl.content,"lxml")

print(soup)

#get data out of the bullshit and into the csv

#change proxy




