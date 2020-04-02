import time
from python_rucaptcha import ReCaptchaV2
from selenium import webdriver

def timing(str):
    named_tuple = time.localtime()  # get struct_time
    time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
    print(str, time_string)

driver = webdriver.Chrome()
driver.get("http://www.123formbuilder.com/form-5012215/online-order-form")
time.sleep(1)
driver.find_element_by_xpath("//input[@placeholder='First']").send_keys("First_name")
time.sleep(1)
driver.find_element_by_xpath("//input[@placeholder='Last']").send_keys("Last_name")
time.sleep(1)
driver.find_element_by_xpath("//div//div//div[2]//div[1]//div[1]//input[1]").send_keys("123123132@mail.ru")
time.sleep(1)
driver.find_element_by_xpath("//input[contains(@placeholder,'### ### ####')]").send_keys("1234567899")
time.sleep(1)
driver.find_element_by_xpath("//label[@id='radio-0000000e0']/label").click()
time.sleep(1)
driver.find_element_by_xpath("//body/form[@id='form']/div/div/div/div/div[1]/div[1]/input[1]").send_keys("12")
time.sleep(1)
driver.find_element_by_xpath("//body/form[@id='form']/div/div/div/div/div/div/div[2]").click() #Вызываем календарь
time.sleep(1)
driver.find_element_by_class_name("today ").click()
time.sleep(1)
driver.find_element_by_xpath("//input[@placeholder='Street Address']").send_keys("Street Address12")
time.sleep(1)
driver.find_element_by_xpath("//input[@placeholder='City']").send_keys("City Cool")
time.sleep(1)
driver.find_element_by_xpath("//input[@placeholder='Region']").send_keys("Region Cool")
time.sleep(1)
driver.find_element_by_xpath("//input[@placeholder='Postal / Zip Code']").send_keys("2344322")
time.sleep(1)
driver.find_element_by_xpath("//input[@placeholder='Country']").click()
driver.find_element_by_xpath("//input[@placeholder='Country']").send_keys("Afghanistan")
time.sleep(1)
driver.find_element_by_xpath("//select").send_keys("Choice1")
time.sleep(1)
driver.find_element_by_xpath("//label[@id='checkbox-00000018-1']//label").click()

timing('before capcha')
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
#time.sleep(5)
driver.implicitly_wait(50)
#driver.execute_script("document.getElementById('text_field').value+='{0}'".format(foo))
timing('start script')

#capt = user_answer['captchaSolve']
#вставляем в скрытое поле
#string1 = str("javascript:document.getElementById('g-recaptcha-response').value = '{0}';".format(capt))
#driver.execute_script(string1)
driver.execute_script(str("javascript:document.getElementById('g-recaptcha-response').style.display = null;"))
driver.find_element_by_id('g-recaptcha-response').send_keys("123412341234")

#time.sleep(5)
driver.implicitly_wait(50)

timing('after script')

#driver.find_element_by_xpath("//span[contains(@class, 'normal-state')]").click()

driver.implicitly_wait(50)
#time.sleep(50)
driver.close()