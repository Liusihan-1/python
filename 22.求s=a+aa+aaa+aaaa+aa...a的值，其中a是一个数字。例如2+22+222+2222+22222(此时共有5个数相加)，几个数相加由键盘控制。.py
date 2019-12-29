def getNum(a,count):
    list1 = []
    res = 0
    a=str(a)
    for i in range(1,count+1):
        list1.append(int(a*i))
        print(list1[i-1],end=" ")
        if i<count:
            print("+",end=" ")
    for j in list1:
        res += j
    print("=", res)
    return res

getNum(2,5)

