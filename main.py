from selenium import webdriver
from selenium.webdriver.common.by import By

# keep webpage open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

event_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")

for time in event_times:
    print(time.text)

event_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")

for name in event_names:
    print(name.text)

events={}

for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_times[n].text
    }
print(events)

#upcoming_events = driver.find_elements_by_css_selector(".medium-widget.event-widget.last .shrubbery")
#print(upcoming_events)

driver.close() # closes active tab

# Other useful
# By.CSS_SELECTOR
# By.ID
#by XPath https://www.w3schools.com/xml/xpath_intro.asp
# pour utiliser des selecteurs multiples :
# si item est dans classe .event-widget, puis ds une li et un a: data = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")
# si item est dans classe .event-widget puis ds claasse schrubbery, nestée ds la 1e => data = driver.find_elements_by_css_selector(".medium-widget.event-widget.last .shrubbery"

# driver.close() # closes active tab
# driver.quit() # closes all tabs