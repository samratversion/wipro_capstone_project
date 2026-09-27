from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/2018/09/automation-form.html")
time.sleep(2)
submit_btn = driver.find_element(By.CSS_SELECTOR,"div.date-picker-box>button.submit-btn")
print("Found submit button via child selector:",submit_btn.text)

submit_btn_descendent = driver.find_element(By.CSS_SELECTOR,"div.date-picker-box button.submit-btn")
print("Found via descendent selector:",submit_btn_descendent.text)

submit_btn.click()
time.sleep(2)

driver.quit()