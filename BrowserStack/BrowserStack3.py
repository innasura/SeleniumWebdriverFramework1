import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from BrowserStack import my_url


class ChromeSearch(unittest.TestCase):

    def setUp(self):
        #self.driver = webdriver.Chrome()

        desired_cap = {
            'browser': 'Chrome',
            'browser_version': '80.0',
            'os': 'Windows',
            'os_version': '10',
            'resolution': '1024x768',
            'name': 'Bstack-[Python]-Chrome1'
        }

        url = my_url.bs_url
        desired_cap['acceptSslCerts'] = True
        self.driver = webdriver.Remote(
            command_executor=url,
            desired_capabilities=desired_cap)

        self.driver.maximize_window()

    # As per unittest module, individual test should start with test_
    def test_search_weather_chrome(self):
        driver = self.driver
        driver_chrome = self.driver
        driver_chrome.get('http://www.google.com')
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located((By.ID, 'hplogo')))
        time.sleep(1)  # simulate long running test

        search = driver_chrome.find_element_by_name("q")
        search.clear()
        search.send_keys("Weather San Jose")
        search.submit()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="wob_wc"]')))
        driver.find_element_by_id("wob_rain").click()
        time.sleep(1)
        driver.find_element_by_id("wob_wind").click()
        time.sleep(1.5)
        driver.find_element_by_id("wob_temp").click()

        # Check if the search returns any result
        assert "No results found." not in driver_chrome.page_source, "No results found in Chrome"
        assert "Weather San Jose - Google Search" in driver.title
        print("Page title in Chrome is:", driver.title)
        time.sleep(1)

    def tearDown(self):
        # Close the browser.
        self.driver.quit()


class FirefoxSearch(unittest.TestCase):
    def setUp(self):
        #self.driver = webdriver.Firefox()

        desired_cap = {
            'browser': 'Firefox',
            'browser_version': '75.0 beta',
            'os': 'Windows',
            'os_version': '10',
            'resolution': '1024x768',
            'name': 'Bstack-[Python]-Firefox1'
        }

        url = my_url.bs_url
        desired_cap['acceptSslCerts'] = True
        self.driver = webdriver.Remote(
            command_executor=url,
            desired_capabilities=desired_cap)

        self.driver.maximize_window()

    # As per unittest module, individual test should start with test_
    def test_search_weather_firefox(self):
        driver_ff = self.driver
        driver_ff.get('http://www.google.com')
        wait = WebDriverWait(driver_ff, 5)
        wait.until(EC.visibility_of_element_located((By.ID, 'hplogo')))
        time.sleep(1)

        search = driver_ff.find_element_by_name("q")
        search.clear()
        search.send_keys("Weather San Jose")
        search.submit()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="wob_wc"]')))
        driver_ff.find_element_by_id("wob_rain").click()
        time.sleep(1.5)
        driver_ff.find_element_by_id("wob_wind").click()
        time.sleep(1)
        driver_ff.find_element_by_id("wob_temp").click()

        # Check if the search returns any result
        assert "No results found." not in driver_ff.page_source, "No results found in Chrome"
        assert "Weather San Jose - Google Search" in driver_ff.title
        print("Page title in Firefox is:", driver_ff.title)
        time.sleep(1)

    # Anything declared in tearDown will be executed for all test cases
    def tearDown(self):
        # Close the browser.
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()