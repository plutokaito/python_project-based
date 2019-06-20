class MyMeta(type):
    def __init__(cls, name, bases, dict):
        print('MyMeta __init__')

    def __new__(cls, name, bases, dict):
        print('MyMeta __new__')
        return type.__new__(cls, name, bases, dict)

    def __call__(cls):
        print('MyMeta __call__')
        return type.__call__(cls)

class Test(metaclass=MyMeta):
    a = 10

    def __init__(self):
        pass

    def __new__(cls):
        return super(Test, cls).__new__(cls)

test = Test()