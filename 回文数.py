def is_palindrome(x):
    # 将整数转换为字符串
    str_x = str(x)
    # 比较字符串与其反转后的字符串是否相同
    return str_x == str_x[::-1]


# 测试
print(is_palindrome(121))  # 返回True
print(is_palindrome(-121))  # 返回False
print(is_palindrome(10))  # 返回False