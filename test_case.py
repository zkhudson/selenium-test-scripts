import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class Bing_signin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.Enter = u'\ue007'
        
        #*** User Configurable Values ***#
        self.username = "USERNAME"
        self.password = "PASSWORD"
        
        self.driver.get("https://www.bing.com")
        self.sign_in_location = '#id_s'
        self.username_location = '#i0116'
        self.password_location = '//*[@id="i0118"]'
        self.accounts_menu_location = '#id_p'
        self.sign_out_location = '//*[@id="b_idProviders"]/li/a/span[2]'
        self.user_text_location = '#id_n'


    def test_account_login(self):
        sign_in = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.sign_in_location)))
        sign_in.click()
        
        #Enter text into Username field
        username_field = WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.username_location)))
        self.assertIn('Sign in to your Microsoft account', self.driver.title)
        username_field.send_keys(self.username)
        
        # Check that the USERNAME has been entered in the Username field, then press Enter
        username_val = username_field.get_attribute('value')
        self.assertEqual(self.username, username_val)
        username_field.send_keys(self.Enter)

        # Enter text into Password field 
        password_field = WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH, self.password_location)))
        self.assertIn('Sign in to your Microsoft account', self.driver.title)
        password_field.send_keys(self.password)

        # Check that the PASSWORD has been entered in the Password field, then press Enter
        password_val = password_field.get_attribute('value')
        self.assertEqual(self.password, password_val)
        password_field.send_keys(self.Enter)

        # Sign out of account
        accounts_menu = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.accounts_menu_location)))
        self.assertIn('Bing', self.driver.title)
        accounts_menu.click()
        self.driver.implicitly_wait(1)
        sign_out = self.driver.find_element(By.XPATH, self.sign_out_location)
        sign_out.click()
        
        # Check that the Sign in text is visible after signing out of the account, i.e. the user's name is not shown
        self.driver.implicitly_wait(4)
        user_text = self.driver.find_element(By.CSS_SELECTOR, self.user_text_location)
        self.assertFalse(user_text.is_displayed())

    def tearDown(self):
        print("\n\n [---> TEST COMPLETE <---] \n")



if __name__ == '__main__':
    unittest.main(verbosity=2)
