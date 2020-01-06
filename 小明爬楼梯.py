num=int(input("请输入台阶数:"))
n1,n2=1,1
sum=[]
for i in range(num):
    n1,n2=n2,n1+n2
    sum.append(n1)
    q=max(sum)
print(f"方法共有：{q}")
    
