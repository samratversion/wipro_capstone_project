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


driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.find_element(By.XPATH, "//input[@id='name']").send_keys("Kousttav")
time.sleep(2)
driver.find_element(By.XPATH, "//input[@id='email']").send_keys("test@example.com")
time.sleep(2)
driver.find_element(By.XPATH, "//input[@id='phone']").send_keys("9614729415")
time.sleep(2)
driver.find_element(By.XPATH, "//textarea[@id='textarea']").send_keys("ABCD, XYZ, India")
time.sleep(2)
driver.find_element(By.XPATH, "//input[@value='male']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//input[@id='sunday']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//input[@id='monday']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//input[@id='tuesday']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//option[@value='india']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//option[@value='red']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//option[@value='blue']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//option[@value='fox']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//input[@id='datepicker']").send_keys("08/15/2026")
time.sleep(2)
driver.find_element(By.XPATH, "//input[@id='txtDate']").send_keys("08/16/2026")
time.sleep(2)
driver.find_element(By.XPATH, "//input[@id='start-date']").send_keys("06/18/2026")
time.sleep(2)
driver.find_element(By.XPATH, "//button[@class='submit-btn']").click()
time.sleep(2)
