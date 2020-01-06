#32.利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。
def put(s, length):
    if length == 0:
        return
    print(s[length - 1], end='')
    output(s, length - 1)


s = input()
length = len(s)
put(s, length)
