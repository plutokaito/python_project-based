def my_decorator(func):
    def wrapper():
        print('wrapper of decorator')
        func()
    return wrapper

def greet():
    print('hello world')

greet_text = my_decorator(greet)
greet_text()

# 语法糖版
@my_decorator
def greet_func():
    print('Hello world')

greet_func()