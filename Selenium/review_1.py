# Tech with Tim Tutorial #1 

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os 


# Chrome driver was saved in local usr folder and secutiry features were bypassed to allow for operation/reading on Mac 
os.environ['PATH'] += '/usr/local/bin/chromedriver'
driver = webdriver.Chrome()

driver.get('https://www.google.com/travel/flights')
print(driver.title)