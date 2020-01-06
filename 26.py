#26.打印出如下图案（菱形）：
n=int(input("请输入行数："))
for i in range(1,n):
    for j in range(1,n-i):
        print(end=" ")
    for a in range(1,i+1):                     
        print("*",end=" " )
    print()
for b in range(2,n):
    for c in range (2,b+1):          
        print(end=" ")
    for d in range(b,n):
        print("*",end=" ")
    print()

