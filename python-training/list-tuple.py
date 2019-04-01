# !/usr/bin/python 
# -*-coding:utf-8 -*- 
#有序可變動列表list
#grades=[12,60,15,70,90]
# grades[1:4]=[] #連續刪除列表中從編號一到編號四（不包含）的資料
# grades=grades+[12,33]
# grades[1]
#length=len(grades) #取得列表的長度 len(列表資料)
#print(length)
# grades[0]=55 #把55放到列表中的第一個位置
#print(grades)
#---------------------------------------
# data=[[3,4,5],[6,7,8]]
# print(data)
# data[0][0:2]=[5,5,5]
# print(data)
#有序不可變動列表tuple
data=(3,4,5)
data[0]=5 #錯誤：tuple的資料不可以變動
print(data)