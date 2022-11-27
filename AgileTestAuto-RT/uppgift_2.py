from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
'#Open Netonnet website in chrome'
driver.get("https://www.netonnet.se")
driver.fullscreen_window()
'#Accept cookies'
driver.find_element(By.XPATH, "//*[@id='cookiebannerShowSettingsButton']/div/div[1]/button").click()
time.sleep(2)
'#Search for product = 1004014'
elem = driver.find_element(By.XPATH, "//input[@placeholder='Sök produkter, guider och mer...']")
elem.send_keys("1004014")
elem.send_keys(Keys.ENTER)
#assert elem == ""
time.sleep(2)
'#Add item 1004014 to checkout'
elem = driver.find_element(By.ID, "BuyButton_ProductPageStandard_1004014")
elem.send_keys(Keys.ENTER)
time.sleep(4)

#cart_menu = driver.find_element(By.XPATH, "//div[@id='dialogAccordion']")
#cart_menu = driver.find_element(By.XPATH, "//div[@id='cartModal']")
cart_menu = driver.find_element(By.XPATH, "//div[@id='cartCollapse']//div[@class='modal-header']")
#x_button = driver.find_element(By.XPATH, "//span[@class='closeModalIcon pull-right']")
achains = ActionChains(driver)
achains.move_to_element(cart_menu).perform()
#ActionChains(driver).move_to_element(cart_menu).click().perform()
#driver.find_element(By.XPATH, "//div[@id='dialogAccordion']")
#driver.switch_to.frame("//div[@id='cartCollapse']")
driver.find_element(By.XPATH, "//span[@class='closeModalIcon pull-right']").click()
time.sleep(2)
driver.close()
