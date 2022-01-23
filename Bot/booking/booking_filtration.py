# File includes a Class with Instance methods that will filter results after arriving at landing page. 
from selenium.webdriver.remote.webdriver import WebDriver

class BookingFiltration:
    def __init__(self, driver:WebDriver):
        self.driver = driver

    def apply_star_filter(self, star_rating):
        star_filtration_box = self.driver.find_element_by_css_selector(
            'div[data-filters-group="class"]'
        )
        star_child_elements = star_filtration_box.find_elements_by_css_selector('*')
        for star_element in star_child_elements:
            if str(star_element.get_attribute('innerHTML')).strip() == f'{star_rating} stars':
                star_element.click()
