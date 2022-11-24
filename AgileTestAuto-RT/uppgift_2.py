from selenium import webdriver
from selenium.webdriver.chrome.service import Service

path = "/Users/superman/PycharmProjects/bin/chromedriver"
s = Service(path)
driver = webdriver.Chrome(service=s)
'#open google website in chrome'
driver.get("https://www.google.se")

driver.maximize_window()
driver.close()