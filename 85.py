#85.题目：给定一个非空整数数组，除了某个元素只出现一次以外，
#其余每个元素均出现两次。找出那个只出现了一次的元素
nums=[1,2,2,3,3,4,4,5,5,6,6,7,7]
for i in range(len(nums)):
    if nums.count(nums[i]) == 1:
        print('nums[%d]: %d' % (i, nums[i]))
        break
