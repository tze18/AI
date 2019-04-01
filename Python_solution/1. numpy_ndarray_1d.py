import numpy as np

# region Create ndarray
arr = np.array([1,2,3,4,5,6,7,8,9,10])
print(arr, type(arr), arr[1])   # Note: np array ouput 元素之間沒有逗號  [ 1  2  3  4  5  6  7  8  9 10]

# 常用屬性 shape 很重要 -Tuple
print (arr.dtype, arr.ndim, arr.shape, type(arr.shape))
print(arr.size, arr.itemsize, arr.nbytes)

arr = np.arange(100)
print(arr)

arr = np.arange(1, 101, 2)
print(arr)
print (arr.dtype, arr.ndim, arr.shape, type(arr.shape))
print(arr.size, arr.itemsize, arr.nbytes)

# TODO  陣列元素值 5~49 find the memory size of any array
arr =  np.arange(5, 50)
print (arr)
print(arr.nbytes,  ' bytes')
# or
print(arr.size * arr.itemsize, ' bytes')

arr=np.zeros((10,)) # arr=np.zeros(10)
print (arr)

arr=np.zeros((10,10))
print (arr)

print(np.ones((10,)))
print(np.ones((10,4)))

print(np.full((10,), 99))
print(np.full((10,10), 77))

print(np.full_like(arr, 11))


arr = np.array([True, False, True])
print (arr.dtype, arr.ndim, arr.shape, type(arr.shape))
print(arr.size, arr.itemsize, arr.nbytes)

arr = np.array(['aaa','bbb','ccc'])
print (arr.dtype, arr.ndim, arr.shape, type(arr.shape))
print(arr.size, arr.itemsize, arr.nbytes)

# 陣列的每個元素都會轉成相同資料型態
arr = np.array([1,222,444, False, True]) # 都是 int32
print(arr, arr.dtype)


# endregion

# region arr 數學運算 & 邏輯運算

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

# ndarray 數學運算
print (arr1 + arr2)
print (arr1 - arr2)
print (arr1 * arr2)
print (arr1 / arr2)

print(arr1 * 30.9)
print (arr1 * [30.9,30.9,30.9] ) # broadcast 廣播

arr1 = arr1*2
arr1 *=2
arr1 +=100
print(arr1)

# python 基本比較邏輯運算 and or => output True or False
a= 100
b = 55
print (a > b)
print (a > b and b<=99)
print (a > b or b ==88)

# ndarray 邏輯運算
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
print (arr1 > arr2)

mask = arr1 > arr2
print (mask, type(mask))       # [False False False] <class 'numpy.ndarray'>
print(mask.dtype, mask.shape)

arr = np.array([1,2,3,4,5,6,7,8,9,10])
mask = arr>=8
print (mask)

# ==========================
# 是否是中間級分同學=> True 還是 False
cond1 = arr >=3
cond2 = arr <=8
print(cond1)             # [False False  True  True  True  True  True  True  True  True]
print(cond2)             # [ True  True  True  True  True  True  True  True False False]

mask = (cond1) & (cond2) # [False False  True  True  True  True  True  True False False]
print (mask)

print((arr >=3) & (arr<=8)) # 記得加 小括號 ()

# 是否是高低級分同學
print( (arr<=2) | (arr >=9))
print( ~((arr >=3) & (arr<=8))) 
print (~mask)

# 陣列個元素是否為偶數
print(arr % 2)
print((arr % 2) == 0)

# arr   [ 1      2      3       4    5     6    7       8   9      10]
# mask  [False  True   False  True False  True False  True False  True]
#       [ 2  4  6  8 10]
mask = (arr % 2) == 0
print(arr[mask])
print (arr[arr%2==0])

print(arr[[True, True, True, True, True, False, False, False, False, False]])
# Exception has occurred: IndexError
# boolean index did not match indexed array along dimension 0; dimension is 10 but corresponding boolean dimension is 9
# print(arr[[True, True, True, True, True, False, False, False, False]])


# TODO 陣列個元素是否有2
# arr *=3
print (arr==2)
print(arr[arr==2])
print((arr[arr==2]).size>0)

# TODO 陣列元素 不是2
print (arr[arr!=2])
print (arr[~(arr==2)])

# TODO 球隊人數 > 10
players = [56,  8, 19, 14, 6, 71]   
# print(players > 10)Exception has occurred: TypeError'>' not supported between instances of 'list' and 'int'
# arr = np.array(players)
# print(arr>10)
# endregion

# region arr [ index...] 簡單 陣列選取- int index, slice index

arr = np.array([0,1,2,3,4,5,6,7,8,9])
print (arr[4])
print (arr[1:5]) # 不包括 end
print (arr[:8])  # start 沒寫, start =0
print(arr[1:])   # end 沒寫, 包括 end
print(arr[:]) 

print (arr[::2])
print(arr[1:8:2])    # [start:end:step]
print (arr[-4:])
print (arr[:-1])

# TODO 陣列倒著排 reverse order
# python 的小花招[::-1] 會反序回傳
print (arr[::-1])
print (arr[::-2])

# endregion

# region arr [ index...] 複雜 陣列選取　- fancy index / boolean index

print (arr[[2,4,6]])
print (arr[[0,4,6]])


# TODO 找陣列 > 5 的奇數元素
arr=np.array([22,33,11,2,3,54,6,78,9,99, 999])
mask=(arr>5) & (arr%2==1)
print(mask)
print (arr[mask])
print (arr[(arr>5) & (arr%2==1)])


# TODO 陣列有沒有任何一個元素 > 99 ?
print(arr[arr>99])
print(arr[arr>99].size>0)

# any()
print(np.any(arr>99))
print(np.any(arr>9999))


# TODO 陣列是不是每個元素都 >9 ? all()
print(np.all(arr>9))
print(np.all(arr>1))

# endregion

# region arr view or copy

arr = np.array([1,2,3,4,5,6,7,8,9,10])

# working on view
arr[0] = 100
arr[1:5] = 99
arr[[1,3]] = 77
arr[arr %2==1] = 111

# working on copy
arr2 =arr[0:4].copy()
arr2[0:4] = 999999
print (arr)

# 陣列化 向量化 程式設計
# < 5 變 1000; >= 5 變 2000
arr = np.arange(100)
arr[arr<5] = 1000
arr[arr>=5] = 2000
print(arr)

# Solution 1: np.where()
arr = np.arange(100)
print(np.where(arr<5, 1000, 2000))

# Solution 2: 
arr = np.arange(100)
mask = arr<5
arr[mask]=1000
arr[~mask]=2000
print (arr)

# TODO 學生成績分成 5 級 ...pandas Apply(func)
data = np.random.randint(0, 101, 100)
arr = np.array(data)
print(arr.mean())

print(arr)

arr[arr<60] = 1
arr[(arr>=60) & (arr <70)] = 2
arr[(arr>=70) & (arr <80)] = 3
arr[(arr>=80) & (arr <90)] = 4
arr[(arr>=90)] = 5

print (arr)

# endregion

# region arr Aggregation 彙總  & 排序 

arr = np.array([1,2,3,4,5,6,7,8,9,10])
print ('sum = ', arr.sum())
print (np.sum(arr))

print(arr.max())
print(arr.min())
print(arr.mean())

print(np.median(arr))               # 中位數, 把所有數值由小到大排列後取中間的值
print(np.median([1,2,3,4,5]))

data = np.random.randint(60, 101, 100)
arr = np.array(data)
arr.sort()
print (arr)

# =================
data = np.random.randint(60, 101, 100)
arr = np.array(data)
print(np.sort(arr))

# TODO 學生成績權重的分數
arr = np.array([80,90, 100])
print ((arr * [0.25, 0.25, 0.5]).sum())

# endregion

print('end')