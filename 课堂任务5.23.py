# def user_info(*args):
#     print(args)
# #('Tom')
# user_info('Tom')
# #('Tom',18)
# user_info('Tom',18)
#
# def user_info(**kwargs):
#     print(kwargs)
# #('name':'Tom','age':'18','id':'110')
# user_info(name='Tom',age=18,id=110)

def sum(*nums):
    #定义一个变量，来保存结果
    result=0
    #遍历元组，并将元组中的数进行累加
    for n in nums:
        result += n
    print(result)
sum(123,456,789,10,20,30,40)