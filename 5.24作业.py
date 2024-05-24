#通过def关键字，定义一个函数，并传入
def test_func(compute):
    result = compute(1,2)
    print(result)
def compute(x,y):
    return x+y
test_func(compute)
#可以通过lambda关键字，传入一个一次性使用的lambda匿名函数
def test_func(compute):
    result = compute(1,2)
    print(result)
test_func(lambda x,y:x+y)
#使用def和使用lambda，定义的函数功能完全一致，只是lambda关键字定义的函数是匿名的，无法二次使用