import os
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Chrome driver was saved in local usr folder and secutiry features were bypassed to allow for operation/reading on Mac 
os.environ['PATH'] += '/usr/local/bin/chromedriver'
driver = webdriver.Chrome()

# direct driver to website 
driver.get('https://jqueryui.com/resources/demos/progressbar/download.html')
# waiting defined x seconds to wait for page to load (3 seconds represents the upper bound of our defined wait time)
driver.implicitly_wait(3)

# direct Selenium to click on the element with download button ID 
download_button = driver.find_element_by_id('downloadButton') # returns an object that can be further manipulated
# perform action with element gathered from page
download_button.click() 

#### These two lines were commented out and the WebDriverWait class was initialized below 
#progress_element = driver.find_element_by_class_name('progress-label')
#print(f"{progress_element.text == 'Completed!'}")

WebDriverWait(driver, 30).until(
    EC.text_to_be_present_in_element( 
        (By.CLASS_NAME, 'progress-label'), # element filtration ( this is another way to find an element in a webpage ), 
        'Complete!' # the expected text
    )
)