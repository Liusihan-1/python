print("1~200的素数有:")
for n in range(1,201):
    flag=1
    for i in range(2,n):
        if n%i==0:
            flag=0
            break
    if flag==1:
        print(n,end=" ")

