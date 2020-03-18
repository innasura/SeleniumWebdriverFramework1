from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.123formbuilder.com/form-5012215/online-order-form")
driver.maximize_window()

#Fill out and send the message form
driver.find_element(By.XPATH, "//input[@placeholder='First']").send_keys("INNA")
driver.find_element(By.XPATH, "//input[@placeholder='Last']").send_keys("SURA")
driver.find_element(By.XPATH, "//div//div//div[2]//div[1]//div[1]//input[1]").send_keys("innasura12@gmail.com")
driver.find_element(By.XPATH, "//input[contains(@placeholder,'### ### ####')]").send_keys("818-555-5555")
#driver.find_element(By.XPATH, "???").send_keys("818-555-5555")
driver.find_element(By.XPATH, "//body/form[@id='form']/div/div/div/div/div[1]/div[1]/input[1]").send_keys("2")

#driver.find_element(By.XPATH, "//body/form[@id='form']/div/div/div[6]/div[1]/div[1]/div[1]/div[1]").send_keys("04/15/2020")
driver.find_element(By.XPATH,"//body/form[@id='form']/div/div/div[6]/div[1]/div[1]/div[1]/div[1]")
#element.send_keys("04152020")

driver.find_element(By.XPATH, "//input[@placeholder='Street Address']").send_keys("987 California Dr.")
driver.find_element(By.XPATH, "//input[@placeholder='City']").send_keys("Los Angeles")

driver.find_element(By.XPATH, "//input[@placeholder='Postal / Zip Code']").send_keys("90210")
driver.find_element(By.XPATH, "//input[@placeholder='Country']").send_keys("United States")
driver.find_element(By.XPATH, "//span[contains(text(),'Choice 1')]").click()
driver.find_element(By.XPATH, "//div[@class='recaptcha-container']").click()









#driver.implicitly_wait(20)
#element = driver.find_element(By.XPATH,"//body/form[@id='form']/div/div/div/button[1]")
#driver.execute_script("arguments[0].click();", element)
#driver.implicitly_wait(10)


'''
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
'''
# closing browser tab
driver.close()