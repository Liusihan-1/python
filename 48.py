#48.两个变量值互换。
a = int(input('a = '))
b = int(input('b = '))
a, b = b, a
print('交换后：a = %d, b = %d' % (a, b))
