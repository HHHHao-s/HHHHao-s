from selenium import webdriver


driver = webdriver.Chrome(r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
driver.implicitly_wait(5)
driver.get('http://cdn1.python3.vip/files/selenium/test4.html')


# --- prompt ---
driver.find_element_by_id('b3').click()

# 获取 alert 对象
alert = driver.switch_to.alert

# 打印 弹出框 提示信息
print(alert.text)

# 输入信息，并且点击 OK 按钮 提交
alert.send_keys('web自动化 - selenium')
alert.accept()

# 点击 Cancel 按钮 取消
driver.find_element_by_id('b3').click()
alert = driver.switch_to.alert
alert.dismiss()


driver.quit()