from selenium import webdriver


driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('http://localhost/litecart/')
list = driver.find_elements_by_css_selector(".image-wrapper")
x = 0
for i in list:
    list[x].find_element_by_css_selector("[class*=sticker]")
    x += 1
driver.quit()

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get('http://localhost/litecart/')
list = driver.find_elements_by_css_selector(".image-wrapper")
x = 0
for i in list:
    list[x].find_element_by_css_selector("[class*=sticker]")
    x += 1
driver.quit()

driver = webdriver.Edge()
driver.implicitly_wait(10)
driver.get('http://localhost/litecart/')
list = driver.find_elements_by_css_selector(".image-wrapper")
x = 0
for i in list:
    list[x].find_element_by_css_selector("[class*=sticker]")
    x += 1
driver.quit()

driver = webdriver.Ie()
driver.implicitly_wait(10)
driver.get('http://localhost/litecart/')
list = driver.find_elements_by_css_selector(".image-wrapper")
x = 0
for i in list:
    list[x].find_element_by_css_selector("[class*=sticker]")
    x += 1
driver.quit()
