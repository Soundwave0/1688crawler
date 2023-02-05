
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



homeurl='https://1688.com/'
'''
homepage= requests.get(url=homeurl)
homeresult = BeautifulSoup(homepage.content, 'html.parser')
'''

'''
translator= Translator(to_lang="zh")
translation = translator.translate("This is a pen.")
'''

#selenium webdriver using
ckw = ["电子产品"]
pathtowebdriver= ('C:\\Users\\konch\\OneDrive\\Desktop\\chromedriver.exe')
driver = webdriver.Chrome(pathtowebdriver)
driver.get(url=homeurl)

#print(driver.current_url) driver current url getter
original_window = driver.current_window_handle
time.sleep(0.2)
elem = driver.find_element(By.ID, "home-header-searchbox")
elem.clear()
elem.send_keys(ckw)
elem.send_keys(Keys.RETURN)
time.sleep(5)
for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break

pageaftersearch = requests.get(driver.current_url)
print(driver.current_url)
soup = BeautifulSoup(pageaftersearch.content,"lxml")
productlist = soup.find_all('div',class_='mojar-element-image')
productlinks = []
print(productlist)

'''
first = productlist[0]
link=first.find_a('a',href=True)
print(link['href'])
'''
'''
for item in productlist:
    for link in item.find_a('a',href=True):
        print(link['href'])
'''
#You need to shange region to shanxi will be done later




#navigate to products and get information

#write into excel

#add appropiate code to product

