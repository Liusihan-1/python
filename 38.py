#38.按逗号分隔列表
list1 = [1, 2, 3, 4, 5]
list2 = ','.join(str(n) for n in list1)
print(list2)
