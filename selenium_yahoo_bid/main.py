from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime

if __name__ == '__main__':

    browser = webdriver.Chrome()
    browser.get('https://login.yahoo.com')  # 登入奇摩購物
    emailElem = browser.find_element_by_id('login-username')
    emailElem.send_keys('xxx')  # 填寫帳號
    loginbtn = browser.find_element_by_id("login-signin")
    loginbtn.click()  # 自動點選下一步

    passwordElem = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "login-passwd"))
    )
    passwordElem.send_keys('xxx')  # 填寫密碼
    submitBtn = browser.find_element_by_id("login-signin")
    submitBtn.click()  # 自動點選下一步

    # https://tw.buy.yahoo.com/gdsale/gdsale.asp?gdid=9172803

    # 商品頁面網址請輸入
    browser.get('xxx')
    url = "xxx"
    browser.implicitly_wait(5)
    delay = 0.01  # seconds   頁面刷新時間

    # 判定是否開放，若有則購買
    counter = 0
    while True:
        counter += 1

        try:
            browser.get(url)
            myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.CLASS_NAME,'SasCheckoutButton__mod___1BK9F.CheckoutBar__buyNowBtn___qgDtR.CheckoutBar__checkoutButton___jSkkJ')))
            print('located')
            break
        except:
            print(f"reload #{counter}")

    myElem.click()

    time.sleep(2)
    browser.find_element_by_xpath('//*[@id="checkout"]/div[4]/div[4]/div[4]/button').click()

    # 設定時間購買
    # def buy_on_time(buytime):
    #     while True:
    #         now = datetime.now()
    #         print (now)
    #         if now.strftime('%Y-%m-%d %H:%M:%S') == buytime:
    #             browser.find_element_by_xpath('//*[@id="checkout"]/div[4]/div[4]/div[4]/button').click()
    #
    # buy_on_time('2021-03-23 11:03:00')









