'''
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.naver.com/")
print(driver.title)
driver.quit()
'''

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

options = Options()
#options.add_argument("--start-maximized")
options.add_argument("--headless")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service = service, options = options)
#driver.maximize_window()

driver.get("https://www.google.co.kr/")
print(driver.current_url)
#driver.execute_script("window.scrollTo(0, document.by.scrollHeight)")
#driver.implicitly_wait(5)


search_input = driver.find_element(By.XPATH, '//*[@id="APjFqb"]')
print(search_input)

search_input.send_keys("파이썬 코딩연습")
time.sleep(2)
search_input.clear()


email_text = driver.find_element(By.XPATH, '//*[@id="gb"]/div/div[1]/div/div[1]/a')
href = email_text.get_attribute("href")
print(href)
'''

search_input = driver.find_element(By.XPATH, '//*[@id="APjFqb"]')
print(search_input)

search_input.send_keys("파이썬 코딩연습")
search_input.send_keys(Keys.ENTER)

driver.save_screenshot("./1204/save.png")
'''