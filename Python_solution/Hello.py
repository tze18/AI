# 三大套件
import numpy as np
import pandas as pd
import matplotlib

import sys
print(sys.version_info)
print(sys.version)


# 三大類別
print (np.ndarray)
print (pd.Series)
print(pd.DataFrame)

print(np.__version__)
print(pd.__version__)

# =============================
# list
myList=[33,45,77]
print(myList[0], type(myList))
print(myList)   # [33, 45, 77]

# Exception has occurred: TypeError
# can't multiply sequence by non-int of type 'float'
# print (myList * 30.9) 
# print(myList * 30)  # [33, 45, 77, 33, 45, 77, 33, 45, 77,.....]

list1=[]
for n in myList:
    list1.append(n*30.9)      # 算美金
print(list1)

# ============================
# ndarray
arr = np.array(myList)
print(arr[0], type(arr))
print (arr)     # [33 45 77]
print (arr * 30.9)             # (批次元素運算)(向量化運算); 這門課幾乎不寫loop


# ============================
# 效能測試
myList = list(range(100000000))
arr = np.arange(100000000)

print (len(myList),  myList[0:100])
print (arr.size, arr[0:100])

# print(myList * 30.9)

import time
t1=time.time()
list1=[]
for n in myList:
    list1.append(n*30.9)      # 算美金
t2 = time.time()
print(t2-t1, ' sec')

t1 = time.time()
list2=[n*30.9 for n in myList] # list (串列生成式)
t2 = time.time()
print(t2-t1, ' sec')

t1 = time.time()
arr = arr * 30.9
t2 = time.time()
print(t2-t1, ' sec')

# print (len(list1),  list1[0:100])
# print (arr.size, arr[0:100])

print('end')


