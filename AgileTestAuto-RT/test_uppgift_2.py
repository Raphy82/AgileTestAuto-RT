import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
#from uppgift_2 import Netonnet



'# check first product added to basket'
'# check right price is added to basket for first product'
'# add second product added to basket'
'# check right price is added to basket for first product'
'# check total price in basket'
'# check discount calculated'
'# check we go to checkout with all correct information'
'# driver.implicitly_wait(10)'

@pytest.mark.usefixtures("setup")
class TestNetonnet:
    def test_artikel(self):
        elem = self.driver.find_element(By.XPATH, "//input[@placeholder='Sök produkter, guider och mer...']")
        elem.send_keys("1004014")
        elem.send_keys(Keys.ENTER)
        artikel = self.driver.find_element(By.XPATH, "//div[@class='subTitle big']")
        artikel = artikel.text
        print(artikel)
        assert "1004014" in artikel

#assert stop.text == "1"
