#40.统计所有小于非负整数 n 的质数的数量。
n = int(input())
count = 0
for i in range(2, n):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        count += 1
print(count)
