from selenium import webdriver
from selenium.webdriver.common.by import By

# keep webpage open afer program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
#driver.get("https://www.amazon.com")
driver.get("https://www.amazon.fr/Garmin-f%C4%93nix-Pro-Solar-Multisports/dp/B0C3WBJX4F/ref=sr_1_5?__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&sr=8-5")

price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")

price_dollar = driver.find_element(By.XPATH, value='//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[3]/span[2]/span[1]')
price_cents = driver.find_element(By.XPATH, value='//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[3]/span[2]/span[2]')
print(f"The price is {price_dollar.text}.{price_cents.text}")
driver.close() # closes active tab

# Other useful
# By.CSS_SELECTOR
# By.ID
#by XPath https://www.w3schools.com/xml/xpath_intro.asp
# driver.close() # closes active tab
# driver.quit() # closes all tabs