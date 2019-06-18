from functools import wraps

class MyApp(object):
    def __init__(self, fn):
        print(f"{fn.__name__} init")
        self.fn = fn

    def __call__(self, *args):
        self.fn(*args)
        print(f"{self.fn.__name__}  called")

@MyApp
def example(msg):
    print(f"hello world,{msg}")

example('shuai')

def no_sugar(msg):
    print(f"hello world, {msg}")

exam = MyApp(no_sugar)
exam('shi')