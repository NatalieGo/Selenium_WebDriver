from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://www.google.com/')
browser.quit()
