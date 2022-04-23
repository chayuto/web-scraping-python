from bs4 import BeautifulSoup
import requests

# HTML From Website
url = "https://www.chemistwarehouse.com.au/buy/76017/swisse-vitamin-c-1000mg-150-tablets"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")