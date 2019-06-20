class MyMeta(type):
    def __init__(cls, name, bases, dict):
        cls.a = 1 # 会被重载
        cls.b = 2 # 会被保留
        print('MyMeta __init__')

    def __new__(cls, name, bases, dict):
        print('MyMeta __new__')
        return type.__new__(cls, name, bases, dict)

    def __call__(cls):
        print('MyMeta __call__')
        return type.__call__(cls)

class Test(metaclass=MyMeta):
    def __init__(self):
        self.a = 10
        print("Test init")

    def __new__(cls):
        print('Test __new__')
        return super(Test, cls).__new__(cls)
    
    def __call__(self):
        print("Test __call__")

test = Test()
print(test.a)
print(test.b)
#print(instance.__bases__)
#print(instance.data)
# 







#### type和object
import yaml 
# Python 2/3 相同部分
class YAMLObjectMetaclass(type):
    def __init__(cls, name, bases, kwds):
        super(YAMLObjectMetaclass, cls).__init__(name, bases, kwds)
        if 'yaml_tag' in kwds and kwds['yaml_tag'] is not None:
            cls.yaml_loader.add_constructor(cls.yaml_tag, cls.from_yaml)
        # 省略其余定义

#Python 3 
class YAMLObject(object, metaclass=YAMLObjectMetaclass):
    yaml_loader = 'Loader'
    #省略其余定义
## 上述相当于
##YAMLObject = YAMLObjectMetaclass('YAMLObject', (), {'yaml_loader':'Loader'})
'''
print(YAMLObject.__bases__)
print(YAMLObject.__class__)
print(YAMLObject.yaml_loader)
'''
