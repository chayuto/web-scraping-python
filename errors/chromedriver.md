Error message: "'chromedriver' executable needs to be available in the path"

pip install webdriver-manager

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

==============================


driver = webdriver.Chrome('/path/to/chromedriver') 




FeatureNotFound: Couldn't find a tree builder with the features you requested: lxml. Do you need to install a parser library?



pip install lxml

import lxml

NoSuchElementException 

NameError: name 'time' is not defined

import time