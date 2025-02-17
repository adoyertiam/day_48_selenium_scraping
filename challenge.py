from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

# ---------------------------auto fill up a form ---------------------------

driver.get("https://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME,value="fName")
last_name = driver.find_element(By.NAME,value="lName")
email = driver.find_element(By.NAME,value="email")

# fill
first_name.send_keys("David")
last_name.send_keys("Gaudin")
email.send_keys("yolo@gmail.com")

sign_up_button = driver.find_element(By.CSS_SELECTOR, value="form button")
sign_up_button.click()