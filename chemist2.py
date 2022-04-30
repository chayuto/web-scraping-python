import time
import requests
import re
# Web scraping library
from selenium import webdriver
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager

urls = [
'https://www.chemistwarehouse.com.au/shop-online/587/swisse',
'https://www.chemistwarehouse.com.au/shop-online/850/garnier-fructis',
'https://www.chemistwarehouse.com.au/shop-online/5571/john-frieda-haircare',
'https://www.chemistwarehouse.com.au/shop-online/2367/vicks-cold-flu',
'https://www.chemistwarehouse.com.au/shop-online/2104/vicks-vapodrops',
'https://www.chemistwarehouse.com.au/shop-online/5286/clairol-natural-instincts',
'https://www.chemistwarehouse.com.au/shop-online/2203/nivea-body',
'https://www.chemistwarehouse.com.au/shop-online/2368/voost',
'https://www.chemistwarehouse.com.au/shop-online/4458/duit-foot-care',
'https://www.chemistwarehouse.com.au/shop-online/4717/duit-hand-cream',
]


driver = webdriver.Chrome(ChromeDriverManager().install())

for base_url in urls:
    driver.get(base_url)

    has_next_page = True
    while has_next_page:
        
        soup = BeautifulSoup(driver.page_source, "html.parser")
        items = soup.find_all(class_="product")
        
        for item in items:
            #item.find(class_="product__title")
            print(item.find(class_="product__title").text)
            print(item.find(class_="product__price-current").text)
            product_name = item.find(class_="product__title").text
            price_str = item.find(class_="product__price-current").text
            image_url = item.find(class_="product__image-main")['src']

            number_strs = re.findall("\d+\.\d+", price_str)
            price = float(number_strs[0])

            # # Sync
            payload = {
                "product_name": product_name,
                "supplier_name": "ChemistWarehouse",
                "price": price,
                "image_url": image_url
                }
            url = "http://localhost:3000/api/products/market_data"
            response = requests.post(url, json= payload)


            
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
    time.sleep(1)
    