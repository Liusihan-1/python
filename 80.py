#80.给定一个数组 nums
#编写一个函数将所有0移动到数组的末尾，同时保持非零元素的相对顺序。
def fun(list1):
    sxc = []
    count = 0
    for i in range(len(list1)):
        if list1[i] != 0:
            sxc.append(list1[i])
        else:
            count += 1
    for j in range(count):
        sxc.append(0)
    return sxc


nums = list(eval(input()))
print(fun(nums))
