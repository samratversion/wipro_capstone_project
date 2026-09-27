from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time

DEMO_PAUSE = 4

driver = webdriver.Chrome()
driver.maximize_window()

try:
    driver.get("https://the-internet.herokuapp.com/")
    assert "The Internet" in driver.title, "Title verification failed!"
    print(f"[PASS] Page title verified: '{driver.title}'")
    time.sleep(DEMO_PAUSE)

    driver.get("https://the-internet.herokuapp.com/checkboxes")
    time.sleep(DEMO_PAUSE)

    wait = WebDriverWait(driver, 10)
    checkbox = wait.until(
        EC.element_to_be_clickable((By.XPATH, "(//input[@type='checkbox'])[1]"))
    )
    checkbox.click()
    print("[PASS] Checkbox clicked successfully.")
    time.sleep(DEMO_PAUSE)

    driver.get("https://the-internet.herokuapp.com/dropdown")
    time.sleep(DEMO_PAUSE)

    dropdown_element = wait.until(
        EC.presence_of_element_located((By.ID, "dropdown"))
    )
    dropdown = Select(dropdown_element)
    dropdown.select_by_visible_text("Option 2")
    print("[PASS] Dropdown option selected successfully.")
    time.sleep(DEMO_PAUSE)

    driver.get("https://the-internet.herokuapp.com/inputs")
    time.sleep(DEMO_PAUSE)

    number_input = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='number']"))
    )
    number_input.send_keys("123")
    print("[PASS] Number entered into input field successfully.")
    time.sleep(DEMO_PAUSE)

    driver.save_screenshot("successful_interaction.png")
    print("[PASS] Screenshot captured: successful_interaction.png")
    time.sleep(DEMO_PAUSE)

    try:
        driver.find_element(By.ID, "this-id-does-not-exist-on-page")
    except NoSuchElementException:
        print("[HANDLED] Expected failure caught: "
              "Element with id 'this-id-does-not-exist-on-page' was not found "
              "on the /inputs page. This is expected and handled gracefully.")
        time.sleep(DEMO_PAUSE)

except (AssertionError, TimeoutException) as e:
    print(f"[FAIL] A real test failure occurred: {e}")

finally:
    driver.quit()
    print("[INFO] Browser session closed safely.")