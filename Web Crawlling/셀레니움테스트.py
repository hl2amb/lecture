import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Specify the path to chromedriver using the Service class
s = Service('/Users/m2/Documents/chromedriver')
browser = webdriver.Chrome(service=s)

# # browser = webdriver.Chrome(executable_path='/Users/m2/Documents/chromedriver')
# # browser = webdriver.Chrome('/Users/sungyounglee/Documents/chromedriver')
# browser.get('https://www.google.com')
