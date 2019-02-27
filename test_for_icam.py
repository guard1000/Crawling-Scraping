'''
아이캠 자동출책용 Test
이녀석은 일단 공개강의 - 국제어강의학습전략(인문사회과학도 에 들어가서 강좌를 클릭하는 기능

조회수가 +1되고
3초 기다린 후 체크하면, 윈도우 창이 2개 열려있는 것을 확인가능
창을 바꿔주고 스크린샷을 찍으면, 강의 플레이어가 스크린샷에 찍힘
즉, 강의 잘 찾아가서 강의 재생까지 누른 것.
'''

from selenium import webdriver
import time

id = input('아이디 :')
pw = input('패스워드 :')
driver =  webdriver.PhantomJS('C:\\Users\\박천욱\\Downloads\\phantomjs-2.1.1-windows\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe')    #팬텀JS사용. 자신의 팬텀JS위치로 설정하세요

driver.get('http://www.icampus.ac.kr/front/main/MainAction.do?method=list')
delay=3
driver.implicitly_wait(delay)

print('icampus로 로그인합니다.')
driver.find_element_by_name('uid').send_keys(id)
driver.find_element_by_name('pwd').send_keys(pw)
driver.find_element_by_xpath('//*[@id="mlogin01"]/div/a').click()
driver.implicitly_wait(delay)
print('로그인 완료\n\n')

driver.find_element_by_xpath('//*[@id="mainmenu"]/li[3]/span/a').click()    #공개강의로 이동
driver.find_element_by_link_text("국제어강의학습전략(인문사회과학도)").click()  #세부 강의 선택
driver.find_element_by_xpath('//a[img/@src="/images/front/ko/icon_test.gif"]').click()  #강의 재생 클릭

time.sleep(3)
print(len(driver.window_handles))   #창 갯수
driver.switch_to_window(driver.window_handles[-1])  #창 바꾸기
driver.get_window_position(driver.window_handles[-1])
driver.save_screenshot("test_cnt.png")  #스크린샷까지 남겨.

source = driver.page_source
print(source)   #해당 페이지 소스 한번 조회해주기 (그냥 별 의민 없음)


