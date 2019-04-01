# !/usr/bin/python 
# -*-coding:utf-8 -*- 

# n=0
# while n<5:
#     if n==3:
#      break
#     print(n)
#     n+=2
# print("最後的 n:",n)
# n=0
# for x in[0,1,2,3]:
#     if x%2==0:
#         continue    
#     print(x)
#     n+=1
# print("最後的 n:",n)       
# sum=0
# for n in range(11):
#     sum+=n

# else:
#     print(sum)

n=input("輸入一個數字:")
n=int(n)
for i in range(n):
    if i*i==n:
    print("整數平方根:", i)
     break
else:
    print("沒有平方根")     

