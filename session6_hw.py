from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import csv
from selenium.webdriver.common.action_chains import ActionChains


# 디버깅 모드
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

chrome_driver = "C:/Users/hanny/OneDrive/바탕 화면/NEXT/Session6/chromedriver.exe"
driver = webdriver.Chrome(chrome_driver, options= chrome_options)


# 실행할 웹페이지 불러오기 (네이버 영화)
driver.get("https://movie.naver.com/")

time.sleep(2)

#네이버 영화 차트 버튼 클릭
chartbtn = driver.find_element(By.XPATH, '//*[@id="scrollbar"]/div[1]/div/div/ul/li[3]/a')
chartbtn.click()

time.sleep(8)

#1위부터 20위 이름 가져오기
for i in range(2,11):
    titles = driver.find_element(By.XPATH, f'/html/body/div/div[4]/div/div/div/div/div[1]/table/tbody/tr[{i}]/td[2]/div/a').text
    print(titles)

time.sleep(8)

#각 영화 클릭
moviebtn = driver.find_element(By.XPATH,'//*[@id="old_content"]/table/tbody/tr[2]/td[2]/div/a')
moviebtn.click()

time.sleep(2)



#개요, 감독, 평점
a = driver.find_element(By.XPATH,'//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[1]/p/span[1]/a[1]').text
print("개요: ", a)
time.sleep(2)
b = driver.find_element(By.XPATH,'//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[2]/p/a').text
print("감독: ", b)
time.sleep(2)
c = driver.find_element(By.XPATH,'//*[@id="actualPointPersentBasic"]/div/span/span').text
print(c)



#좋아하는 영화 검색
searchbox = driver.find_element(By.XPATH, '//*[@id="ipt_tx_srch"]')
time.sleep(10)
searchbox.send_keys("마음이2")
time.sleep(5)
searchbox.send_keys(Keys.ENTER)
time.sleep(2)

heartbtn = driver.find_element(By.XPATH,'//*[@id="old_content"]/ul[2]/li[1]/dl/dt/a/strong[1]')
heartbtn.click()
time.sleep(2)

# 제목, 감독, 스크롤 내려서 평점 + 리뷰 개수
hearttitle = driver.find_element(By.XPATH,'//*[@id="content"]/div[1]/div[2]/div[1]/h3/a').text
heartdtr = driver.find_element(By.XPATH,'//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[2]/p/a').text
time.sleep(2)

driver.find_element(By.TAG_NAME,'body').send_keys(Keys.PAGE_DOWN)
time.sleep(2)
driver.find_element(By.TAG_NAME,'body').send_keys(Keys.PAGE_DOWN)
time.sleep(2)
driver.find_element(By.TAG_NAME,'body').send_keys(Keys.PAGE_DOWN)
time.sleep(2)

heartscore = driver.find_element(By.XPATH,'//*[@id="content"]/div[1]/div[4]/div[5]/div[2]/div[2]/div[1]/div/div/em').text

heartreview = driver.find_element(By.XPATH,'//*[@id="content"]/div[1]/div[4]/div[5]/div[2]/div[3]/strong/em').text
time.sleep(2)

print("제목: ", hearttitle)
print("감독: ",heartdtr)
print("평점: ", heartscore)
print("리뷰 개수: ", heartreview)


time.sleep(5)

# csv 파일로 저장

file = open('movies.csv', mode="w", newline='')
writer = csv.writer(file)
writer.writerow(["hearttitle","heartdtr","heartscore","heartreview"])

writer.writerow([hearttitle,heartdtr,heartscore,heartreview])



file.close()

time.sleep(2)
