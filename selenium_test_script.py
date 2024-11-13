from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Update the path to your chromedriver.exe
service = Service(r"C:\Program Files\chromedriver.exe")

# Initialize WebDriver
driver = webdriver.Chrome(service=service)

# Navigate to Google
driver.get("http://127.0.0.1:5000")

try:
    # Wait until the search box is present
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )
    search_box.send_keys("Selenium Python")
    search_box.submit()

    # Wait for a few seconds to see the results
    time.sleep(5)
finally:
    # Close the browser
    driver.quit()
