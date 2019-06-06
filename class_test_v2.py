class A():
    def __init__(self):
        print('我是祖先类')


class B(A):
    def __init__(self):
        print('我是第1代B')
        super().__init__()


class C(A):
    def __init__(self):
        print('我是第一代C')
        super().__init__()

class D(B):
    def __init__(self):
        print('我是第二代D-》B')
        super().__init__()

class F(C):
    def __init__(self):
        print('我是第二代F-》C')
        super().__init__()

class E(D,F):
    def __init__(self):
        print('我是E')
        super().__init__()
        # B.__init__()
        # C.__init__()


print(E())
print(E.mro())