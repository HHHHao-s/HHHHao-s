from selenium import webdriver


driver = webdriver.Chrome(r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
driver.implicitly_wait(5)
driver.get('http://cdn1.python3.vip/files/selenium/test1.html')

elements = driver.find_elements_by_xpath('/html/body/div/p')

for element in elements:
    print(element.text)