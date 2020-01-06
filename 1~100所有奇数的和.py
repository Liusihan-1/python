#1-100所有奇数的和
sum=0
for i in range(1,101):
    if i%2!=0:
        sum=sum+i
        i+=1
print(f"1-100所有奇数的和是：{sum}")
    
