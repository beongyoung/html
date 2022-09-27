#!/usr/bin/env python
# coding: utf-8

# In[45]:


from bs4 import BeautifulSoup as bs
# 웹을 통제하기 위한 라이브러리
from selenium import webdriver as wb
# 웹에 키 값을 전달하기 위한 라이브러리
from selenium.webdriver.common.keys import Keys
# select 유형을 정해주는 라이브러리
from selenium.webdriver.common.by import By
import time
# pandas 라이브러리
import pandas as pd


# In[41]:


url = 'https://www.youtube.com/c/dlwlrma/videos'
driver = wb.Chrome()
driver.get(url)


# In[53]:


body = driver.find_element(By.CSS_SELECTOR, 'body')
for i in range(15):
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.3)


# In[84]:


list_title = []
list_view = []
list_range = []
list_date = []

soup = bs(driver.page_source, 'lxml')

title = soup.select('a.yt-simple-endpoint.style-scope.ytd-grid-video-renderer')
view = soup.select('span.style-scope.ytd-grid-video-renderer:nth-child(1)')
date = soup.select('span.style-scope.ytd-grid-video-renderer:nth-child(2)')

for i in range(len(title)):
    list_title.append(title[i].text)
    list_view.append(view[i].text.strip('조회수 '))
    list_date.append(date[i].text)
    list_range.append(i+1)
    
div = {'제목' : list_title, '조회수' : list_view, '순번' : list_range, '날짜' : list_date}
df = pd.DataFrame(div)
df = df.set_index('순번')
df


# In[85]:


df.to_csv('아이유 채널 영상 정보.csv', encoding = 'utf-8-sig')

