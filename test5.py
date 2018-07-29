from selenium import webdriver


driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('http://localhost/litecart/')
list = driver.find_elements_by_css_selector("li.product.column.shadow.hover-light")
form = list[0]
form.find_element_by_css_selector("[class*=sticker]")
form = list[1]
form.find_element_by_css_selector("[class*=sticker]")
form = list[2]
form.find_element_by_css_selector("[class*=sticker]")
form = list[3]
form.find_element_by_css_selector("[class*=sticker]")
form = list[4]
form.find_element_by_css_selector("[class*=sticker]")
form = list[5]
form.find_element_by_css_selector("[class*=sticker]")
form = list[6]
form.find_element_by_css_selector("[class*=sticker]")
form = list[7]
form.find_element_by_css_selector("[class*=sticker]")
form = list[8]
form.find_element_by_css_selector("[class*=sticker]")
form = list[9]
form.find_element_by_css_selector("[class*=sticker]")
form = list[10]
form.find_element_by_css_selector("[class*=sticker]")
driver.quit()
