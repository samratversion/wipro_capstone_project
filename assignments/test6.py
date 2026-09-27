from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import time

browsername="chrome"
if browsername.lower() == "chrome":
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
elif browsername.lower() == "firefox":
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
else:
    raise Exception("Invalid browser name. Please choose 'chrome' or 'firefox'.")


########
#Absolute XPath
#
#/html/body/div/form/input

#Relative XPath
#
#//input[@id='username']
########


driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

time.sleep(2)
driver.find_element(By.XPATH, '//input[@value="option1"]').click()
time.sleep(2)
driver.find_element(By.XPATH, '//input[@value="option2"]').click()
time.sleep(2)
driver.find_element(By.XPATH, '//input[@value="option3"]').click()
time.sleep(2)