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

import secret#file containing login information

homeurl='https://i.taobao.com/my_taobao.htm?spm=a2141.241046-cn.754894437.3.c9006f11T8S8JU&ad_id=&am_id=&cm_id=&pm_id=1501036000a02c5c3739'
taobaousername=secret.taobaousername
taobaopass=secret.taobaopass


ckw = ["小工具"]
pathtowebdriver= ('C:\\Users\\konch\\OneDrive\\Desktop\\chromedriver.exe')
driver = webdriver.Chrome(pathtowebdriver)
driver.get(url=homeurl)
driver.maximize_window()
time.sleep(1)
#pass verification
loginelem=driver.find_element_by_name('fm-login-id')
loginelem.send_keys(taobaousername)
passelem=driver.find_element_by_id('fm-login-password')
passelem.send_keys(taobaopass)
#issue with the sliding captcha bullshit

