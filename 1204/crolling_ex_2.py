from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import requests
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service = service)

driver.get("https://knitted.co.kr/")

search_bt = driver.find_element(By.CLASS_NAME, 'name')
print(search_bt.text)

"""search_bt = driver.find_element(By.XPATH, '//*[@id="main"]/header/div/div[2]/div/div[3]/ul/li[1]/img[1]')
search_bt.click()

time.sleep(2)

search_item = driver.find_element(By.XPATH, '//*[@id="keyword"]')
search_item.send_keys("팬츠")
search_item.send_keys(Keys.ENTER)

time.sleep(2)

item_name = driver.find_element(By.XPATH, '//*[@id="anchorBoxId_3970"]/div/div[2]/strong/a/span')
print(item_name[0])


time.sleep(2)"""
