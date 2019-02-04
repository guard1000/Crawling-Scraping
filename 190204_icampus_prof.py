from selenium import webdriver
from bs4 import BeautifulSoup

driver =  webdriver.PhantomJS()
driver.get('http://www.icampus.ac.kr/front/main/MainAction.do?method=list')
delay=3
driver.implicitly_wait(delay)

driver.find_element_by_name('uid').send_keys('[아이디]')
driver.find_element_by_name('pwd').send_keys('[비밀번호]')
driver.find_element_by_xpath('//*[@id="mlogin01"]/div/a').click()
driver.implicitly_wait(delay)

driver.get('http://www.icampus.ac.kr/back/login/login.do')
driver.find_element_by_name('uid').send_keys('[아이디]')
driver.find_element_by_name('pwd').send_keys('[비밀번호]')
driver.find_element_by_xpath('//*[@id="main_login"]/table/tbody/tr[1]/td[2]/a').click()

driver.save_screenshot("icampus_prof.png")