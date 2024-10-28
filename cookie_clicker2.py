from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.XPATH, value='//*[@id="cookie"]')

upgrades_id = ["buyTime machine", "buyPortal", "buyAlchemy lab", "buyShipment", "buyMine", "buyFactory", "buyGrandma",
               "buyCursor"]

iterations = 1
total_timeout = time.time() + (60 * 5)

while time.time() <= total_timeout:
    for _ in range(iterations):
        cookie.click()

    for upgrade_id in upgrades_id:
        try:
            driver.find_element(By.ID, value=upgrade_id).click()
        except:
            continue

    iterations += 10

cps = driver.find_element(By.ID, value="cps").text
print(cps)

driver.quit()