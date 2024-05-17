def maximumProduct(nums):
    # 对数组进行排序
    nums.sort()
    n = len(nums)

    # 考虑有负数和没有负数的情况
    # 1. 两个最小的负数（如果存在）和最大的数相乘
    # 2. 最大的三个数相乘
    return max(nums[0] * nums[1] * nums[n - 1], nums[n - 3] * nums[n - 2] * nums[n - 1])


# 示例使用
nums = [1,2,3,4]
print(maximumProduct(nums))