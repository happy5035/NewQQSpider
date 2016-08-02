# coding = utf-8
'''
Created on 2016.8.2

@author: yjw
'''
from selenium import webdriver
import time
import os
import traceback


def test():
    chrome_driver = os.path.abspath("D:\MyDrivers\chromedriver.exe")
    os.environ["webdriver.chrome.driver"] = chrome_driver
    browser = webdriver.Chrome(chrome_driver)
    print "begin..."
    time.sleep(0.3)
    browser.get("http://qzone.qq.com/")
    time.sleep(1)
    browser.switch_to.frame("login_frame")
    plogin = browser.find_element_by_id("switcher_plogin")
    plogin.click()
    time.sleep(1)
    u = browser.find_element_by_id('u')
    p = browser.find_element_by_id('p')
    u.send_keys("928385274")
    p.send_keys("@objective-c")
    login = browser.find_element_by_id("login_button")
    login.click()
    print browser.title
    print browser.get_cookies()
    time.sleep(3)
    browser.quit()


if __name__ == '__main__':
    try:
        print 3/0
    except Exception, e:
        print  traceback.format_exc()
        print e.message
    