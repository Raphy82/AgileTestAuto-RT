from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
'#open ellos website in chrome'
driver.get("https://www.netonnet.se")
driver.fullscreen_window()
'#Search for product = 1004014'
elem = driver.find_element(By.XPATH, "//input[@placeholder='Sök produkter, guider och mer...']")
elem.send_keys("1004014")
elem.send_keys(Keys.ENTER)
time.sleep(4)
'#Add item 1004014 to checkout'
elem = driver.find_element(By.ID, "BuyButton_ProductPageStandard_1004014")
elem.send_keys(Keys.ENTER)
time.sleep(4)
driver.close()
