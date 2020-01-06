def fun(n):
    n=int(input("请输入一个整数\n"))
    if n==1:
        print("是三的幂次方\n")
    while n>3 and n%3==0:
        n/=3
    if n==3:
        print("是三的幂次方\n",n)
    else:
        print("不是三的幂次方\n",n)
get def fun(3)
