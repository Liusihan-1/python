n=int(input('请输入需要分解的正整数'))
lt = []
m=n
while n>1:
    for i in range(2,n+1):
        if n%i==0:
            n=n//i
            lt.append(str(i))
            break
if len(lt) == 1:
    print(m,'=','1 x',m)
else:
    s ='x'.join(lt)
    print(m,'=',s)    
