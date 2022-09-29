#!/usr/bin/env python
# coding: utf-8

# In[1]:


# python progress bar library
from tqdm import tqdm

# requests 라이브러리
import requests as req
# BeautifulSoup 라이브러리
from bs4 import BeautifulSoup as bs

# 웹을 통제하기 위한 라이브러리
from selenium import webdriver as wb
# 웹에 키 값을 전달하기 위한 라이브러리
from selenium.webdriver.common.keys import Keys
# select 유형을 정해주는 라이브러리
from selenium.webdriver.common.by import By

# 시간 제어를 위한 라이브러리
import time

# pandas 라이브러리
import pandas as pd

# 파일 시스텡을 위한 라이브러리 (파일, 폴더의 생성, 삭제 존재여부 파악)
import os

# url 동작에 관여하는 라이브러리
import urllib

# 이미지 경로를 파일로 저장
from urllib.request import urlretrieve


# In[2]:


# Question 2. 크롤링을 검색하고 화면을 띄우는 코드
url = 'https://www.naver.com'
driver = wb.Chrome()
driver.get(url)

input_area = driver.find_element(By.CSS_SELECTOR,'#query')
input_area.send_keys('크롤링')

btn = driver.find_element(By.CSS_SELECTOR,'.btn_submit')
btn.click()


# In[3]:


# Question 3. 크롤링으로 G마켓 1~10위의 품목 가져오기
list_item_name = []
list_item_price = []
list_item_origin = []
list_item_index = []
for i in tqdm(range(1,11)):
    list_item_index.append(i)
url = 'https://corners.gmarket.co.kr/Bestsellers'
driver = wb.Chrome()
driver.get(url)

img = driver.find_elements(By.CSS_SELECTOR,'img.lazy')
for i in tqdm(range(10)):
    img = driver.find_elements(By.CSS_SELECTOR,'img.lazy')
    img[i].click()
    time.sleep(0.5)
    
    soup = bs(driver.page_source,'lxml')
    itemName = soup.select_one('h1.itemtit').text
    itemPrice = soup.select_one('strong.price_real').text
    span = soup.select('span.sp_vipgroup')
    
    for i in span:
        i.extract()
    origin = soup.select('li.list-item-origin.uxeslide_item > div.box__information-title > div.box__information')

    list_item_name.append(itemName)
    list_item_price.append(itemPrice)
    list_item_origin.append(origin[0].text.strip())
    
    driver.back()
    time.sleep(0.5)


# In[4]:


# Question 3. pandas의 DataFrame형태로 결과를 출력하여야 한다. 컬럼명은 상품명, 가격, 인덱스번호는 1부터 시작 
div = {'상품명' : list_item_name, '가격' : list_item_price, '인덱스번호':list_item_index}
df = pd.DataFrame(div)
df = df.set_index('인덱스번호')
df.to_csv('지마켓_정보.csv', encoding = 'utf-8-sig')
df


# In[5]:


# Question 4.네티즌평점에서 1페이지부터 10페이지까지 영화명와 리뷰를 가져오는 프로그램을 작성하시오.
list_title = []
list_review = []
list_range = []
list_page = []

for page in range(1,11):
    url = "https://movie.naver.com/movie/point/af/list.naver?&page="+str(page)
    res = req.get(url)
    soup = bs(res.text)

    review_title = soup.select("a.movie.color_b")
    # 태그 삭제
    title = soup.select('a.movie.color_b')
    report = soup.select('a.report')
    d1 = soup.select('div.list_netizen_score>span')
    d2 = soup.select('div.list_netizen_score>em')
    
    review_body = soup.select('td.title')
    
    for i in range(len(title)):
        title[i].extract()
        report[i].extract()
        d1[i].extract()
        d2[i].extract()

    for i in range(len(title)):
        list_title.append(title[i].text)
        list_review.append(review_body[i].text.strip())
        list_range.append(i+1)
        list_page.append(page)

dic = {'페이지' : list_page, '영화제목' : list_title, '리뷰' : list_review, '순번' : list_range}
dic

df = pd.DataFrame(dic)
df = df.set_index(['페이지','순번', '영화제목', '리뷰'])
df

df.to_csv('영화리뷰.csv', encoding = 'utf-8-sig')


# In[6]:


# Question 5. 각 상품별 이미지데이터와 상품을 클릭하여 들어가 상품명, 열량, 단백질 수치값을 수집하시오.
url = 'https://www.bbq.co.kr/menu/menuList.asp'
driver = wb.Chrome()
driver.get(url)

img_src = []
list_menu_name = []
list_menu_cal = []
list_menu_protein = []
list_menu_no = []

img = driver.find_elements(By.CSS_SELECTOR,'div.img')

for menu in tqdm(range(12)):
    img = driver.find_elements(By.CSS_SELECTOR,'div.img')
    img[menu].click()
    time.sleep(0.5)
    
    soup = bs(driver.page_source,'lxml')
    menuName = soup.select('div.info > h3')
    menuCal = soup.select('li.circle1 > p')
    menuPro = soup.select('li.circle3 > p')
    
    for i in range(len(menuName)):
        list_menu_name.append(menuName[i].text)
        list_menu_cal.append(menuCal[i].text)
        list_menu_protein.append(menuPro[i].text)
        list_menu_no.append(menu+1)
    img = soup.select('img.jackInTheBox')
    for i in img:
        try:
            img_src.append(i['data-lazy-src'])
        except:
            img_src.append(i['src'])

    driver.back()
    time.sleep(0.5)


# In[7]:


# Question 5. DataFrame 생성 및 csv 파일로 추출
div = {'상품명' : list_menu_name, '열량' : list_menu_cal, '단백질' : list_menu_protein, '순번' : list_menu_no}
df = pd.DataFrame(div)
df = df.set_index(['순번', '상품명', '열량', '단백질'])
df.to_csv('bbq신메뉴.csv', encoding = 'utf-8-sig')
df


# In[8]:


# 이미지 3 폴더 생성 후 이미지 저장
if(not os.path.isdir('./이미지3')):
    print("Folder Created!")
    os.mkdir('./이미지3')
    
for i in tqdm(range(len(img_src))):
    #link에서 이미지 다운로드, './image/'에 파일명은 index와 확장자명으로
    urlretrieve(urllib.parse.quote(img_src[i],safe=':/?-='),'./이미지3/{}{}'.format(list_menu_name[i], '.jpg'))
    time.sleep(0.3)

