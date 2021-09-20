# 学习网址：http://www.python3.vip/tut/auto/selenium/02/

from selenium import webdriver

wd = webdriver.Chrome(r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')

wd.get('http://cdn1.python3.vip/files/selenium/sample1.html')
wd.implicitly_wait(10)# 最大等待时间

# css中\#对应id .对应class 不填对应tag



elements = wd.find_elements_by_css_selector('[href="http://www.miitbeian.gov.cn"]')

for element in elements:
    print('--------')
    print(element.get_attribute('outerHTML'))
    print(element.text)
print('--------')

wd.quit()
pass