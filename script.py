from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Automatically download and manage ChromeDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open a website
driver.get("https://pypi.org/project/webdriver-manager/")  # Replace with the URL you need

# Wait for the page to load
time.sleep(2)

# Scroll down in steps
for _ in range(5):  # Adjust the range for more scrolling
    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
    time.sleep(1)  # Wait for content to load

# Alternative: Scroll to the bottom of the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)

# Close the browser
driver.quit()
