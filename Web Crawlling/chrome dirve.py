import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Specify the path to chromedriver using the Service class
s= Service(executable_path='/Users/sungyounglee/Documents/')
# s = Service('/Users/sungyounglee/Documents/')
browser = webdriver.Chrome(service=s)

