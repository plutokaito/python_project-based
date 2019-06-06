# 父类的私有变量继承问题
class A(object):
    def __init__(self):
        self.__a_private_param = '我是父类私有变量'
        self.a_param = '我是父类变量'

    def getPrivateParam(self):
        return self.__a_private_param

class B(A):
    def __init__(self):
        super(B, self).__init__()
        # B.private_param = self.__a_private_param 不能继承
        B.param = self.a_param

    def getParentPrivateParam(self):
        return super(B, self).getPrivateParam()

obj_a = A()
print(obj_a.getPrivateParam())
obj_b = B()
print(obj_b.param)
print(obj_b.getPrivateParam())
