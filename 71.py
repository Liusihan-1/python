#71.题目：循环输出列表
list1 = [1, 2, 3, 4, 5]
for i in range(len(list1) - 1):
    print(list1[i], end=' ')
print(list1[i + 1])
