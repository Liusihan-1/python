#取一个整数a从右端开始的4〜7位。
a = int(input())
b = a >> 4
c = ~(~0 << 4)
d = b & c
print('%o\t%o' % (a, d))
