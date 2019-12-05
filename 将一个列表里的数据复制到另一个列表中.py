list1=[4,3,2,1]
list2=[]
list3=[]
for i in range(len(list1)):
    print(list1[i])
for i in list1:
    list2.append(i)
list2.sort(reverse=False)
print(list2)
list3=sorted(list2)
print(list3)
