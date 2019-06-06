# 接口类
from abc import ABCMeta,abstractclassmethod

class A(metaclass=ABCMeta):
    @abstractclassmethod
    def get_title(self):
        pass

    @abstractclassmethod
    def get_content(self):
        pass