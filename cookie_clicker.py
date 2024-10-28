from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://orteil.dashnet.org/experiments/cookie/")

# variables
minutes = 5
game_is_on = True
timeout = time.time() + 60*minutes
powerup_timer_start = time.time()
powerup_timeout = 5

booster_names_list = []
booster_prices_list = []

cookies_per_second = driver.find_element(By.ID, value="cps")


#click on cookie
cookie = driver.find_element(By.ID, value="cookie")

#stop game after number of minutes
while time.time()<timeout:

    # check every 5 secs if enough money to buy powerup
    if time.time() > powerup_timer_start + powerup_timeout:
        money = driver.find_element(By.ID, value="money").text
        money = int(money.replace(",", ""))

        # Reset the booster lists
        booster_names_list = []  # <--- Liste réinitialisée à chaque itération
        booster_prices_list = []  # <--- Liste réinitialisée à chaque itération

        powerup_list = driver.find_elements(By.CSS_SELECTOR, value="#store b")
        powerup_list = powerup_list[:-1]
        powerup_list = powerup_list[len(powerup_list)-1:0:-1] # reverse list (from most expensive to cheapest)

        for item in powerup_list:
            # get booster names in a list
            booster_name = item.text.split(" - ")[0]
            booster_names_list.append(booster_name)

            # transform booster prices into readable numbers
            booster_price = item.text.split(" - ")[1]
            booster_price = int(booster_price.replace(",", ""))

            # get booster prices in a list
            booster_prices_list.append(booster_price)

        for index, booster_price in enumerate(booster_prices_list):
            if money > booster_price:
                booster_name = booster_names_list[index]
                driver.find_element(By.ID, value=f"buy{booster_name}").click()

        powerup_timer_start = time.time()

    cookie.click()

driver.quit()
print(cookies_per_second.text)