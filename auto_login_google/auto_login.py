from selenium import webdriver
import time

url = 'https://www.google.com'
email = input('請輸入你的google email帳號')
pwd = input('請輸入你的google email密碼')

browser = webdriver.Chrome()
browser.get(url)

browser.find_element_by_id('gb').click()
browser.find_element_by_id('identifierId').send_keys(email)
time.sleep(3)