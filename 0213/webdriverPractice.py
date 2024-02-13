from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.microsoft import  EdgeChromiumDriverManager
# EdgeChromiumDriverManager.install()
driver = webdriver.Edge()
driver.get('https://www.naver.com')
# driver.fullscreen_window()
# print(driver.title)
sleep(3)
driver.implicitly_wait(time_to_wait=5)
print(driver.current_url)
print(driver.title)
webpage = driver.page_source

driver.find_elements(By.NAME, 'link_login')
driver.close() #하나의 탭만 종료
driver.quit() #전체 탭을 종료