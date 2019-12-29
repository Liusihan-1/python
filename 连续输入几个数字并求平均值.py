sum=0
num=0
flag=input("please input 'yes' or 'no'")
yes=str(yes)
while flag==yes:
    score=int(input("please input a number:"))
    sum=int(sum)
    sum=score+sum
    num=num+1
    aver=sum/num
    print("aver is:",aver)
else:
    return 0

