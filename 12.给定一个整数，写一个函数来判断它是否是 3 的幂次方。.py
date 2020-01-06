#给定一个整数，写一个函数来判断它是否是 3 的幂次方。
def fun(n):
    if n == 1:
        return True
    while n > 3 and n % 3 == 0:
        n /= 3
    if n == 3:
        return True
    else:
        return False


num = int(input())
print(fun(num))
