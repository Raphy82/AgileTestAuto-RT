import pytest
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

        self.driver.find_element(By.XPATH, "//div[@id='add_to_cart_page.recs_1']//a[@class='btn btn-outline-primary btn-block-xs'][normalize-space()='Fortsätt handla']").click()
        time.sleep(2)
