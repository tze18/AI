import numpy as np
import pandas as pd

# region DataFrame 處理遺失 NA 值 (清洗資料) 

data = pd.read_excel('data/scoresToClean.xlsx', sheet_name='Sheet1')
df = pd.DataFrame(data)

# drop columns or rows
df.drop(['Avg','Rank','Sum','Max','Min','Good'],axis=1, inplace=True) # drop columns
df.drop([8,9],axis =0, inplace=True)                                  # drop rows

#endregion

# region DataFrame wrangle data 資料角力 - merge(join) concate(union) reshape

df_Categories = pd.read_excel('data/CategoryProducts.xlsx', sheet_name='Categories')
df_Products = pd.read_excel('data/CategoryProducts.xlsx', sheet_name='USAProducts')



df1 = pd.read_excel('data/CategoryProducts.xlsx', sheet_name='USAProducts')
df2 = pd.read_excel('data/CategoryProducts.xlsx', sheet_name='CAProducts')

#endregion

# region DataFrame groupby
# endregion

# region DataFrame plot

# endregion

print('end')