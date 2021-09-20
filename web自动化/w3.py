from selenium import webdriver


wd = webdriver.Chrome(r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe') 
wd.implicitly_wait(10)

wd.get('http://cdn1.python3.vip/files/selenium/sample3.html')

mainwindow = wd.current_window_handle

# 点击打开新窗口的链接
link = wd.find_element_by_tag_name("a")
link.click()

for handle in wd.window_handles:
    wd.switch_to.window(handle)
    if 'Bing' in wd.title:
        break



# wd.title属性是当前窗口的标题栏 文本
print(wd.title)
wd.switch_to.window(mainwindow)
wd.find_element_by_id('outerbutton').click()
pass