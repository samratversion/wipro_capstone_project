from selenium import webdriver
from selenium.webdriver.chrome.options import Options


driver = webdriver.Chrome()
try:
    driver.get("https://www.google.com")

    print(driver.title)
finally:
    driver.quit()