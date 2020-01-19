str=input("请输入一串字符：")
flag=0
count=0
for c in str:
    if c=="":
        flag=0
    else:
        if flag==0:
            flag=1
            count=count+1
print("共有%d个单词"%count)
