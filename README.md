
you will need to install the Selenium Python library and place a ChromeDriver executable on your path.

You will also need to have Chrome installed.

It may also work with Chromium but we have not tested this.

Selenium can be installed using pip using the command 'pip install selenium'.


pip install beautifulsoup4
pip3 install beautifulsoup4

pip install selenium
pip3 install selenium

pip install webdriver-manager
pip3 install webdriver-manager

pip install undetected-chromedriver
pip3 install undetected-chromedriver

from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())

# REF

###
https://github.com/amirbehzad/grocery-prices