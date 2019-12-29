def insert_sort(array):
    for i in range(1,len(array)):
        if array[i-1]>array[i]:
            temp=array[i]
            index=i
            while index>0 and array[index-1]>temp:
                array[index]=array[index-1]
                index-=1
            array[index]=temp
b=input("请输入一组数据:")
array=[]
for i in b.split(','):
    array.append(int(i))
print("排序前的数据:")
print(array)
insert_sort(array)
print("排序后的数据:")
print(array)
                
