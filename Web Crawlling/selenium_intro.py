import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

import pyperclip
import pyautogui

browser = webdriver.Chrome()

browser.get('https://www.naver.com/')
elem = browser.find_element(By.CLASS_NAME, 'MyView-module__link_login___HpHMW')
elem.click()

browser.find_element(By.ID, 'id').send_keys('hl2amb')
browser.find_element(By.ID, 'pw').send_keys('Puteaux54##')
# id = browser.find_element(By.ID, 'id_line')
# id.click()
# pyperclip.copy('hl2amb')
# pyautogui.hotkey('ctrl', 'v')
#
# time.sleep(1)
#
# pwd = browser.find_element(By.ID, 'pw_line')
# pwd.click()
# pyperclip.copy('Puteaux54##')
# pyautogui.hotkey('ctrl', 'v')
time.sleep(1)

browser.find_element(By.ID, 'log.login').click()
time.sleep(10)




