from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from BrowserStack import my_url

desired_cap = {
 'browser': 'Chrome',
 'browser_version': '80.0',
 'os': 'Windows',
 'os_version': '10',
 'resolution': '1024x768',
 'name': 'Bstack-[Python]-Test1'
}

url = my_url.bs_url
desired_cap['acceptsSsLCerts'] = True
driver = webdriver.Remote(
    command_executor=url,
    desired_capabilities=desired_cap)

#driver = webdriver.Chrome()
driver.get("https://qasvus.wordpress.com/")
driver.maximize_window()

#Print link(href) for header message "California Real Estate"
print(driver.find_element(By.XPATH,"//p[@class='site-title']//a[contains(text(),'California Real Estate')]").get_attribute("href"))
#print(driver.find_element_by_xpath("...").get_attribute("href"))

#Print link(src) for first home image under "About us"
print(driver.find_element(By.CLASS_NAME,"wp-image-55").get_attribute("src"))

#Verify (do assert) "California Real Estate" in website title
assert "California Real Estate" in driver.title
print(driver.title)

#verify this text is present on the web page
assert "Send Us a Message" in driver.page_source

#Fill out and send the message form
driver.find_element(By.ID, "g2-name").send_keys("INNA SURA")
driver.find_element(By.ID, "g2-email").send_keys("innasura12@gmail.com")
driver.find_element(By.NAME, "g2-message").send_keys("HAPPY TUESDAY!")

driver.implicitly_wait(20)
#driver.find_element(By.CLASS_NAME, "pushbutton-wide").click()
element = driver.find_element_by_class_name('pushbutton-wide')
driver.execute_script("arguments[0].click();", element)
driver.implicitly_wait(10)

#Go Back
#driver.find_element(By.XPATH, "//a[contains(text(),'go back')]").click()
element = driver.find_element(By.XPATH, "//a[contains(text(),'go back')]")
driver.execute_script("arguments[0].click();", element)

driver.implicitly_wait(10)
print(driver.find_element(By.CLASS_NAME,"pushbutton-wide").get_attribute("type"))

# closing browser
driver.quit()