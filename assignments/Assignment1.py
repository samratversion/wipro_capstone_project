from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# ==========================================
# ASSIGNMENT 1: WEB ELEMENT IDENTIFICATION
# ==========================================

# Open Chrome
driver = webdriver.Chrome()

# Open webpage
driver.get("https://testautomationpractice.blogspot.com/")

# Maximize browser
driver.maximize_window()

time.sleep(2)

# ==========================================
# 1. By.ID
# Locate the Name field
# ==========================================

name_field = driver.find_element(By.ID, "name")
print("By.ID:", name_field.get_attribute("id"))

# Fill the Name field
name_field.send_keys("Ankita Chakraborty")

time.sleep(1)

# ==========================================
# 2. By.NAME
# Locate Gender using its name attribute
# ==========================================

gender = driver.find_element(By.NAME, "gender")
print("By.NAME:", gender.get_attribute("name"))

# Select gender
gender.click()

time.sleep(1)

# ==========================================
# 3. By.TAG_NAME
# Locate an input element
# ==========================================

input_element = driver.find_element(By.TAG_NAME, "input")
print("By.TAG_NAME:", input_element.tag_name)

time.sleep(1)

# ==========================================
# 4. By.LINK_TEXT
# Locate a specific link
# ==========================================

print("\n--- LINK TEXT ---")

link = driver.find_element(By.LINK_TEXT, "Udemy Courses")

print("Link Text:", link.text)
print("Href:", link.get_attribute("href"))

time.sleep(1)

# ==========================================
# 5. By.CLASS_NAME
# Locate Submit button
# ==========================================

button = driver.find_element(By.CLASS_NAME, "submit-btn")

print("By.CLASS_NAME:", button.get_attribute("class"))

time.sleep(2)

# ==========================================
# Keep browser open
# ==========================================

time.sleep(10)

# ==========================================
# Close browser
# ==========================================

driver.quit()
