#84.题目：从键盘输入一个字符串，将小写字母全部转换成大写字母
#然后输出到一个磁盘文件"test"中保存。
with open("test.txt", "a") as file:
    strs = input("请输入一个字符串:")
    strs = strs.upper()
    file.write(strs)
