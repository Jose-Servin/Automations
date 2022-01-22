# Contains a Class with instance methods that we will call 
# responsible for describing methods that will be called and bot will take action 

import booking.constants as const
import os 
from selenium import webdriver

# instance object will have methods from both selenium webdriver and any created by us. 
class Booking(webdriver.Chrome):
    def __init__(self, driver_path='/usr/local/bin/chromedriver', teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown #used to control when brower exit function executes. Given to Booking ()
        os.environ['PATH'] += self.driver_path #places driver path into system level PATH variable
        super(Booking, self).__init__() #instantiates an instance of the webdriver class as well 
        self.implicitly_wait(15) # used to give browser time to load up and find elements
        #self.maximize_window() # used for visualization purposes 

    # method reponsible for exitting browser 
    # python automatically runs this dunder method once code exits with indentation block
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)

    def change_currency(self, currency=None):
        currency_element = self.find_element_by_css_selector(
            'button[data-tooltip-text="Choose your currency"]'
        )
        currency_element.click()

        selected_currency_element = self.find_element_by_css_selector(
            f'a[data-modal-header-async-url-param*="selected_currency={currency}"]'
        )
        selected_currency_element.click()

    def enter_destination(self, destination=None):
        text_field = self.find_element_by_id('ss')
        text_field.clear()
        text_field.send_keys(destination)

        first_result = self.find_element_by_css_selector (
            'li[data-i="0"]'
        )
        first_result.click()