# # 라이브러리 (Library)
#   -> Numberical Python의 약자

# # numpy.ndarray = array

# In[1]:


import numpy as np
import numpy.random as rd
np.add(1,2)


# In[2]:


list1 = [0,1,2,3,4]
list1


# In[3]:


# np.array(리스트명)
# 리스트 생성 후 np.array(list)
np.array(list1)


# In[4]:


arr1 = np.array([1,3,5,7,9])


# In[5]:


#ndarray 생성
arr2 = np.array([ [1,2,3],
          [4,5,6] ])


# In[6]:


arr2.shape


# In[7]:


# 배열의 전체 요소 확인
# array.size
arr1.size
arr2.size


# In[8]:


# 배열의 타입 화인
arr1.dtype
print(arr2.dtype)


# In[9]:


# 배열 차원확인하기
# n차원(n dimention)
arr2.ndim


# In[10]:


arr3 = np.array([
    [ [1, 2], [3, 4] ],
    [ [5, 6], [7, 8] ]
])
print(f"배열의 크기 : {arr3.shape}")
print(f"배열의 차원 : {arr3.ndim}")
print(f"배열의 개수 : {arr3.size}")


# In[11]:


# np.zeros() : 0값으로 초기화
np.zeros((2,3))


# In[12]:


np.ones((3,4))


# In[13]:


# 특정한 값으로 배열 생성
# np.full((행, 열), 숫자)
np.full((5,5),7)


# In[14]:


list_num = []
for i in range (1,51):
    list_num.append(i)


# In[15]:


arr_list = np.array(list_num)
print(arr_list)


# In[16]:


arr_np = np.arange(1,51)
print(arr_np)


# In[17]:


# np.random.rand(행, 열)
# rand의 특징 : 0 ~ 1 사이의 값을 랜덤 추출
rd.rand(1,2)


# In[18]:


rd.randint(1,20)


# In[19]:


# type 지정해서 배열 생성하는 방법!
np.array([1.2, 2.3, 3.4], dtype = np.int64)


# In[20]:


list1 = [1.2, 1.5, 4.3]
np.array(list1, int)


# In[21]:


# array 연산
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr3 = arr1 + arr2
print(arr3)


# In[22]:


# list 연산
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1 + list2


# In[23]:


arr2_a = np.array([[1,2, 3], [4, 5, 6]])
arr2_b = np.array([[1,2, 3], [4, 5, 6]])
arr2_c = arr2_a + arr2_b
print(arr2_c)


# In[24]:


arr2_c + 3


# ## Numpy 인덱싱 & 슬라이싱
# #### 인덱싱 : 무엇인가를 '가르킨다'는 의미
# #### 슬라이싱 : 무엇인가를 '잘라낸다'는 의미

# In[25]:


arr2_a[0]


# In[29]:


# 1차원의 array 생성
arr = np.arange(10)
arr


# In[33]:


arr[3:8]


# In[41]:


arr_2 = np.arange(50).reshape(5,10)
arr_2


# In[48]:


arr_2[0:2]


# In[50]:


arr_2[0:4, 0:5]


# In[61]:


# delimiter : 구분기호
data = np.loadtxt("height_weight(p).txt",delimiter=",")
data


# In[88]:


# pound to kg
arr_weight = data[1] / 2.204
arr_height = data[0] / 100

# BMI = weight / height**2
arr_bmi = arr_weight / arr_height ** 2
arr_bmi


# # Boolean Indexing
# ### -> 배열 안에서 조건을 충족하는 True인 값들만 추출해주는 인덱싱 방법

# In[89]:


s = "안녕"
s[0]


# In[97]:


score = np.array([60, 75, 55, 96, 30])
# 60점 이상인 것들의 점수 추출
score[score >= 60]


# In[98]:


name = np.array(["1", "2", "3", "4"])
name


# In[99]:


# true false -> boolean data
bol = np.array([False, True, True, False])
bol


# In[100]:


name[bol]


# In[102]:


score = np.array([[60, 60], [70, 70], [80, 80], [90, 90]])
score


# 

# In[104]:


name[name=="1"]


# In[114]:


# sum()
arr = rd.randint(1,10, size = (2,5))
print(f"{arr}의 합계 : {np.sum(arr)}")


# In[120]:


import math
math.sqrt(np.sum(arr))
np.abs(-20)


# ![image.png](attachment:image.png)

# ![image.png](attachment:image.png)
