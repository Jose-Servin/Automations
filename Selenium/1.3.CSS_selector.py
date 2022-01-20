import os 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 

# Chrome driver was saved in local usr folder and secutiry features were bypassed to allow for operation/reading on Mac 
os.environ['PATH'] += '/usr/local/bin/chromedriver'
driver = webdriver.Chrome()

# Project Scope: we will be sending two numeric values to specified website and clicking button to perform calculation 
driver.get('https://compendiumdev.co.uk/selenium/testpages/calculate.php')
driver.implicitly_wait(5)

# Pop up window appears
try: 
    no_button = driver.find_element_by_class('class')
    no_button.click()
except:
    print('No pop up window appeared. Skipping.....')

# Find elements on webpage 
number1 = driver.find_element_by_id('number1')
number2 = driver.find_element_by_id('number2')

# Send key with respective element 
number1.send_keys(Keys.NUMPAD1, Keys.NUMPAD6)
number2.send_keys(14)

# CSS Selector 