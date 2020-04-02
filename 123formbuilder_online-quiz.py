import random
import unittest
from time import sleep

import selenium.common.exceptions as Ex
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


# *************************************************
# Fill out form by Chrome http://www.123formbuilder.com/form-5012206/online-quiz
# *************************************************

class ChromeFillForm(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_fill_form(self):
        driver = self.driver
        driver.get("http://www.123formbuilder.com/form-5012206/online-quiz")
        try:
            WebDriverWait(driver, 10). \
                until(EC.visibility_of_element_located((By.XPATH, "//h1[contains(text(),'Online Quiz')]")))
            print('Go!', driver.name)
        except Ex.TimeoutException:
            print('Warning! Too mach time to load page', driver.name)
            driver.get_screenshot_as_file('Load_main_page_mach_time' + driver.name + '.png')
            driver.quit()
        try:  # radio animal
            WebDriverWait(driver, 3). \
                until(EC.visibility_of_element_located((By.XPATH, "//div[@data-hash='00000008']")))
            xpath = "//input[@id='00000008_" + str(random.randint(1, 3)) + "']"
            driver.find_element(By.XPATH, xpath).click()
            print('Found Animal Radio', xpath)
        except Ex.TimeoutException:
            print('No Animal Radio!')
            driver.quit()
        try:  # radio river
            WebDriverWait(driver, 3). \
                until(EC.visibility_of_element_located((By.XPATH, "//div[@data-hash='0000000a']")))
            xpath = "//label[@id='radio-0000000a" + str(random.randint(0, 2)) + "']"
            driver.find_element(By.XPATH, xpath).click()
            print('Found River Radio ', xpath)
        except Ex.TimeoutException:
            print('No River Radio!')
            driver.quit()
        try:  # checkbox inventions
            WebDriverWait(driver, 3). \
                until(EC.visibility_of_element_located((By.XPATH, "//div[@data-hash='0000000c']")))
            xpath = "//label[contains(@id,'checkbox-0000000c-') and @data-role='choice']"
            chbox_list = driver.find_elements(By.XPATH, xpath)
            for c in chbox_list:
                if random.randint(False, True): c.click()
            print('Found inventions CheckBox ', xpath)
        except Ex.TimeoutException:
            print('No Inventions CheckBox!')
            driver.quit()
        try:  # checkbox hardware
            WebDriverWait(driver, 3). \
                until(EC.visibility_of_element_located((By.XPATH, "//div[@data-hash='0000000e']")))
            xpath = "//label[contains(@id,'checkbox-0000000e-') and @data-role='choice']"
            chbox_list = driver.find_elements(By.XPATH, xpath)
            for c in chbox_list:
                if random.randint(False, True): c.click()
            print('Found hardware CheckBox ', xpath)
        except Ex.TimeoutException:
            print('No Hardware CheckBox!')
            driver.quit()
        try:  # radio food
            WebDriverWait(driver, 3). \
                until(EC.visibility_of_element_located((By.XPATH, "//div[@data-hash='00000010']")))
            xpath = "//label[@id='radio-00000010" + str(random.randint(0, 2)) + "']"
            driver.find_element(By.XPATH, xpath).click()
            print('Found Food Radio ', xpath)
        except Ex.TimeoutException:
            print('No Food Radio!')
            driver.quit()
        try:  # radio food
            xpath = "//input[@type='email']"
            WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            driver.find_element(By.XPATH, xpath).send_keys('Testing@test.com')
            print('Found Email', xpath)
        except Ex.TimeoutException:
            print('No Email!')
            driver.quit()
        try:  # button submit
            WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, "//button[@type='submit']")))
            driver.find_element(By.XPATH, "//button[@type='submit']").click()
            print('Send!')
        except Ex.NoSuchElementException:
            print('No Submit Button!')
            driver.quit()
        sleep(10)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    ChromeFillForm.main()