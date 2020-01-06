#35.一个5位数，判断它是不是回文数。
#即12321是回文数，个位与万位相同，十位与千位相同
num = int(input('请输入一个五位数：'))
a = num // 10000
b = num % 10000 // 1000
c = num % 1000 // 100
d = num % 100 // 10
e = num % 10
if a == e and b == d:
    print('%d是回文数' % num)
else:
    print('%d不是回文数' % num)
