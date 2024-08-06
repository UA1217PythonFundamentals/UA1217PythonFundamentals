from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("http://www.python.org")
assert "Python" in driver.title
import time
time.sleep(2)
elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys("pycon")
time.sleep(2)
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
time.sleep(2)
driver.close()