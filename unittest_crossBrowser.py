import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class ChromeSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
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

    def test_search_weather_chrome_1120x550(self):
        driver = self.driver
        driver_chrome = self.driver
        driver.set_window_size(1120, 550)
        driver_chrome.get('http://www.google.com')
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located((By.ID, 'hplogo')))
        time.sleep(1)

        search = driver_chrome.find_element_by_name("q")
        search.clear()
        search.send_keys("Weather San Jose")
        search.submit()
        wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="wob_wc"]')))
        driver.find_element_by_id("wob_rain").click()
        time.sleep(2)
        driver.find_element_by_id("wob_wind").click()
        time.sleep(1.5)
        driver.find_element_by_id("wob_temp").click()

        # Check if the search returns any result
        assert "No results found." not in driver_chrome.page_source, "No results found in Chrome"
        assert "Weather San Jose - Google Search" in driver.title
        print("Page title in Chrome 1120x550 is:", driver.title)
        time.sleep(1)

    def tearDown(self):
        # Close the browser.
        self.driver.quit()


class FirefoxSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
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

    def test_search_weather_firefox_1120x850(self):
        driver = self.driver
        driver_firefox = self.driver
        driver.set_window_size(1120, 850)
        driver_firefox.get('http://www.google.com')
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located((By.ID, 'hplogo')))
        time.sleep(1)

        search = driver_firefox.find_element_by_name("q")
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
        assert "No results found." not in driver_firefox.page_source, "No results found in Chrome"
        assert "Weather San Jose - Google Search" in driver.title
        print("Page title in Chrome 1120x850 is:", driver.title)

    # Anything declared in tearDown will be executed for all test cases
    def tearDown(self):
        # Close the browser.
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()