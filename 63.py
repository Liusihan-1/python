#63.题目：有n个整数，使其前面各数顺序向后移m个位置，最后m个数变成最前面的m个数
num = list(eval(input("请输入数字")))
m = int(input("请输入数字"))
n = len(num)
result = []
for i in range(n - m, n):
    result.append(num[i])
for i in range(n - m):
    result.append(num[i])
print(result)
