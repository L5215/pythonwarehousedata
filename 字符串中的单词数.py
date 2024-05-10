def count_words(text):
    # 使用 split() 方法将字符串按空格分割成单词列表
    # 假设字符串中只包含空格作为单词的分隔符
    words = text.split()
    # 返回单词列表的长度
    return len(words)
# 示例字符串
text = "Hello, my name is Jhon"
# 调用函数并打印结果
print(count_words(text)) # 输出: 5