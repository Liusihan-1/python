#求两个整数的最大公约数
m,n=eval(input("请输入两个整数:"))
if m<n:
    min=m
else:
    min=n
for i in range(min,1,-1):
    if m%i == 0 and n%i == 0:
         print("最大公约数为:",i)
         break
         
