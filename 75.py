#75.题目：给定一个字符串
#找到它的第一个不重复的字符，并返回它的索引
#如果不存在，则返回 -1。
def fun(str1):
    if str1[0] != str1[1]:
        return 0
    for i in range(1, len(str1) - 1):
        if str1[i] != str1[i + 1]:
            return i + 1
    else:
        return -1


str1 = input()
print(fun(str1))
