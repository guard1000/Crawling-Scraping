'''
아이캠 자동출책용 Test
이녀석은 18-2학기 - 네트워크 강좌(강의저장)을  찾아가 클릭하는 기능
어차피 아이캠 출석할때 클릭하는것과 같은 메커니즘이므로, 개강하면 아이캠으로 테스트

날짜별로 강의파일이 올라올때 이름이 달라지므로, 그걸로 판단해서 이번주에 들어야 할 강의를 재생
'''

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup


id = input('아이디 :')
pw = input('패스워드 :')
driver =  webdriver.PhantomJS('C:\\Users\\박천욱\\Downloads\\phantomjs-2.1.1-windows\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe')    #팬텀소환. 주소는 자신의phantomjs 절대주소로 바꾸세요

driver.get('http://www.icampus.ac.kr/front/main/MainAction.do?method=list')
delay=3
driver.implicitly_wait(delay)

print('icampus로 로그인합니다.')
driver.find_element_by_name('uid').send_keys(id)
driver.find_element_by_name('pwd').send_keys(pw)
driver.find_element_by_xpath('//*[@id="mlogin01"]/div/a').click()
driver.implicitly_wait(delay)
print('로그인 완료\n\n')

#test용 2학기로 가보자. 학기도 바꿀 수 있다. 인덱스 기준으로 다른 학기 조회 가능
driver.find_element_by_xpath('//*[@id="mlogin02"]/div/p[3]/select/option[3]').click()

print('수강과목 조회')
driver.find_element_by_xpath('//*[@id="mlogin02"]/ul/li[1]/a/img').click()  #수강과목 버튼을 id기준으로 찾아내 클릭한다.

#컴퓨터네트워크 클릭
driver.find_element_by_link_text("컴퓨터네트워크").click() #강좌 이름은 짜피 고유값을 가지므로 이름으로 찾아도 된다.

#수업 클릭. 여기부턴 개발자도구로 HTML 분석이 안되므로, driver.page_source로 페이지를 가져와서 직접 보면서 들어가자
#driver.find_element_by_xpath("//a[contains(@onclick, '2827784')]").click()  #공지사항으로 넘어가보기 -> 제대로 클릭이 작동한다.
driver.find_element_by_xpath("//a[contains(@onclick, '0907')]").click()  #9월7일강의로 넘어간다. 교수님이 아이캠에 업로드한 날짜 시간 분 초 까지 다 나온다. 이거 기준으로 찾으면 댐
time.sleep(3)
print(len(driver.window_handles))   #창 몇개인지 -> 그냥 팝업 뜨나확인용
#driver.switch_to_window(driver.window_handles[1])  #창 바꾸기. 이것도 확인용
#driver.get_window_position(driver.window_handles[1])

driver.implicitly_wait(delay)

source = driver.page_source #페이지 소스 분석용
print(source)   #그냥 지금 페이지 확인용

driver.save_screenshot("icampus_student.png") # 잘 되었나 스크린샷을 남겨보자.