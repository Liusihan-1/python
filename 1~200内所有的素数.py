print("1~200内的素数有:")
for m in range(1,201):
    flag=1
    for i in range(2,m):
        if m%i==0:
            flag=0
            break
    if flag==1:
        print(m,end=" ")
