def plusOne(digits):
    # 从数组末尾开始遍历
    carry = 1  # 初始进位为1
    for i in range(len(digits) - 1, -1, -1):
        # 当前位与进位相加
        sum_digit = digits[i] + carry
        # 更新当前位
        digits[i] = sum_digit % 10
        # 更新进位
        carry = sum_digit // 10

        # 如果最高位也有进位，则在数组最前面插入1
    if carry:
        digits.insert(0, carry)

    return digits


# 示例
digits = [1, 2, 3]
print(plusOne(digits))  # 输出: [1, 2, 4]

digits = [9, 9, 9]
print(plusOne(digits))  # 输出: [1, 0, 0, 0]

digits = [0]
print(plusOne(digits))  # 输出: [1]