#-*- coding:utf-8 -*-

'''示例4: 使用内嵌包装函数来确保每次新函数都被调用，
内嵌包装函数的形参和返回值与原函数相同，装饰函数返回内嵌包装函数对象'''

def deco4(func):
    def _deco():
        print("before myfunc4() called.")
        func()
        print("after myfunc4() called.")
        # 不需要返回func，实际上应返回原函数的返回值
    return _deco

@deco4
def myfunc4():
    print(" myfunc() called.")
    return 'ok'

#myfunc4()
#myfunc4()

'''示例5: 对带参数的函数进行装饰，
内嵌包装函数的形参和返回值与原函数相同，装饰函数返回内嵌包装函数对象'''

def deco5(func):
    def _deco(a, b):
        print("before myfunc() called.")
        ret = func(a, b)
        print("  after myfunc() called. result: %s" % ret)
        return ret
    return _deco

@deco5
def myfunc5(a, b):
    print(" myfunc5(%s,%s) called." % (a, b))
    return a + b

#myfunc5(1, 2)
#myfunc5(3, 4)

'''示例6: 对参数数量不确定的函数进行装饰，
参数用(*args, **kwargs)，自动适应变参和命名参数'''
def deco6(func):
    def _deco(*args, **kwargs):
        print("before %s called." % func.__name__)
        ret = func(*args, **kwargs)
        print("  after %s called. result: %s" % (func.__name__, ret))
        return ret
    return _deco

@deco6
def myfunc61(a, b):
    print(" myfunc(%s,%s) called." % (a, b))
    return a+b

@deco6
def myfunc62(a, b, c):
    print(" myfunc2(%s,%s,%s) called." % (a, b, c))
    return a+b+c

myfunc61(1, 2)
myfunc61(3, 4)
myfunc62(1, 2, 3)
myfunc62(3, 4, 5)
