# test page to search for elements needed 

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os 


# Chrome driver was saved in local usr folder and secutiry features were bypassed to allow for operation/reading on Mac 
os.environ['PATH'] += '/usr/local/bin/chromedriver'
driver = webdriver.Chrome()

driver.get('https://www.booking.com/searchresults.html?label=gen173nr-1FCAEoggI46AdIM1gEaLACiAEBmAExuAEHyAEM2AEB6AEB-AECiAIBqAIDuALTqriPBsACAdICJDVhNTVmYzZhLTk2MGYtNDBhOS1hYWJlLWNlMzU0Y2NiNmIxNNgCBeACAQ&sid=cc9c68546e5c6ba2d6db5e2a41803b5a&sb=1&sb_lp=1&src=index&src_elem=sb&error_url=https%3A%2F%2Fwww.booking.com%2Findex.html%3Flabel%3Dgen173nr-1FCAEoggI46AdIM1gEaLACiAEBmAExuAEHyAEM2AEB6AEB-AECiAIBqAIDuALTqriPBsACAdICJDVhNTVmYzZhLTk2MGYtNDBhOS1hYWJlLWNlMzU0Y2NiNmIxNNgCBeACAQ%3Bsid%3Dcc9c68546e5c6ba2d6db5e2a41803b5a%3Bsb_price_type%3Dtotal%26%3B&ss=Houston%2C+Texas%2C+United+States&is_ski_area=&checkin_year=2022&checkin_month=2&checkin_monthday=1&checkout_year=2022&checkout_month=2&checkout_monthday=10&group_adults=2&group_children=0&no_rooms=1&b_h4u_keep_filters=&from_sf=1&ss_raw=hou&ac_position=0&ac_langcode=en&ac_click_type=b&dest_id=20128761&dest_type=city&iata=HOU&place_id_lat=29.76&place_id_lon=-95.3625&search_pageview_id=63b114a9563001a5&search_selected=true&search_pageview_id=63b114a9563001a5&ac_suggestion_list_length=5&ac_suggestion_theme_list_length=0')

review_text = driver.find_element_by_css_selector(
    'div[data-testid="review-score"]'
)


print(review_text.text)