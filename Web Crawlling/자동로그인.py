
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import pyperclip
import pyautogui

url ='https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/'
browser = webdriver.Chrome()
browser.get(url)
browser.implicitly_wait(10)

# browser.find_element(By.ID, 'id').send_keys('hl2amb')
# browser.find_element(By.ID, 'pw').send_keys('Puteaux54##')
id = browser.find_element(By.CSS_SELECTOR, '#id')
id.click()
pyperclip.copy('hl2amb')
id.send_keys(Keys.COMMAND, 'v')
# pyautogui.hotkey('command','v')
# id.send_keys('hl2amb')

pwd = browser.find_element(By.CSS_SELECTOR, '#pw')
pwd.click()
pyperclip.copy('Puteaux54##')
pwd.send_keys(Keys.COMMAND, 'v')
# pyautogui.hotkey('command', 'v')
# pwd.send_keys('Puteaux54##')

login_button = browser.find_element(By.CSS_SELECTOR, '#log\.login')
# login_button.click()
time.sleep(10)