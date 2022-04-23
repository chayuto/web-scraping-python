import time
# Web scraping library
from selenium import webdriver
from bs4 import BeautifulSoup

base_url = 'https://www.chemistwarehouse.com.au/shop-online/587/swisse'

from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())

browser = driver
browser.get(base_url)

has_next_page = True
while has_next_page:
    
    soup = BeautifulSoup(driver.page_source, "html.parser")
    items = soup.find_all(class_="product")
    
    for item in items:
        #item.find(class_="product__title")
        print(item.find(class_="product__title").text)
        print(item.find(class_="product__price-current").text)
        
    next_button = None
    try:
        next_button = driver.find_element_by_xpath("//button[contains(text(),'Next')]")
        has_next_page = True
    except:
        has_next_page = False
        pass
    
    if has_next_page:
        next_button.click()
        time.sleep(3)
    