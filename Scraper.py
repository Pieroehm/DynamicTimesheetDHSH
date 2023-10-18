from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Define your credentials
from credentials import USERNAME,PASSWORD

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Navigate to the website
driver.get('https://onlineportal.wak-sh.de/Detailseiten/Login/login')

# Find the username and password fields and fill them out
username_field = driver.find_element(By.ID, 'txtUserName')  # replace 'username_field_id' with the appropriate ID
password_field = driver.find_element(By.ID, 'txtPassword')  # replace 'password_field_id' with the appropriate ID

username_field.send_keys(USERNAME)
password_field.send_keys(PASSWORD)

# Submit the login form
password_field.send_keys(Keys.RETURN)  # This assumes the form submits when you press enter in the password field. Adjust if necessary.

# Wait for the login to complete (You can also use WebDriverWait to wait for a specific element to be loaded)
driver.implicitly_wait(10)  # waits up to 10 seconds for the elements to become available

# Find and click the button
button = driver.find_element(By.ID, 'btnIcalender')  # replace 'button_id' with the appropriate ID or use another method to locate the button
button.click()

driver.implicitly_wait(5)  # waits up to 10 seconds for the elements to become available
button = driver.find_element(By.ID, 'btnOkOkAbbrechenModal')  # replace 'button_id' with the appropriate ID or use another method to locate the button
button.click()

# You can continue with other tasks or close the browser
driver.quit()

