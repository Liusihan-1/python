#86题目：有两个磁盘文件A和B,各存放一行字母
#要求把这两个文件中的信息合并(按字母顺序排列), 输出到一个新文件C中。
with open("A.txt", "r") as fileA:
    strA = ''
    for letters in fileA:
        strA += letters
with open("B.txt", "r") as fileB:
    strB = ''
    for letters in fileB:
        strB += letters
strC = "".join(sorted(strA + strB))
with open("C.txt", "w") as fileC:
    fileC.write(strC)
