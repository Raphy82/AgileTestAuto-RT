import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

'# Main driver'
@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    '#Open Netonnet website in chrome'
    driver.get("https://www.netonnet.se")
    driver.find_element(By.XPATH, "//*[@id='cookiebannerShowSettingsButton']/div/div[1]/button").click()
    driver.fullscreen_window()
    '# provide "driver" for any calling fixture'
    request.cls.driver = driver
    yield
    driver.close()
