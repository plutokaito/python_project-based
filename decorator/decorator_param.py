# 带有参数的装饰器
def my_decorator(func):
    def wrapper(msg):
        print('hello, {}'.format(func.__name__))
        func(msg)
        print('goodbye, {}'.format(func.__name__))
    return wrapper

@my_decorator
def shuai(msg):
    print('say:{}'.format(msg))

shuai('Hello world')

#print(greet.__name__)
#print(help(greet))

import functools
def wrap_logger(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        print("%s(%s, %s)" % (func, args, kwargs))
        print("before execute")
        result = func(self, *args, **kwargs)
        print("after execute")
        return result

    return wrapper


class Test:
    def __init__(self):
        pass

    @wrap_logger
    def test(self, a, b, c):
        print(f"{a},{b},{c}")


t = Test()
t.test(1, 2, 3)