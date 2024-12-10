from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service = service)

driver.get("https://www.agoda.com/")

search_country = driver.find_element(By.XPATH, '//*[@id="textInput"]')
search_country.send_keys("충칭")
time.sleep(3)

search_country_button = driver.find_element(By.XPATH, '//*[@id="property-suggestion-icon-container-10084"]/span/i')
search_country_button.click()
time.sleep(2)

search_from = driver.find_element(By.XPATH, '//*[@id="DatePicker__Accessible"]/div/div[2]/div[1]/div[3]/div[5]/div[2]/div/div/div/span')
search_from.click()
time.sleep(2)

search_to = driver.find_element(By.XPATH, '//*[@id="DatePicker__Accessible"]/div/div[2]/div[1]/div[3]/div[5]/div[6]/div/div/div/span')
search_to.click()
time.sleep(2)

search_search_button = driver.find_element(By.XPATH, '//*[@id="Tabs-Container"]/button')
search_search_button.click()
time.sleep(5)

driver.switch_to.window(driver.window_handles[-1])

search_hotel_name = driver.find_elements(By.CLASS_NAME, 'dynamic-style-typographystyle-13 sc-kstrdz btjemE ae7b2-no-underline ae7b2-ae7b2-box ae7b2-inline-flex ae7b2-m-none')
#search_hotel_name = driver.find_elements(By.CSS_SELECTOR, '.hotel-list-container h3')
#search_hotel_price = driver.find_element(By.XPATH, '//*[@id="contentContainer"]/div[4]/ol[1]/li[1]/div/div/div/div/div[3]/div/div[2]/aside/ul/li/div/span[3]')
time.sleep(2)

print(search_hotel_name)

time.sleep(5)

