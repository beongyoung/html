#!/usr/bin/env python
# coding: utf-8

# ### Celenium
#     - 웹 페이지를 제어하기 위한 모듈
#     - !pip install selenium
#     - chrome driver설치

# In[1]:


get_ipython().system('pip install selenium')


# In[2]:


from bs4 import BeautifulSoup as bs
# 웹을 통제하기 위한 라이브러리
from selenium import webdriver as wb
# 웹에 키 값을 전달하기 위한 라이브러리
from selenium.webdriver.common.keys import Keys
# select 유형을 정해주는 라이브러리
from selenium.webdriver.common.by import By


# In[26]:


driver = wb.Chrome()
url = "https://www.naver.com/"
driver.get(url)


# ### 검색창 제어

# In[27]:


input_area = driver.find_element(By.CSS_SELECTOR,'#query')
input_area.send_keys('애플페이')


# ### Enter 키 제어

# In[28]:


input_area.send_keys(Keys.ENTER)


# In[12]:


btn = driver.find_element(By.CSS_SELECTOR,'.btn_submit')
btn.click()


# ### 한솥 도시락 메뉴 가져오기

# In[46]:


url = 'https://www.hsd.co.kr/menu/menu_list'
driver = wb.Chrome()
driver.get(url)

for i in range(6):
    try:
        btn = driver.find_element(By.CSS_SELECTOR,'.btn_st04')
        time.sleep(1)
        btn.click()
    except:
        print("End", i)
        break


# ### 시간 제어

# In[30]:


import time


# In[61]:


price = soup.select('div.item-text > strong')


# ### Parsing

# In[73]:


import pandas as pd
soup = bs(driver.page_source, 'lxml')
menu = soup.select('h4.h.fz_03')
price = soup.select('div.item-price > strong')

list_menu = []
list_price = []
list_index = []

for i in range(len(menu)):
    list_menu.append(menu[i].text)
    list_price.append(price[i].text)
    list_index.append(i+1)
    
dic = {'메뉴' : list_menu, '가격' : list_price, '순번' : list_index}

df = pd.DataFrame(dic)
df = df.set_index('순번')
df


# In[74]:


df.to_csv('한솥도시락 메뉴정보.csv', encoding = 'utf-8-sig')

