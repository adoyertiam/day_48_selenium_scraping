from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# keep webpage open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Create and configure the Chrome webdriver
driver = webdriver.Chrome(options=chrome_options)

# ---------------------access wikipedia & interact -------------------------------------

driver.get("https://en.wikipedia.org/wiki/Main_Page")

# find elements by ID or CSS selector(s)
number_articles = driver.find_element(By.ID, value="articlecount")
article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a") #pound needed
# event_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a") #but here it's a dot :)
print(article_count.text)

# click on selected item
article_count.click()

# find element by link text
all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")

# find the <search> input by name
search = driver.find_element(By.NAME, value="search")

# send keyboard input to selenium
search.send_keys("Python", Keys.ENTER)

# closes all tabs
driver.quit()
