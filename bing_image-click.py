from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome() 
driver.get("https://www.bing.com")

search_field = driver.find_element_by_css_selector("#sb_form_q")
search_field.click()
search_field.send_keys("bourbon.io")
search_field.send_keys(Keys.RETURN)

driver.implicitly_wait(1)
images = driver.find_element_by_css_selector("#b_header > nav > ul > li:nth-child(2) > a")
images.click()

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((
    By.CSS_SELECTOR, "#mmComponent_images_1 > ul:nth-child(6) > li:nth-child(1) > div > div.imgpt > a > div > img"))).click()
