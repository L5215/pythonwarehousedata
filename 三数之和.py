def threeSum(nums):
    # 首先对数组进行排序
    nums.sort()
    result = []
    n = len(nums)

    # 遍历数组，作为三元组的第一个元素
    for i in range(n - 2):
        # 跳过重复的元素
        if i > 0 and nums[i] == nums[i - 1]:
            continue

            # 定义双指针，分别指向当前元素的下一个位置和数组末尾
        left = i + 1
        right = n - 1

        # 使用双指针寻找和为0的另外两个元素
        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == 0:
                # 找到和为0的三元组
                result.append([nums[i], nums[left], nums[right]])

                # 跳过重复的元素
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                    # 移动指针以寻找新的三元组
                left += 1
                right -= 1
            elif total < 0:
                # 如果和小于0，则需要增加和，移动左指针
                left += 1
            else:
                # 如果和大于0，则需要减少和，移动右指针
                right -= 1

    return result


# 示例
nums = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums))