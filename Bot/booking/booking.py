# Contains a Class with instance methods that we will call 
# responsible for describing methods that will be called and bot will take action 

import booking.constants as const
import os 
from selenium import webdriver
from booking.booking_filtration import BookingFiltration
from booking.booking_report import BookingReport
from prettytable import PrettyTable

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

        # FINDING ELEMENT THAT MATCHES GIVEN ARGUMENT 
        selected_currency_element = self.find_element_by_css_selector(
            f'a[data-modal-header-async-url-param*="selected_currency={currency}"]'
        )
        selected_currency_element.click()

    def enter_destination(self, destination=None):
        text_field = self.find_element_by_id('ss')
        # CLEAR TEXT FIELD BEFORE ENTERING TEXT 
        text_field.clear()
        text_field.send_keys(destination)

        first_result = self.find_element_by_css_selector (
            'li[data-i="0"]'
        )
        first_result.click()

    def enter_dates(self, check_in, check_out):
        check_in_date = self.find_element_by_css_selector(
            f'td[data-date="{check_in}"]'
        )
        check_in_date.click()

        check_out_date = self.find_element_by_css_selector(
            f'td[data-date="{check_out}"]'
        )
        check_out_date.click()

    def enter_adults(self, num_adults=None):
        selection_element = self.find_element_by_id('xp__guests__toggle')
        selection_element.click()

        # HOW TO RESET A COUNT 

        # When the number of adults reaches one, exit while loop (safety logic)
        while True:
            # Decrease Adult value to its minimum 
            decrease_button  = self.find_element_by_css_selector(
                'button[aria-label="Decrease number of Adults"]'
            )
            decrease_button.click()

            default_adult_value_element = self.find_element_by_id('group_adults')
            default_val = default_adult_value_element.get_attribute('value') # recieves a key name and returns value 

            if int(default_val) == 1:
                break

        
        increase_button  = self.find_element_by_css_selector(
            'button[aria-label="Increase number of Adults"]'
        )

        for _ in range(num_adults-1): #range starts at 0, default is 1 so we subtract 1 to bring it to range start value 
            increase_button.click()

    def search(self):
        search_button = self.find_element_by_css_selector(
            'button[type="submit"]'
        )
        search_button.click()

    def apply_filtrations(self):
        filtration = BookingFiltration(driver=self)
        filtration.apply_star_filter(4,5)
        filtration.sortby_lowest_price()

    def report_results(self):
        result_boxes = self.find_element_by_id(
            'search_results_table'
            )
        
        report = BookingReport(result_boxes)
        table = PrettyTable(
            field_names=['Hotel Name','Hotel Price', 'Hotel Rating']
        )
        table.add_rows(report.pull_titles())
        print(table)
        #print(report.pull_titles())
