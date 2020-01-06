#19.颠倒给定的 32 位无符号整数的二进制位。
def dpf(n):
    temp = bin(n)[2:]
    count = 32 - len(temp)
    if count > 0:
        for i in range(0, count):
            temp = '0' + temp
        return int(temp[::-1], 2)
    return int(temp[::-1], 2)


num = int(input())
print('原数字的二进制表示：', bin(num))
print('颠倒二进制位后：')
print('二进制表示：', bin(dpf(num)))
print('十进制表示：%d' % dpf(num))
