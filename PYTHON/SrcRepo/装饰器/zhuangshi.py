#-*- coding:utf-8 -*-
'''示例1: 最简单的函数,表示调用了两次'''
def myfunc1():
    print("myfunc called.")

'''示例2: 替换函数(装饰)
装饰函数的参数是被装饰的函数对象，返回原函数对象
装饰的实质语句: myfunc = deco(myfunc)'''
def deco2(func):
    print("before myfunc called.")
    func()
    print("after myfunc called.")
    return func
#myfunc = deco(myfunc)

'''示例3: 使用语法糖@来装饰函数，相当于“myfunc = deco(myfunc)”
但发现新函数只在第一次被调用，且原函数多调用了一次'''
def deco3(func):
    print("before myfunc3() called.")
    func()
    print("after myfunc3() called.")
    return func

@deco3
def myfunc3():
    print(" myfunc() called.")



myfunc3()
myfunc3()
