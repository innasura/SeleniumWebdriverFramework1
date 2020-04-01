import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from BrowserStack import my_url


class ChromeSubmitForm(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.Chrome()
        desired_cap = {
            'browser': 'Chrome',
            'browser_version': '80.0',
            'os': 'Windows',
            'os_version': '10',
            'resolution': '1024x768',
            'name': 'Bstack-[Python]-CARealEstate_Chrome1'
        }
        url = my_url.bs_url
        desired_cap['acceptSslCerts'] = True
        self.driver = webdriver.Remote(command_executor=url, desired_capabilities=desired_cap)
        self.driver.maximize_window()

    # As per unittest module, individual test should start with test_
    def test_submit_form_chrome(self):
        driver = self.driver
        driver_chrome = self.driver
        driver_chrome.get('https://qasvus.wordpress.com')
        wait = WebDriverWait(driver, 3)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@class='pushbutton-wide']")))
        time.sleep(1)  # simulate long running test

        assert "California Real Estate" in driver.title
        print("Page title in Chrome is:", driver.title)

        # Clear fields: text area, first and last name
        driver.find_element(By.ID, "g2-name").clear()
        driver.find_element(By.ID, "g2-email").clear()
        driver.find_element(By.NAME, "g2-message").clear()
        time.sleep(1)

        #Fill out all fields and click on Submit button
        driver.find_element(By.ID, "g2-name").send_keys("INNA SURA")
        driver.find_element(By.ID, "g2-email").send_keys("innasura12@gmail.com")
        driver.find_element(By.NAME, "g2-message").send_keys("Hello")
        driver.implicitly_wait(10)
        element = driver.find_element_by_class_name('pushbutton-wide')
        driver.execute_script("arguments[0].click();", element)
        driver.implicitly_wait(10)

        # Use "try/except" method to wait "go back" link is VISIBLE and click it after
        try:
            WebDriverWait(driver, 10) \
                .until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'go back')]")))
            element = driver.find_element(By.XPATH, "//a[contains(text(),'go back')]")
            driver.execute_script("arguments[0].click();", element)
            print("The form is submitted!")
        except TimeoutException:
            print("Loading took too much time!")

        # Use "wait.until" method for visibility of all 4 houses images on the main page
        WebDriverWait(driver, 10) \
            .until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-55']")))
        WebDriverWait(driver, 10) \
            .until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-34']")))
        WebDriverWait(driver, 10) \
            .until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-56']")))
        WebDriverWait(driver, 10) \
            .until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-30']")))

        # Do assertion for page title and print it with custom string
        assert "California Real Estate" in driver.title
        print("GO BACK Page title in Chrome is:", driver.title)

    def tearDown(self):
        # Close the browser.
        self.driver.quit()


class FirefoxSubmitButton(unittest.TestCase):
    def setUp(self):
        # self.driver = webdriver.Firefox()
        desired_cap = {
            'browser': 'Firefox',
            'browser_version': '75.0 beta',
            'os': 'Windows',
            'os_version': '10',
            'resolution': '1024x768',
            'name': 'Bstack-[Python]-CARealEstate_Firefox1'
        }
        url = my_url.bs_url
        desired_cap['acceptSslCerts'] = True
        self.driver = webdriver.Remote(command_executor=url, desired_capabilities=desired_cap)
        self.driver.maximize_window()

    # As per unittest module, individual test should start with test_
    def test_submit_button_firefox(self):
        driver = self.driver
        driver_ff = self.driver
        driver_ff.get('https://qasvus.wordpress.com')
        wait = WebDriverWait(driver, 3)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@class='pushbutton-wide']")))
        time.sleep(1)  # simulate long running test

        assert "California Real Estate" in driver.title
        print("Page title in Firefox is:", driver.title)

        # Clear fields: text area, first and last name
        driver.find_element(By.ID, "g2-name").clear()
        driver.find_element(By.ID, "g2-email").clear()
        driver.find_element(By.NAME, "g2-message").clear()
        time.sleep(1)

        # Fill out all fields and click on Submit button
        driver.find_element(By.ID, "g2-name").send_keys("INNA SURA")
        driver.find_element(By.ID, "g2-email").send_keys("innasura12@gmail.com")
        driver.find_element(By.NAME, "g2-message").send_keys("Hello")
        driver.implicitly_wait(10)
        element = driver.find_element_by_class_name('pushbutton-wide')
        driver.execute_script("arguments[0].click();", element)
        driver.implicitly_wait(10)

        # Use "try/except" method to wait "go back" link is VISIBLE and click it after
        try:
            WebDriverWait(driver, 10) \
                .until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'go back')]")))
            element = driver.find_element(By.XPATH, "//a[contains(text(),'go back')]")
            driver.execute_script("arguments[0].click();", element)
            print("The form in Firefox is submitted!")
        except TimeoutException:
            print("Loading took too much time!")

        # Use "wait.until" method for visibility of all 4 houses images on the main page
        WebDriverWait(driver, 10) \
            .until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-55']")))
        WebDriverWait(driver, 10) \
            .until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-34']")))
        WebDriverWait(driver, 10) \
            .until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-56']")))
        WebDriverWait(driver, 10) \
            .until(EC.visibility_of_element_located((By.XPATH, "//img[@class='wp-image-30']")))

        # Do assertion for page title and print it with custom string
        assert "California Real Estate" in driver.title
        print("GO BACK Page title in Firefox is:", driver.title)

    # Anything declared in tearDown will be executed for all test cases
    def tearDown(self):
        # Close the browser.
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()