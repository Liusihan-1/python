def isprime(n):
    for i in range(2,n):
        if(n%i==0):
            return 0
    return 1
m=int(input("请输入一个整数:"))
flag=isprime(m)
if(flag==1):
    print("%d是素数"%m)
else:
    print("%d不是素数"%m)
        
