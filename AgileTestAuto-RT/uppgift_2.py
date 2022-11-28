import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


@pytest.mark.usefixtures("setup")
class Netonnet:
    def __init__(self, driver):
        self.driver = driver

    '#Search for any product = skus'
    def findproduct(self, skus):
        sku = self.driver.find_element(By.XPATH, "//input[@placeholder='Sök produkter, guider och mer...']")
        sku.send_keys(skus)
        sku.send_keys(Keys.ENTER)
        time.sleep(2)

    '#Add item to basket'
    def additem(self):
        item = self.driver.find_element(By.XPATH, "//button[@id='BuyButton_ProductPageStandard_1004014']")
        item.send_keys(Keys.ENTER)
        time.sleep(2)

        #iframe = self.driver.find_element(By.XPATH, "//div[@id='insuranceModal']//div[@class='modal-dialog modal-lg']")
        #self.driver.switch_to.frame(iframe)
        #self.driver.find_element(By.XPATH, "//div[@id='insuranceModal']//span[@class='closeModalIcon pull-right']").click()

        #driver.switch_to.frame("//div[@id='cartCollapse']")
        #driver.find_element(By.XPATH, "//span[@class='closeModalIcon pull-right']").click()

        #cart_menu = driver.find_element(By.XPATH, "//div[@id='dialogAccordion']")
        #cart_menu = driver.find_element(By.XPATH, "//div[@id='cartModal']")
        #cart_menu = driver.find_element(By.XPATH, "//div[@id='cartCollapse']//div[@class='modal-header']")
        #cart_menu = driver.find_element(By.XPATH, "//span[@class='closeModalIcon pull-right']")
        #achains = ActionChains(driver)
        #achains.move_to_element(cart_menu).perform()
        #ActionChains(driver).move_to_element(cart_menu).click().perform()

        #Alert(driver).dismiss()

        #time.sleep(2)
