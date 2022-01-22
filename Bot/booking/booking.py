# Contains a Class with instance methods that we will call 
# responsible for describing methods that will be called and bot will take action 

import booking.constants as const
import os 
from selenium import webdriver

# instance object will have methods from both selenium webdriver and any created by us. 
class Booking(webdriver.Chrome):
    def __init__(self, driver_path='/usr/local/bin/chromedriver'):
        self.driver_path = driver_path
        os.environ['PATH'] += self.driver_path #places driver path into system level PATH variable
        super(Booking, self).__init__() #instantiates an instance of the webdriver class as well 

    def land_first_page(self):
        self.get(const.BASE_URL)
