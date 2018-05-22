import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

class Bing_signin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.actions = ActionChains(self.driver)
        self.Enter = u'\ue007'
        
        #*** User Configurable Values ***#
        self.driver.get("https://www.bing.com")
        self.sign_in_location = 'id_s'
        self.username_location = '//*[@id="i0116"]'
        self.password_location = '//*[@id="i0118"]'
        self.accounts_menu_location = '//*[@id="id_p"]'
        self.sign_out_location = '//*[@id="b_idProviders"]/li/a/span[2]'
        self.username = "USERNAME"
        self.password = "PASSWORD"

    def test_account_login(self):
        sign_in = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, self.sign_in_location)))
        sign_in.click()
        
        #Enter text into Username field
        username_field = WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH, self.username_location)))
        username_field.send_keys(self.username)
        username_field.send_keys(self.Enter)
        
        # Enter text into Password field 
        password_field = WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH, self.password_location)))
        password_field.send_keys(self.password)
        password_field.send_keys(self.Enter)

    def tearDown(self):
        print(" ---> TEST COMPLETE")


if __name__ == '__main__':
    unittest.main(verbosity=2)
