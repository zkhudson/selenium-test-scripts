import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
driver.get("https://www.bing.com")
actions = ActionChains(driver)

photo_button = wait.until(EC.element_to_be_clickable((By.ID, 'vs_bs_download')))
photo_button.click()