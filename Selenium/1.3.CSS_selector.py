import os 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 

# Chrome driver was saved in local usr folder and secutiry features were bypassed to allow for operation/reading on Mac 
os.environ['PATH'] += '/usr/local/bin/chromedriver'
driver = webdriver.Chrome()

# Project Scope: we will be sending two numeric values to specified website and clicking button to perform calculation 
driver.get('https://www.marshu.com/articles/calculate-addition-calculator-add-two-numbers.php')
driver.implicitly_wait(5)

# Pop up window appears
try: 
    no_button = driver.find_element_by_class('class')
    no_button.click()
except:
    print('No pop up window appeared. Skipping.....')

# Find elements on webpage 
number1 = driver.find_element_by_name('n01')
number2 = driver.find_element_by_name('n02')

# Send key with respective element 
number1.send_keys(Keys.NUMPAD1, Keys.NUMPAD6)
number2.send_keys(14)

# CSS Selector: A pattern to filter an element by its styling 
#btn = driver.find_element_by_css_selector('button[onclick="findcalculatorcalculate(this.form)"]')
btn = driver.find_element_by_xpath('/html/body/table/tbody/tr/td[1]/table[2]/tbody/tr[1]/td[2]/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/form/p[4]/input')
btn.click()
