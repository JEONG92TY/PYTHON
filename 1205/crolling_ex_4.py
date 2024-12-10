from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import requests
import time, os

list = []

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service = service)

driver.get("https://www.google.com/")

search = driver.find_element(By.XPATH, '//*[@id="APjFqb"]')
search.send_keys("바위너구리")
search.send_keys(Keys.ENTER)

button = driver.find_element(By.XPATH, '//*[@id="hdtb-sc"]/div/div/div[1]/div/div[2]/a/div').click()

time.sleep(2)

for i in range(3) :
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

images = driver.find_elements(By.CSS_SELECTOR, 'img.YQ4gaf')
os.makedirs("./1205/images", exist_ok = True)

time.sleep(2)

code = 1

for image in images :
    src = image.get_attribute("src")
    if "https" in src :
        res = requests.get(src)
        #print(res.content)
        with open(f"./1205/images/img_{code}.png", "wb") as file:
            file.write(res.content)
        code += 1

time.sleep(2)
