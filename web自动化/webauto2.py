from selenium import webdriver

wd = webdriver.Chrome(r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
wd.get('http://cdn1.python3.vip/files/selenium/sample2.html')
wd.implicitly_wait(10)

wd.switch_to.frame('frame1')

elements = wd.find_elements_by_css_selector('.plant')

for element in elements:
    print(element.text)

wd.switch_to_default_content()
wd.find_element_by_id('outerbutton').click()


wd.quit()