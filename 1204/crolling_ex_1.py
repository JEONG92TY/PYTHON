from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import requests
import time
'''
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service = service)

driver.get("https://github.com/login")

search_id = driver.find_element(By.XPATH, '//*[@id="login_field"]')
search_pw = driver.find_element(By.XPATH, '//*[@id="password"]')

search_id.send_keys("xoduddlrn@gmail.com")
search_pw.send_keys("Wjdxodud1@")
search_pw.send_keys(Keys.ENTER)

search_bt = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/header/div/div[2]/div[3]/deferred-side-panel/include-fragment/react-partial-anchor/button/span/span/img')
search_bt.click()

search_fp = driver.find_element(By.XPATH, '//*[@id=":rf:--label"]')
search_fp.click()
'''
find_profile = "https://github.com/JEONG92TY"
res = requests.get(find_profile)
soup = BeautifulSoup(res.text, "html.parser")

profile = soup.select("span.p-nickname")

f = [i.text.strip() for i in profile]
print(f"사용자 이름 = {f}")

time.sleep(2)