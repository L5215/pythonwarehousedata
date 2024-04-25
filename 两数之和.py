def two_sum(nums, target):
    num_dict = {}  # 创建一个空字典来存储数组元素和对应的索引
    for i, num in enumerate(nums):
        complement = target - num  # 计算目标值与当前元素的差值
        if complement in num_dict:  # 检查差值是否已经在字典中
            return [num_dict[complement], i]  # 返回差值对应的索引和当前元素的索引
        num_dict[num] = i  # 将当前元素及其索引添加到字典中
    return None  # 如果没有找到满足条件的两个数，返回None


# 示例使用
nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print(result)  # 输出应该是 [0, 1]，因为 2 + 7 = 9
