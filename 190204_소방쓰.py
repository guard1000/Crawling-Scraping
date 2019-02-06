from selenium import webdriver
from bs4 import BeautifulSoup

driver =  webdriver.PhantomJS()
driver.get('http://www.nfds.go.kr/fr_base_0001.jsf')
delay =2

driver.implicitly_wait(delay)
driver.find_element_by_xpath("//option[@value='11']").click()
driver.find_element_by_xpath("//option[@value='110']").click()
driver.find_element_by_xpath('//*[@id="content-area"]/div[2]/div[2]/form/table/tbody/tr/td[3]/input').click()

#driver.save_screenshot("소방.png")
#print('캡처 완료')