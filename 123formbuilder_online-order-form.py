# http://www.123formbuilder.com/form-5012215/online-order-form
#import KillProcess
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import random
from time import sleep
from python_rucaptcha import ReCaptchaV2

## to clear the memory from the chromedriver.exe
#KillProcess.killproc('chromedriver.exe') #kill chromedriver.exe #можно вставить для очистки памяти

driver = webdriver.Chrome()
driver.get("http://www.123formbuilder.com/form-5012215/online-order-form")
driver.maximize_window()

driver.find_element_by_xpath("//input[@placeholder='First']").send_keys('FirstName')
driver.find_element_by_xpath("//input[@placeholder='Last']").send_keys('LastName')
driver.find_element_by_xpath("//input[@type='email']").send_keys(str(random.randrange(1000,9999))+'@gmail.com')
driver.find_element_by_xpath("//input[@placeholder='### ### #### ']").send_keys(str(random.randrange(1,9999999999)).zfill(10))

driver.find_element_by_tag_name('html').send_keys(Keys.PAGE_DOWN)

driver.implicitly_wait(5)

driver.find_element_by_id("0000000e_1").click() #RADIO

driver.implicitly_wait(5)
driver.find_element_by_xpath("//input[@type='number']").send_keys(str(random.randint(1, 100))) #quantity
driver.find_element_by_xpath("//body/form[@id='form']/div/div/div/div/div/div/div[2]").click() #Вызываем календарь
sleep(1)
driver.find_element_by_class_name("today ").click()
driver.find_element_by_xpath("//input[@placeholder='Street Address']").send_keys('12345 Main St')
driver.find_element_by_xpath("//input[@placeholder='Street Address Line 2']").send_keys('Apt #255')
driver.find_element_by_xpath("//input[@placeholder='City']").send_keys('Encino')
driver.find_element_by_xpath("//input[@placeholder='Region']").send_keys('CA')
driver.find_element_by_xpath("//input[@placeholder='Postal / Zip Code']").send_keys('91305')
driver.find_element_by_xpath("//input[@placeholder='Country']").click()#send_keys('\n')
driver.implicitly_wait(5)
#driver.find_element_by_xpath("//input[@placeholder='Country']").send_keys('Albania') #самое очевидное решение для заполнения
driver.find_element_by_xpath("//*[contains(text(), 'United States')]").click() #можно было в input толкать, но мы же эмулируем работу пользователя, так что жмем элемент из списка

driver.find_element_by_tag_name('html').send_keys(Keys.PAGE_DOWN)
sleep(1)

Select(driver.find_element_by_tag_name('select')).select_by_index(1) #simple select
#driver.find_element_by_xpath("//option[contains(text(),'Choice1')]").click() #или можно так, самый простой способ
driver.find_element_by_tag_name('html').send_keys(Keys.PAGE_DOWN)
driver.implicitly_wait(5)
driver.find_element_by_tag_name('html').send_keys('\n')
driver.find_element_by_id("00000018_1").click()
driver.find_element_by_id("00000018_3").click()
driver.find_element_by_xpath("//input[@type='text'][@data-role='other']").send_keys('blablabla')


#frame = driver.find_element_by_xpath('//iframe[contains(@src, "recaptcha")]')
#driver.switch_to.frame(frame)
#driver.find_element_by_xpath("//*[@id='recaptcha-anchor']").click() #Jam! # Капча нажмется, но потом разгадывание велосипедов и автобусов


# Введите ключ от сервиса RuCaptcha, из своего аккаунта
RUCAPTCHA_KEY = "53da620a6ac51a8ad6adc5bc9bac7822"
# G-ReCaptcha ключ сайта
SITE_KEY = "6LdMNiMTAAAAAGr0ibqKRZc3e5Z6wfLBraX9NuOY"
# Ссылка на страницу с капчёй
PAGE_URL = "http://www.123formbuilder.com/form-5012215/online-order-form"
# Возвращается JSON содержащий информацию для решения капчи
user_answer = ReCaptchaV2.ReCaptchaV2(rucaptcha_key=RUCAPTCHA_KEY).captcha_handler(site_key=SITE_KEY, page_url=PAGE_URL)
#if not user_answer['error']:
# решение капчи
#    print('captchaSolve: ', user_answer['captchaSolve'])
#    print('taskId ', user_answer['taskId'])
#elif user_answer['error']:
# Тело ошибки, если есть
#    print(user_answer['errorBody']['text'])
#    print(user_answer['errorBody']['id'])
sleep(2)
#driver.execute_script("document.getElementById('text_field').value+='{0}'".format(foo))
capt = user_answer['captchaSolve']
#вставляем в скрытое поле
string1 = str("javascript:document.getElementById('g-recaptcha-response').value = '{0}';".format(capt))
driver.execute_script(string1)
sleep(100)

driver.find_element_by_xpath("//button[@type='submit']").click()
#driver.close()
