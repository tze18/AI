import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# region Create Series

# Series - 有 label 標籤索引   的 一維  ndarray 

# 位置索引 (int index)               index 可以是  0,1,2 .. (預設)   
# 標籤索引 (label index)             index 可以是 'a', 'b'... (index 可重複)

series1 = pd.Series([11,22,33])
print(series1)
print(series1.index)
print(series1.values, type(series1.values))
print(series1.ndim, series1.shape)

series1.index.name='id'
series1.name='Chi'
print(series1)

series1 = pd.Series([80,90, 100], index=['a','b','c'], name='Chi Scores')
print(series1)
# a     80
# b     90
# c    100
# Name: Chi Scores, dtype: int64

print(series1*2)
print(series1 >= 90)
print(series1[series1>=90])


series2 = pd.Series([80,70, 100,99], index=['a','b','c','d'], name='Eng Scores')
print(series1 + series2)

#endregion

# region Series index [ ] 篩選資料
series1 = pd.Series([80,90, 100], index=['a','b','c'])
print(series1['a'], series1[0]) # 直接索引[]  OK

# 直接索引[] confuse
series1 =  pd.Series([80,70, 100,99], index=[5,6,0,3])
print(series1[0])


# 
# iloc -int positional indexing 位置索引 (一定是 int 整數用) ; iloc[]  interger by location :
# loc - label indexing          標籤索引 (          標籤用)
series1 = pd.Series(np.arange(10), index=list('abcdefghij'))
print(series1)

print(series1.iloc[3])
print(series1.iloc[3:7])
print(series1.iloc[[0,3,5]])

print(series1.loc['a'])
print(series1.loc['a':'f'])
print(series1.loc[['a','b','f']])

# TODO  測驗回答以下 series 有幾個元素
s1 = pd.Series( np.arange(10), index=[2,3,1,6,7,8,9,10,11,5])
print(s1)
print(s1.iloc[:3]) 
print(s1.loc[:3])

print(series1.loc[series1%2==0])
print(series1.loc[series1>5])
print(series1[series1>5])      # 直接索引 OK, for boolean index
print(series1.a)               # 動態屬性
print(series1.d)               # 動態屬性


def myfunc(s):
    # ..............
    return (s>5) & (s<8)
print(series1.loc[myfunc])                        # 具名方法 function
print(series1.loc[lambda s: (s>5) & (s<8) ])     # 匿名方法 function

# iat /at - for scalar value
# print(series1.iat[0])
# print(series1.at['a'])

# endregion

# region Series apply() map()
series1=pd.Series([1,2,3,4,5,6,7,8,9,10])

def myfunc(x):
    # if x %2==0:
    #     return 'Even'
    # else :
    #     return 'Odd'
    return 'Even' if x%2==0 else 'Odd'

print(series1.apply(myfunc))
print(series1.apply(lambda x:'Even' if x%2==0 else 'Odd' ))

# NOTE apply 沒有 inplace, 是回傳apply後的 series
# series1 = series1.apply(myfunc)
# print(series1)

# TODO  value>3 *30 else *3
series1=pd.Series([1,2,3,4,5,6,7,8,9,10])
print(series1.apply(lambda x:  x*30 if x>3 else x*3 ))

# TODO apply => ABCDE => cut()
def myfunc(value):
    # logic .................
   if (value<60):
       grade= 'E'
   elif (value<70):
      grade='D'
   elif (value<80):
       grade= 'C'   
   elif (value<90):
       grade= 'B'
   else:
      grade='A'   
   return '{0} ({1})'.format(value, grade) 

series1 = pd.Series( np.random.randint(60, 101, 100))
print(series1)
print(series1.apply(myfunc))

print(series1.apply(np.sin))
print(series1.apply(np.sin).apply)

series1 = pd.Series(['Female','Male', 'Female'])
print(series1)
print(series1.map({'Female':0, 'Male':1}))


# endregion

# region Series CRUD

series1 = pd.Series([1,2,3,4], index=['a','b','c','d'])
print(series1)

# 新增 工作不存在的 index 就是新增; 否則就是修改 
series1['e'] = 100

# 修改
series1['c'] = 100
series1.loc['c'] = 200

series1.iloc[0:2] = 88


# 刪除
result = series1.drop('a', inplace=False)
series1.drop(['b','c'], inplace=True)

# OK del
del series1['d']

print(series1)

# TODO 小測驗 偶數累加 100
series1 = pd.Series([1,2,3,4], index=['a','b','c','d'])
#series1.loc[series1%2==0] +=100
series1[series1%2==0] += 100   # OK
print(series1)

# endregion

# region Series 彙總  & 排序
series1=pd.Series([np.nan,  1,2,3,3, 4,4 ,4,5,6,7,8,3, 9,10])
print('sum = ',series1.sum())
print(series1.min())
print(series1.max())
print(series1.mean())
print(series1.median())

print(series1.mode()) # 眾數, 出現最多次數的資料

# 最高和最低差多少 (統計 全距)
print(series1.max()-series1.min())

print (series1.describe()) # 四分位數（Quartile）是統計學中分位數的一種，即把所有數值由小到大排列並分成四等份，
print(series1.shape[0], series1.size, series1.count()) # size - 包括 nan; count() 不包括 nan

# (10,)
# [22,33]
data = np.random.randint(1000, 5000, 1000)
series1 = pd.Series(data, index=pd.date_range('1/1/2000', periods=1000))
print(series1)

series1.sort_values(ascending=False, inplace=True)
print(series1)

series1.sort_values(ascending=True, inplace=True)
print(series1)

result = series1.sort_values(ascending=False)
print(result)


series1.sort_index(ascending=False, inplace=True)
print(series1)

print(type(series1.index))
print(series1.index.year)
print(series1.index.month)


# TODO 所有銷售紀錄中, 最高銷售紀錄前 5 筆 ? 最低銷售紀錄 5 筆 ? 
print(series1.sort_values(ascending=False).iloc[0:5])
print(series1.sort_values(ascending=True).iloc[0:5])

# endregion

# region Series groupby() split- apply - combine
series1 = pd.Series([1,2,3,4,5])

"""
mylist = [8, 23, 45, 12, 78]
for index, item in enumerate(mylist):
    print(index, item) 
"""

# split
# g = groupby object (SeriesGroupBy object)
# groupby 物件 iterate 可迭代
g = series1.groupby(['a','a','a','b','b'])
print ( type(g),  g.groups)

for k,v in g: # k-key, v- series
    print (k)
    print(v)
    print('==================')

# apply-combine
print(g.sum())
print(g.min())
print(g.max())
print(g.count())

# ==========================
series1 = pd.Series([1,2,3,4,5,11,33])
# by_series=series1 % 2
by_series = series1.apply(lambda x: 'Even' if x%2==0 else 'Odd')

print(series1.groupby(by_series).count())
print(series1.groupby(by_series).max())
print(series1.groupby(by_series).min())

print(series1.groupby(by_series).sum())
print(series1.groupby(by_series).apply(np.sum))

# TODO　每一群由大到小排序
print(series1.groupby(by_series).apply( lambda s:s.sort_values(ascending=False)))

# TODO 每一群的全距
print(series1.groupby(by_series).apply( lambda s: s.max()-s.min()  ))


#endregion

# region Sereis value_counts()
series1 = pd.Series([90,80,90,80,100,100,100,80, 100])

print(series1.groupby(series1).count().sort_values(ascending=False))
print(series1.value_counts()) # value_counts() 就是自動做 group by series - apply - count ; 未來可看到進階的 API, 其實內部就是精簡 複雜的功能

print(series1.value_counts( normalize=True))
print((series1.groupby(series1).count()/series1.count()).sort_values(ascending=False))




# TODO  不重複值總共有幾個
series1 = pd.Series([90,80,90,80,100,100,100,80, 100])
print(series1.value_counts().count())
# or 
print(series1.unique().size)# Return number of unique elements in the object. Excludes NA values by default.
# or
print(series1.nunique()) 

# TODO 小測驗 找 80 or 90 分
print(series1.isin([80,90]))
print (series1[(series1==80) | (series1==90)])
# or 
mask = series1.isin([80,90]) # 回傳 boolean array
print (series1[mask])

print('a' in series1) # check series 的 index


# endregion


# region datetime series Series 排序 sort_values() sort_index()


data = np.random.randint(1000, 5000, 1000)
series1 = pd.Series(data, index=pd.date_range('1/1/2000', periods=1000))

print(series1)
print(series1.index.year)

print(series1.groupby(series1.index.year).sum())


# endregion


print('end')