#45.两个 3 行 3 列的矩阵，实现其对应位置的数据相加，并返回一个新矩阵：
avc1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
avc2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
avc3 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(3):
    for j in range(3):
        avc3[i][j] = avc1[i][j] + avc2[i][j]
print(avc3)
