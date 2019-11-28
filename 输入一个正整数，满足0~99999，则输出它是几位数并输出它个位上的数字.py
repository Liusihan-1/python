x=int(input("Please input x:"))
if x>=0 and x<99999:
    i=x
    n=0
    while i>0:
        i=i//10
        n=n+1
    a=x%10
    print("%d是%d位数,它的个位上数字是%d"%(x,n,a))
else:
    print("输入错误!")
