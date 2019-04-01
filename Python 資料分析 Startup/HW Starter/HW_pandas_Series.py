import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# region 銷售分析 &　plot (I) 

dateindex = pd.date_range(start='1/1/2000',periods=4000)
series1 = pd.Series(np.random.randint(1000, 5000, 4000), index=dateindex )
# print(series1)

# 2001 年 的總銷售 ?  某年 總銷售金額 ? 
# print(sum(series1['1-1-2001':'12-31-2001']))
# print(sum(series1['2001']))

# 2000 & 2001 年 的總銷售 ?
print(sum(series1['2001'])+sum(series1['2000']))
# 2000 ~ 2009 年 的總銷售 ?
print(sum(series1['2000':'2009']))
# endregion

# region 銷售分析 &　plot (II)

# 年度最高銷售金額 年度最低銷售金額
y=series1.groupby(dateindex.year)
print(y.max())

print(y.min())
# 那一年總銷售最好 ? 那一年總銷售最不好 ?  hint:idxmax()
# print(y.sum())
# print(y.sum().idxmin())
# print(y.sum().idxmax())

# 那一個月總銷售最好 ? 那一個月總銷售最不好 ?

m=series1.groupby([dateindex.year,dateindex.month])
print(m.sum().idxmin())
print(m.sum().idxmax())
# 每年 總銷售分析 圖
# y.sum().plot()
# plt.show()
# 每月 總銷售分析 圖
# m.sum().plot()
# plt.show()
# 年累計總銷售   hint:cumsum()
print(y.sum().cumsum())

# endregion


# region groupby 隨機 統計 100 個學生 分數 60~200
series2 = pd.Series(np.random.randint(60,101,100))
# split=> 分成 三群 '待加強'(60~69) '佳'(70~89) '優良'(90~100) 
def score(x):
    if (x>=90):
        return '優良'
    elif (x>=70):
        return '佳'
    else:
        return '待加強'  
s1=series2.apply(score)
g = series2.groupby(s1)  
for k,v in g :
    print(k)
    print(v)
# print 每一群是哪幾個 ? (每一群 sort by 分數 descending)
# print(s1.sort())
# endregion


# region 統計 : 每一群有幾個 ? 每一群最高分 每一群最低分 每一群全距 
print('22222222222')
print(g.count())
print(g.max())
print(g.min())
print(g.max()-g.min())
# 統計 :　所有隨機分數出現的次數/比率; sort ascending or descending
s2=series2.groupby(series2)
print(s2.count())
# Excellent
# 3     95
# 1     94
# 14    91
# ...
# dtype: int32

# Good
# 6    89
# 5    88
# 0    71
# ...and
# dtype: int32

# OK
# 4    63
# 2    63
# 7    62
# ...
# dtype: int32


#            count       mean       std   min   25%   50%    75%    max
# Excellent   23.0  95.391304  3.726309  90.0  92.0  96.0  99.50  100.0
# Good        52.0  80.000000  5.725759  70.0  75.0  79.0  84.25   89.0
# OK          25.0  63.160000  2.511308  60.0  61.0  63.0  64.00   69.0


#            count       mean       std  min  max  quantile  median  peak
# Excellent     23  95.391304  3.726309   90  100      96.0      96    10
# Good          52  80.000000  5.725759   70   89      79.0      79    19
# OK            25  63.160000  2.511308   60   69      63.0      63     9


# None
# 63     7.00%
# 100    6.00%
# 78     6.00%
# 89     5.00%
# 83     5.00%
# 61     4.00%
# 64     4.00%
# 91     4.00%
# 79     4.00%
# 84     3.00%
# 62     3.00%
# 73     3.00%
# 74     3.00%
# 75     3.00%
# ...

# endregion



# region 統計 :所有隨機分數出現的次數/比率? sort ascending or descending

# None
# 63     7.00%
# 100    6.00%
# 78     6.00%
# 89     5.00%
# 83     5.00%
# 61     4.00%
# 64     4.00%
# 91     4.00%
# 79     4.00%
# 84     3.00%
# 62     3.00%
# 73     3.00%
# 74     3.00%
# 75     3.00%
# ...

# endregion
