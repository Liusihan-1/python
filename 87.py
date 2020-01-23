#87题目：列表转换为字典。
a_list=['a','b','c']
b_list=[1,2,3]
a_dict={}
for i in range(len(a_list)):
    a_dict[a_list[i]]=b_list[i]
print(a_dict)
