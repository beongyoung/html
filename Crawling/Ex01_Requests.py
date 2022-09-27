#!/usr/bin/env python
# coding: utf-8

# ### Requests 사용법
#     - html의 모든 정보를 가져온다

# In[1]:


# 서버에 페이지 정보를 요청할때 사용하는 라이브러리
import requests as req


# In[4]:


url = "https://www.naver.com"
res = req.get(url)
# <Response [200]> : 요청 성공


# In[7]:


# 페이지 정보 확인
res.text


# ### BeautifulSoup 사용법
#     - 원하는 컨텐츠만 추출할때 사용

# In[8]:


from bs4 import BeautifulSoup as bs


# In[28]:


# Beautiful Soup 라이브러이에서 사용할 수 있도록 Parsing
# bs(parsedata, way of parse)
soup = bs(res.text,'lxml')


# In[27]:


result = soup.select("a.nav")


# In[33]:


for contents in result:
    print(contents.text, end = " ")


# In[42]:


url = "https://www.melon.com/index.htm"
res = req.get(url)
# <Response [406]> : 요청 실패


# In[44]:


# 컴퓨터가 아닌 사람으로 속이는 작업
h = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}


# In[91]:


url = "https://www.melon.com/index.htm"
res = req.get(url, headers = h)
soup = bs(res.text,'lxml')
soup.select("span.menu_bg")


# In[155]:


url = "https://www.melon.com/chart/index.htm"
res = req.get(url, headers = h)
soup = bs(res.text, 'lxml')
# 자식선택자 이용(>)
title = soup.select("div.ellipsis.rank01 > span > a")
# nth-child (몇번째 자식을 가져올 것인지?)
singer = soup.select("div.ellipsis.rank02 > span > a:nth-child(1)")


# In[161]:


listTitle = []
listSinger = []
listRank = []

for i in range(len(title)):
    listTitle.append(title[i].text)
    listSinger.append(singer[i].text)
    listRank.append(i+1);


# In[165]:


import pandas as pd


# In[177]:


dic = {'노래제목' : listTitle, '가수' : listSinger, '순위' : listRank}
df = pd.DataFrame(dic)
# df.set_index = 실제 영향을 주지 않음 -> 다시 이를 집어넣으면 영향을 줌
df = df.set_index('순위')
df

