num = int(input('请输入数列的元素个数:'))

n1, n2 = 0, 1

fib = []

for i in range(num):

    n1, n2 = n2, n1 + n2

    fib.append(n1)

print (fib)
