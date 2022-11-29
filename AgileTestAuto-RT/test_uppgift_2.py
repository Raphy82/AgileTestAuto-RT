import pytest
from selenium.webdriver.common.by import By
from uppgift_2 import Netonnet


@pytest.mark.usefixtures("setup")
class TestNetonnet:
    def test_artikel(self):
        artikel1 = Netonnet(self.driver)
        artikel1.findproduct("1004014")
        artikel = self.driver.find_element(By.XPATH, "//div[@class='subTitle big']")
        artikel = artikel.text
        print(artikel)
        assert "1004014" in artikel

    def test_namn(self):
        namn = self.driver.find_element(By.XPATH, "//h2[normalize-space()='Testvinnande powerbank med många laddmöjligheter']")
        namn = namn.text
        print(namn)
        assert "powerbank" in namn

    def test_pris(self):
        pris = self.driver.find_element(By.XPATH, "//div[@class='price-big']")
        pris = pris.text
        print(pris)
        assert "499" in pris

    def test_lager(self):
        lager = self.driver.find_element(By.XPATH, "//span[normalize-space()='I lager']")
        lager = lager.text
        print(lager)
        assert "I lager" in lager

    def test_additem(self):
        item1 = Netonnet(self.driver)
        item1.additem()
        item = self.driver.find_element(By.XPATH, "(//span[@class='cartItemCountValue'])[1]")
        item = item.text
        print(item)
        assert item == "1"
