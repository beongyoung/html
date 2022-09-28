#!/usr/bin/env python
# coding: utf-8

# In[3]:


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
# 이미지 경로를 파일로 저장
from urllib.request import urlretrieve

# python progress bar library
from tqdm import tqdm


# ### Image 크롤링

# In[5]:


url = 'https://search.naver.com/search.naver?sm=tab_hty.top&where=image&query=%EC%95%84%EC%9D%B4%EC%9C%A0&oquery=The+golden+hour&tqi=hzMgPlp0J1ZssmETXCssssssshs-103445'
driver = wb.Chrome()
driver.get(url)


# In[83]:


body = driver.find_element(By.CSS_SELECTOR,'body')
for i in range(20):
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.3)


# In[27]:


if(not os.path.isdir('./image')):
    print("Folder Created!")
    os.mkdir('./image')


# In[6]:


img_src = []
soup = bs(driver.page_source,'lxml')
img = soup.select('img._image._listImage')

for i in img:
    try:
        img_src.append(i['data-lazy-src'])
    except:
        img_src.append(i['src'])
len(img_src)


# In[7]:


# 저장할 이미지 경로, 저장할 위치 및 파일명

#리스트에 있는 원소만큼 반복, 인덱스는 index에, 원소들은 link를 통해 접근 가능
for i in tqdm(range(len(img_src))):
    #link에서 이미지 다운로드, './image/'에 파일명은 index와 확장자명으로
    urlretrieve(img_src[i], './image/{}{}'.format(i+1, '.jpg'))
    time.sleep(0.3)


# In[99]:


if(not os.path.isdir('./hansotImg')):
    print("Folder Created!")
    os.mkdir('./hansotImg')


# In[102]:


url = 'https://www.hsd.co.kr/menu/menu_list'
driver = wb.Chrome()
driver.get(url)


# In[104]:


body = driver.find_element(By.CSS_SELECTOR,'body')
for i in range(6):
    try:
        btn = driver.find_element(By.CSS_SELECTOR,'.btn_st04')
        time.sleep(1)
        btn.click()
    except:
        print("End", i)
        break


# In[119]:


hansot_src = []
soup = bs(driver.page_source, 'lxml')
img = soup.select('div.item-img > img')
menu = soup.select('h4.h.fz_03')

for i in img:
    try:
        hansot_src.append(i['data-lazy-src'])
    except:
        hansot_src.append(i['src'])

# 저장할 이미지 경로, 저장할 위치 및 파일명

#리스트에 있는 원소만큼 반복, 인덱스는 index에, 원소들은 link를 통해 접근 가능
for i in tqdm(range(len(hansot_src))):
    #link에서 이미지 다운로드, './image/'에 파일명은 index와 확장자명으로
    urlretrieve(hansot_src[i], './hansotImg/{}{}'.format(menu[i].text, '.jpg'))
    time.sleep(0.3)

