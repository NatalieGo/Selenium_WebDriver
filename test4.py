from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(desired_capabilities={"chromeOptions": {"args": ["--start-fullscreen"]}})
driver.implicitly_wait(10)
driver.get('http://localhost/litecart/admin/')
driver.find_element_by_name("username").send_keys("admin")
driver.find_element_by_name("password").send_keys("admin")
driver.find_element_by_name("login").click()
WebDriverWait(driver, 10).until(EC.title_is("My Store"))
list = driver.find_elements_by_class_name("name")
x = 0
for i in list:
    list[x].click()
    driver.find_element_by_tag_name("h1")
    x+=1
    block = driver.find_element_by_css_selector("#app-.selected")
    list1 = block.find_elements_by_class_name("name")
    a = list1.__len__()
    if a > 1:
        y = 0
        for i in list1:
            list1[y].click()
            driver.find_element_by_tag_name("h1")
            y+=1
            block = driver.find_element_by_css_selector("#app-.selected")
            list1 = block.find_elements_by_class_name("name")
    driver.get('http://localhost/litecart/admin/')
    list = driver.find_elements_by_class_name("name")
driver.quit()

driver = webdriver.Firefox(firefox_binary="c:\\Program Files\\Mozilla FirefoxNew\\firefox.exe")
driver.implicitly_wait(10)
driver.get('http://localhost/litecart/admin/')
driver.find_element_by_name("username").send_keys("admin")
driver.find_element_by_name("password").send_keys("admin")
driver.find_element_by_name("login").click()
WebDriverWait(driver, 10).until(EC.title_is("My Store"))
list = driver.find_elements_by_class_name("name")
x = 0
for i in list:
    list[x].click()
    driver.find_element_by_tag_name("h1")
    x+=1
    block = driver.find_element_by_css_selector("#app-.selected")
    list1 = block.find_elements_by_class_name("name")
    a = list1.__len__()
    if a > 1:
        y = 0
        for i in list1:
            list1[y].click()
            driver.find_element_by_tag_name("h1")
            y+=1
            block = driver.find_element_by_css_selector("#app-.selected")
            list1 = block.find_elements_by_class_name("name")
    driver.get('http://localhost/litecart/admin/')
    list = driver.find_elements_by_class_name("name")
driver.quit()

driver = webdriver.Edge()
driver.implicitly_wait(10)
driver.get('http://localhost/litecart/admin/')
driver.find_element_by_name("username").send_keys("admin")
driver.find_element_by_name("password").send_keys("admin")
driver.find_element_by_name("login").click()
WebDriverWait(driver, 10).until(EC.title_is("My Store"))
list = driver.find_elements_by_class_name("name")
x = 0
for i in list:
    list[x].click()
    driver.find_element_by_tag_name("h1")
    x+=1
    block = driver.find_element_by_css_selector("#app-.selected")
    list1 = block.find_elements_by_class_name("name")
    a = list1.__len__()
    if a > 1:
        y = 0
        for i in list1:
            list1[y].click()
            driver.find_element_by_tag_name("h1")
            y+=1
            block = driver.find_element_by_css_selector("#app-.selected")
            list1 = block.find_elements_by_class_name("name")
    driver.get('http://localhost/litecart/admin/')
    list = driver.find_elements_by_class_name("name")
driver.quit()

driver = webdriver.Ie()
driver.implicitly_wait(10)
driver.get('http://localhost/litecart/admin/')
driver.find_element_by_name("username").send_keys("admin")
driver.find_element_by_name("password").send_keys("admin")
driver.find_element_by_name("login").click()
WebDriverWait(driver, 10).until(EC.title_is("My Store"))
list = driver.find_elements_by_class_name("name")
x = 0
for i in list:
    list[x].click()
    driver.find_element_by_tag_name("h1")
    x+=1
    block = driver.find_element_by_css_selector("#app-.selected")
    list1 = block.find_elements_by_class_name("name")
    a = list1.__len__()
    if a > 1:
        y = 0
        for i in list1:
            list1[y].click()
            driver.find_element_by_tag_name("h1")
            y+=1
            block = driver.find_element_by_css_selector("#app-.selected")
            list1 = block.find_elements_by_class_name("name")
    driver.get('http://localhost/litecart/admin/')
    list = driver.find_elements_by_class_name("name")
driver.quit()
