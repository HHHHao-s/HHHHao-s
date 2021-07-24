from selenium import webdriver
from selenium.webdriver.support.ui import Select



wd = webdriver.Chrome(r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe') 
wd.implicitly_wait(10)

wd.get('http://cdn1.python3.vip/files/selenium/test2.html')

# 先把 已经选中的选项全部点击一下
select = Select(wd.find_element_by_id('ss_multi'))

select.deselect_all()

select.select_by_visible_text('小雷老师')
select.select_by_visible_text('小凯老师')

wd.quit()

