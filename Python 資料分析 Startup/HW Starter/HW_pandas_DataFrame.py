
# region 搜尋 班級學生成績
# Read scores.csv; first column as index
# 共幾個 學員成績 ?						
				
# 找出 前面三個 的學員所有科目成績					
# 找出 後面兩個 的學員所有科目成績					
												
# 找出 ID index 'a','b','c' 的學員國文英文科目成績					

# 找出學員 'bbb' 的成績	                          ==
           		
# 找出除了 'bbb' 學員的學員的所有成績 ('bbb' 退學)	!=
 							
# 找出 Name 名字 'aaa', 'bbb' 'ccc' 學員 國文數學兩科 科目成績  |	 isin(...)	
# 				
# 數學不及格 ... 是誰 , 有幾個 ?
# endregion

# region 統計 每個學生個人成績

# scores_df.to_excel('data/scores統計.xlsx')
# Rank by 三科成績加總 並排序
# 國文權重加倍
# 依平均分計算 Grade & Pass 
# endregion

# region Clean Data 國英數 na 填平均
# scoresToClean.xlsx=>scoresToCleanOut.xlsx
# endregion

# region Group by 學生統計資料 & 繪圖

# 各班級英文最高分最低分相差分
#         min  max       peak
# Class                     
# CS_101   50   80        30
# CS_102   70   80        10

# 群組統計後, CS_101 英文最高分 ?

# ------------------------------
# 各班級不同性別數學最高分 ?
# Class   Gender
# CS_101  Female     55
#         Male       50
# CS_102  Female     85
#         Male      100


# 群組統計後, CS_101 女生數學最高分 ?

# ---------------------------------
# 各班級不同性別數學最高分 ? (groupby or pivot_table)
# Gender  Female  Male
# Class
# CS_101      75    50
# CS_102      85   100



# endregion

# region Group by 統計資料 & 繪圖 optional
# 鐵達尼號不同性别的活存分析


# 男女生存人數 / 男女生存比率

# Sex
# female    233
# male      109
# Name: Survived, dtype: int64

# Sex
# female    68.13%
# male      31.87%
# Name: Survived, dtype: object

# 不同性別 生存/死亡 人數
# 不同性別 生存/死亡 人數比率

# Sex     Survived
# female  0            81
#         1           233
# male    0           468
#         1           109

# Survived   罹難   活存
# Sex               
# female      81    233
# male       468    109


# Survived   罹難      活存
# Sex                     
# female    25.80%  74.20%
# male      81.11%  18.89%

# ========================================
# 每個月總銷售分析 
# 各製造商每個月總銷售分析 
# Date
# 1     791664.93
# 2    1236566.52
# 3    2205318.15
# 4    2233854.63
# 5    1785360.78
# 6    1573418.07
# Name: Revenue, dtype: float64

# endregion
