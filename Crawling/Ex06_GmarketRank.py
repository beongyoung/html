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


# In[46]:


url = 'https://corners.gmarket.co.kr/Bestsellers'
driver = wb.Chrome()
driver.get(url)


# In[3]:


img_url = []
img = driver.find_elements(By.CSS_SELECTOR,'img.lazy')
img[0].click()


# In[4]:


soup = bs(driver.page_source,'lxml')
itemName = soup.select_one('h1.itemtit').text
itemPrice = soup.select_one('strong.price_real').text
span = soup.select('span.sp_vipgroup')
for i in span:
    i.extract()
origin = soup.select('li.list-item-origin.uxeslide_item > div.box__information-title > div.box__information')
origin[0].text.strip()


# In[5]:


# 뒤로가기
driver.back()


# In[87]:


img = driver.find_elements(By.CSS_SELECTOR,'img.lazy')

title_list = []
price_list = []
origin_list = []
rank_list = []

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

    title_list.append(itemName)
    price_list.append(itemPrice)
    origin_list.append(origin[0].text.strip())
    
    driver.back()
    time.sleep(0.5)


# In[90]:


rank_list = []
for i in range(10):
    rank_list.append(i+1)
rank_list


# In[91]:


title_list


# In[84]:


price_list


# In[88]:


origin_list


# In[92]:


div = {'상품명' : title_list, '가격' : price_list, '원산지' : origin_list, '랭크' : rank_list}
df = pd.DataFrame(div)
df = df.set_index(['랭크', '가격', '상품명', '원산지'])
df


# ### 카테고리별 수집

# In[47]:


cat = driver.find_elements(By.CSS_SELECTOR,'ul.by-group > li')
len(cat)


# In[48]:


for i in tqdm(range(1,len(cat))):
    cat = driver.find_elements(By.CSS_SELECTOR,'ul.by-group > li')
    cat[i].click()
    time.sleep(0.5)


# In[128]:


url = 'https://corners.gmarket.co.kr/Bestsellers'
driver = wb.Chrome()
driver.get(url)

img = driver.find_elements(By.CSS_SELECTOR,'img.lazy')

title_list = []
price_list = []
origin_list = []
cat_list = []
for category in tqdm(range(1,len(cat))):
    cat = driver.find_elements(By.CSS_SELECTOR,'ul.by-group > li')
    cat[category].click()
    time.sleep(0.5)
    for i in tqdm(range(4)):
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
        cat_list.append(category)
        title_list.append(itemName)
        price_list.append(itemPrice)
        origin_list.append(origin[0].text.strip())

        driver.back()
        time.sleep(0.5)
        
div = {'상품명' : title_list, '가격' : price_list, '원산지' : origin_list, '카테고리' : cat_list}

df = pd.DataFrame(div)
df = df.set_index(['카테고리', '가격', '상품명', '원산지'])
df


# In[130]:


div = {'상품명' : title_list, '가격' : price_list, '원산지' : origin_list, '카테고리' : cat_list}

df = pd.DataFrame(div)
df = df.set_index(['카테고리','가격', '상품명', '원산지'])
df


# In[15]:


url = 'https://www.bbq.co.kr/menu/menuList.asp'
driver = wb.Chrome()
driver.get(url)

list_menu_name = []
list_menu_price = []
list_menu_cat = []
list_menu_no = []

tabs = driver.find_elements(By.CSS_SELECTOR,'ul.menu-tab > li')

for tab in tqdm(range(9)):
    tabs = driver.find_element(by=By.XPATH,value='/html/body/div[5]/div[2]/article/section/div[2]/ul/li[5]/a')
    tabs.click()
    time.sleep(0.3)
    
    soup = bs(driver.page_source,'lxml')
    menu_name = soup.select('p.name')
    menu_price = soup.select('p.pay')
    
    for i in tqdm(range(len(menu_name))):
        menu_name = soup.select('p.name')
        menu_price = soup.select('p.pay')
        list_menu_name.append(menu_name[i].text)
        list_menu_price.append(menu_price[i].text)
        list_menu_no.append(i+1)
        list_menu_cat.append(tab);
    
    driver.back()
    time.sleep(0.3)


# In[16]:


div = {'menu' : list_menu_name, 'price' : list_menu_price, 'category' : list_menu_cat, 'no' : list_menu_no}
df = pd.DataFrame(div)
df.set_index(['category', 'no',  'menu', 'price'])

