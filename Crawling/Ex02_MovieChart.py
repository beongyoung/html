#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests as req
url = "https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=cur&date=20220925"
res = req.get(url)

from bs4 import BeautifulSoup as bs
soup = bs(res.text, 'lxml')
movieTitle = soup.select('div.tit5 > a')
rate = soup.select('td.point')


# In[2]:


import pandas as pd
listTitle = []
listRank = []
listRate = []
for i in range(len(movieTitle)):
    listTitle.append(movieTitle[i].text)
    listRate.append(rate[i].text)
    listRank.append(i+1)

dic = {'영화제목' : listTitle, '평점' : listRate, '순위' : listRank}
dic

df = pd.DataFrame(dic)
df = df.set_index('순위')
df


# ### 다른 페이지 정보 수집

# In[20]:


listTitle = []
listRank = []
listRate = []
listDate = []
    
for date in range(20220901, 20220926):
    url = "https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=cur&date=" + str(date)
    res = req.get(url)
    soup = bs(res.text, 'lxml')
    
    title = soup.select('div.tit5 > a')
    rate = soup.select('td.point')
    
    for i in range(len(title)):
        listTitle.append(title[i].text)
        listRate.append(rate[i].text)
        listRank.append(i+1)
        listDate.append(date)


# In[21]:


dic = {'영화제목' : listTitle, '평점' : listRate, '순위' : listRank, '날짜' : listDate}
df = pd.DataFrame(dic)
df = df.set_index('순위')
df


# In[22]:


df[df['날짜'] == 20220920]


# In[38]:


from tqdm import tqdm_notebook # 반복문 진행사항 확인 할 수 있는 라이브러리


# In[39]:


listTitle = []
listRank = []
listRate = []
listDate = []

# pandas 날짜 생성
date = pd.date_range(start = '2022-01-01', end = '2022-09-25')

# 문자열 formatting
days = date.strftime('%Y%m%d')

for day in tqdm_notebook(days):
    url = "https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=cur&date=" + day
    res = req.get(url)
    soup = bs(res.text, 'lxml')
    
    title = soup.select('div.tit5 > a')
    rate = soup.select('td.point')
    
    for i in range(len(title)):
        listTitle.append(title[i].text)
        listRate.append(rate[i].text)
        listRank.append(i+1)
        listDate.append(day)


# In[24]:


dic = {'영화제목' : listTitle, '평점' : listRate, '순위' : listRank, '날짜' : listDate}
df = pd.DataFrame(dic)
df = df.set_index('순위')
df


# In[37]:


df[df['날짜'] == '20220101']


# ### 평점 리뷰 가져오기

# In[67]:


import requests as req
import pandas as pd
from bs4 import BeautifulSoup as bs

list_title = []
list_review = []
list_range = []
list_page = []

for page in range(1,101):
    url = "https://movie.naver.com/movie/point/af/list.naver?&page="+str(page)
    res = req.get(url)
    soup = bs(res.text)

    review_title = soup.select("a.movie.color_b")

    # 태그 삭제
    title = soup.select('a.movie.color_b')
    report = soup.select('a.report')
    d1 = soup.select('div.list_netizen_score>span')
    d2 = soup.select('div.list_netizen_score>em')
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

dic = {'페이지' : list_page, '리뷰제목' : list_title, '리뷰' : list_review, '순번' : list_range}
dic

df = pd.DataFrame(dic)
df = df.set_index('순번')
df[df['페이지'] == 3]

