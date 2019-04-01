import numpy as np
import matplotlib.pyplot as plt

# 二維 陣列
# arr [ row, column]

# # 沿著 row 的方向 axis = 0,  沿著column 的方向 axis = 1, 
# axis =0  代表 三個學生
# axis =1, 代表 每個學生 國英數成績


# region Create 2d ndarray
arr = np.array([
                [1,2,3],
                [4,5,6],
                [7,8,9]
                ])
print (arr)
print (arr.ndim, arr.dtype, arr.shape)
print(arr.size, arr.itemsize, arr.nbytes)
print ('number of rows :', arr.shape[0])

print (np.zeros((5,3)))
print (np.ones_like(arr))
print(np.full((10,10), 11))

# (陣列 批次元素運算) (or 陣列向量化運算); 
# 這門課幾乎不寫loop, 把迴圈替換成陣列表達式的動作, 被稱為向量化 (Vectorization)(陣列導向程式設計)
# 相同位置 對齊 做相對運算
print (arr *2)
print (arr ** 2)
print (arr >= 5)
print (arr[arr>=5])

print (arr + arr)
print (arr * arr)

# Universal Functions (ufunc) - 向量化運算
print (arr + arr)
print (np.add(arr,arr)) # 二元 ufunc 
print (np.sin(arr))     # 一元 ufunc 

#endregion

# region 2d ndarray [row, column] 陣列選取
print (arr[1])
print (arr[1,1])

print (arr[0:2, 0:2])
print (arr[:, 0:2])
print (arr[0:2, :])   # for 所有 column

# reverser order
print(arr[::-1, :])
print(arr[::-1, ::-1])

print(arr[[1,2],:])
print(arr[arr>5])

# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]
# TODO 偶數而且>5元素 累加 1000
arr[(arr>5) & (arr%2==0)] += 1000
print(arr)

# endregion

# region 2d ndarray reshape/T
arr1d = np.arange(12)

arr2d= arr1d.reshape((2,6))
print (arr2d)

arr2d= arr1d.reshape((6,2))
print (arr2d)

arr2d= arr1d.reshape((3,4))
print (arr2d)

arr2d= arr1d.reshape((4,3))
print (arr2d)

print (arr2d.T)

# TODO 2d ndarray 周邊 0, 內部 1
arr = np.zeros((10,10))
print(arr)
arr[1:-1,1:-1]= 1
print(arr)


# endregion

# region 2d ndarray 'axis 觀念' 彙總  & 排序

# # 沿著 row 的方向 axis = 0,  沿著column 的方向 axis = 1, 
# axis =0  代表 三個學生
# axis =1, 代表 每個學生 國英數成績


arr = np.array([
                [1,2,3],
                [4,5,6],
                [7,8,9]
                ])

print(arr.sum())            # 預設 axis=none, 所有元素的加總

print (arr.sum(0))
print (arr.sum(axis=0))     # instance method
print (np.sum(arr, axis=0)) # package function

print (arr.sum(1))
print (arr.sum(axis=1))
print (np.sum(arr, axis=1))

print (arr.max(axis=0))
print (arr.max(axis=1))

print (arr.min(axis=0))
print (arr.min(axis=1))

print (arr.mean(axis=0))
print (arr.mean(axis=1))

print (np.median(arr, axis=0))
print (np.median(arr, axis=1))


# sort
arr = np.array([[3,1],
                [1,4]])
              
print (arr.sort(axis=0)) # sort an array in place
print (arr)

# ------------------------------
arr = np.array([[3,1],
                [1,4]])
              
print (arr.sort(axis=1)) # sort an array in place
print (arr)

# endregion

# region numpy random  &  matplotlib plt

# plot(x, y, color='green', marker='o', markersize=12 ,linestyle='dashed', linewidth=2)
# plt.plot(population, color='green', marker='x') # x 沒傳 -> [0,1,2,3....]
# plt.show()

years = np.arange(2002, 2013)
populations= np.random.randint(50, 100, years.shape)

plt.plot(years, populations, color='r')
plt.plot(years, populations * 1.5, color='b')

plt.xlabel('Years')
plt.ylabel('Populations')
plt.title('population / year')
plt.show()

plt.bar(years, populations, color='r')
plt.show()

plt.barh(years, populations, color='r')
plt.show()

plt.pie(populations, labels=years, autopct='%1.1f%%')
plt.show()

# plt.pie(populations, labels=years)
# plt.show()

x = np.random.randn(100)
y = np.random.randn(100)
print (x)
print (y)

plt.scatter(x,y)
plt.show()

plt.scatter(x[x>0], y[x>0],c='r')
plt.scatter(x[x<=0], y[x<=0],c='g')
plt.show()

# TODO scatter y > 0 紅色 
plt.scatter(x[y>0], y[y>0],c='r')
plt.scatter(x[y<=0], y[y<=0],c='g')
plt.show()

# endregion



print('end')

