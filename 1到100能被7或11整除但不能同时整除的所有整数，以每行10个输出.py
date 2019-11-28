print("满足条件的数字分别为:")
count=0
for i in range(1,100):
    if i%7==0 and i%11!=0 or i%11==0 and i%7!=0:
        print(i,end=" ")
        count=count+1
        if count%10==0:
            print(" ")
