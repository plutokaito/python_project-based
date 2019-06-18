class MyApp():
    def __init__(self):
        self.func_map = {}

    def register(self, name):
        def func_wrapper(func):
            self.func_map[name] = func
            return func
        return func_wrapper

    def call_method(self, name=None):
        func = self.func_map.get(name, None)
        if func is None:
            raise Exception("No function registered against - " + str(name))
        return func()

app = MyApp()

@app.register('/')
def main_page_func():
    return "This is the main page."

## 深刻理解
'''
@wrapper                func = wrapper(func)
def func():   =====>
    pass
'''

@app.register('/next_page')
def next_page_func():
    return "This is the next page."

def prev_page_func():
    return "This is the prev page"

# print(app.call_method('/'))
# print(app.call_method('/next_page'))

print(next_page_func())

app.register('/prev_page')(prev_page_func)
print(app.call_method('/prev_page'))