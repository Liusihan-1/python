#73.题目：给定一个整数数组 nums 和一个目标值 target
#请你在该数组中找出和为目标值的那两个整数并返回他们的数组下标
#你可以假设每种输入只会对应一个答案。
#但是，你不能重复利用这个数组中同样的元素。

nums = [2, 7, 11, 15]
flag = int(input())
for i in range(4):
    for j in range(i + 1, 4):
        if nums[i] == flag - nums[j]:
            print(i, j)
