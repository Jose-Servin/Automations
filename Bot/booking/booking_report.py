# generate report in terminal 
# methods in this file will parse the data needed from each result box
from selenium.webdriver.remote.webelement import WebElement


class BookingReport():
    def __init__(self, boxes_selection_element:WebElement):
        self.boxes_selection_element = boxes_selection_element
        self.deal_boxes = self.pull_deal_boxes()

    def pull_deal_boxes(self):
        return self.boxes_selection_element.find_elements_by_class_name('_5d6c618c8')

    def pull_titles(self):
        master_data = []

        for deal_box in self.deal_boxes:

            hotel_name = deal_box.find_element_by_css_selector(
                'div[data-testid="title"]'
            ).get_attribute('innerHTML').strip()
            
            hotel_price = deal_box.find_element_by_css_selector('.fde444d7ef._e885fdc12').get_attribute('innerHTML').strip()

            hotel_rating = deal_box.find_element_by_css_selector(
                'div[data-testid="review-score"]'
            ).get_attribute('innerHTML')

            master_data.append(
                [hotel_name, hotel_price, hotel_rating]
            )
        return master_data