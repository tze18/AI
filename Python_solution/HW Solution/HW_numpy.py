
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# region  練習球隊範例
#  
                 
players = [56,  8, 19, 14, 6, 71]   # list 球隊人數                                        
teams = ['Apple ', 'Orange', 'pineApple', 'Big Apple', 'Bananna', 'Cherry'] # list 球隊 Team

# 建立 ndarray 物件
arr_players=np.array(players)
arr_teams=np.array(teams) 

# players 總共有幾人 ? 
print(arr_players.sum())

# Team 總共有幾隊 ?
print(arr_teams.size)

# 最多的人的 team 是幾人 ?
print(arr_players.max())

# 最多的人的 team 是哪個 team ?  即哪一隊最多人 ?
print(arr_teams[arr_players==arr_players.max()])

# 人數大於 10 的組別 ? 有幾組 ?
print(arr_teams[arr_players>10])
print(arr_teams[arr_players>10].size)

# 除了cherry組以外的 players 總數 ?
print(arr_players[arr_teams != 'cherry'].sum())

# endregion


# region 繪圖 冰島每年人口數 ? / 每年人口成長率 ?
#                                
# 近十年 2009 ~ 2018; 每年隨機 25萬 ~ 33 萬之間     
years = np.arange(2009, 2019)
populations=np.random.randint(25,34, years.shape)


plt.plot(years, populations, color='green')
plt.plot(years, populations*1.5, color='blue',linestyle='dashed', linewidth=2)

plt.xlabel('Year')
plt.ylabel('Population')
plt.title('Population/Year')
plt.show()

# ===========================================================
# 每年人口成長率 
# You are looking for pct_change

# fancy index
thisyears = np.arange(1, years.size)           # [1,2,3,4,5,6,7,8,9]
lastyears = np.arange(0,years.size-1)          # [0,1,2,3,4,5,6,7,8]

grows=np.zeros(years.shape)

grows[1:] = (populations[thisyears] - populations[lastyears]) / populations[lastyears] * 100
print(grows)

# or slice index
grows[1:] = (populations[1:] -populations[:-1] ) / populations[:-1] * 100
print(grows)

plt.plot(years, grows,  'bo--' )
plt.xlabel('Year')
plt.ylabel('Population')
plt.title('Populatoin/Year')
plt.show()

# region 使用 Series / DataFrame
# or 用 Series pct_change()
grows2 = pd.Series(populations).pct_change()
print(grows2)
plt.plot(years, grows,  'bo--' )
plt.show()


# 用 dataFrame 就會較好做 / shift
import pandas as pd
df = pd.DataFrame()

df['Year']=years
df['Population']=populations[:]
df['LYPopulation']=df['Population'].shift(1) # lastYearPopulation
df['Grows'] = (df['Population'] - df['LYPopulation']) / df['LYPopulation'] * 100
print(df)

# endregion

# endregion


# region  2d array

# Create 2d array (4*3) (value 1~12) , 大於 5 的奇數 + 200

# Create a 10x10 array with random values from the "standard normal" distribution.
# find the minimum and maximum values

# endregion

# region  畫棋盤

# 周邊 0, 內部 1

# 周邊 1, 內部 0

# 棋盤 

# [[1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
#  [1. 0. 0. 0. 0. 0. 0. 0. 0. 1.]
#  [1. 0. 0. 0. 0. 0. 0. 0. 0. 1.]
#  [1. 0. 0. 0. 0. 0. 0. 0. 0. 1.]
#  [1. 0. 0. 0. 0. 0. 0. 0. 0. 1.]
#  [1. 0. 0. 0. 0. 0. 0. 0. 0. 1.]
#  [1. 0. 0. 0. 0. 0. 0. 0. 0. 1.]
#  [1. 0. 0. 0. 0. 0. 0. 0. 0. 1.]
#  [1. 0. 0. 0. 0. 0. 0. 0. 0. 1.]
#  [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]]

# [[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
#  [0. 1. 1. 1. 1. 1. 1. 1. 1. 0.]
#  [0. 1. 1. 1. 1. 1. 1. 1. 1. 0.]
#  [0. 1. 1. 1. 1. 1. 1. 1. 1. 0.]
#  [0. 1. 1. 1. 1. 1. 1. 1. 1. 0.]
#  [0. 1. 1. 1. 1. 1. 1. 1. 1. 0.]
#  [0. 1. 1. 1. 1. 1. 1. 1. 1. 0.]
#  [0. 1. 1. 1. 1. 1. 1. 1. 1. 0.]
#  [0. 1. 1. 1. 1. 1. 1. 1. 1. 0.]
#  [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]]

# [[0. 1. 0. 1. 0. 1. 0. 1. 0. 1.]
#  [1. 0. 1. 0. 1. 0. 1. 0. 1. 0.]
#  [0. 1. 0. 1. 0. 1. 0. 1. 0. 1.]
#  [1. 0. 1. 0. 1. 0. 1. 0. 1. 0.]
#  [0. 1. 0. 1. 0. 1. 0. 1. 0. 1.]
#  [1. 0. 1. 0. 1. 0. 1. 0. 1. 0.]
#  [0. 1. 0. 1. 0. 1. 0. 1. 0. 1.]
#  [1. 0. 1. 0. 1. 0. 1. 0. 1. 0.]
#  [0. 1. 0. 1. 0. 1. 0. 1. 0. 1.]
#  [1. 0. 1. 0. 1. 0. 1. 0. 1. 0.]]

# endregion