#43.有一个已经排好序的列表。现输入一个数，要求按原来的规律将它插入数组中。
a = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]
b = int(input())
a.append(b)
a.sort()
print(a)
