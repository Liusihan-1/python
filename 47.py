#47.求输入数字的平方，如果平方运算后小于 50 则退出。
a = 1
while a:
    num = int(input())
    print(num**2)
    if num**2 >= 50:
        again = 1
    else:
        again = 0
