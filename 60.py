#题目：给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
def reverseNumber(x):
    if x >= 0:
        xReverse = int(str(x)[::-1])
    else:
        xReverse = -int(str(x)[:0:-1])

    # 判断反转后的整数是否溢出
    if -2 ** 31 <= xReverse <= 2 ** 31 - 1:
        return xReverse
    else:
        return 0


n = int(input())
print(reverseNumber(n))
