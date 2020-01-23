#91.题目：python字典按照value进行排序
A_dict = {'a': 1, 'b': 4, 'c': 2, 'd': 12}
print(A_dict)
A_dict = dict(sorted(A_dict.items(), key=lambda x: x[1]))
print(A_dict)
