from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.get('http://localhost/litecart/admin/')
browser.find_element_by_name("username").send_keys("admin")
browser.find_element_by_name("password").send_keys("admin")
browser.find_element_by_name("remember_me").click()
browser.find_element_by_name("login").click()
WebDriverWait(browser, 10).until(EC.title_is("My Store"))
browser.quit()
