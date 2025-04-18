from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Change this to match your file location
file_path = "file:///C:/Users/dell/Desktop/selenium-add/index.html"

#file_path = "file:///C:\Users\dell\selenium-add/index.html"  # Windows
# file_path = "file:///Users/yourname/test-app/index.html"  # Mac/Linux

# Start the browser
driver = webdriver.Chrome()

# Open the HTML file
driver.get(file_path)

# Input values
driver.find_element(By.ID, "num1").send_keys("7")
driver.find_element(By.ID, "num2").send_keys("5")

# Click the Add button
driver.find_element(By.ID, "addBtn").click()

# Wait for the result
time.sleep(1)

# Verify the result
result = driver.find_element(By.ID, "result").text
assert result == "12", f"Test Failed! Expected 12 but got {result}"
print("✅ Test Passed: 7 + 5 = 12")

# Close the browser
driver.quit()
