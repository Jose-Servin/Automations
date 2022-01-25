import os
from selenium import webdriver
from prettytable import PrettyTable
import DealSearch.variables as var

class Carmax(webdriver.Chrome):
    def __init__(self, driver_path='/usr/local/bin/chromedriver', teardown=False):
        self.teardown = teardown
        self.driver_path = driver_path
        os.environ['PATH'] += self.driver_path
        super(Carmax, self).__init__()
        self.implicitly_wait(15)

    def __exit__(self, exc_type, exc_value, exc_traceback): 
        if self.teardown:
            self.quit()

    def landing_page(self):
        self.get(var.BASE_URL)

    def current_store(self):
        current_location = self.find_element_by_id(
            'header-my-store-button-text'
            ).get_attribute('innerHTML').strip()
        print(f' Your default store is {current_location}')

    def search_store_button(self):
        store_button = self.find_element_by_id('header-my-store-button-text')
        store_button.click()

        see_inventory_button = self.find_element_by_class_name('header-footer-my-store-details-inventory-link')
        see_inventory_button.click()