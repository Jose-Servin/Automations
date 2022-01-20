import os 
from selenium import webdriver

# Chrome driver was saved in local usr folder and secutiry features were bypassed to allow for operation/reading on Mac 
os.environ['PATH'] += '/usr/local/bin/chromedriver'
driver = webdriver.Chrome()

# Project Scope: we will be sending two numeric values to specified website and clicking button to perform calculation 
driver.get('https://compendiumdev.co.uk/selenium/testpages/calculate.php')