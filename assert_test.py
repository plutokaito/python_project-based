#%%
assert 1 == 2, 'assertion is wrong'
#%%
if __debug__:
    if not 1 == 2:
        raise AssertionError('assertion is wrong')

#%%
import unittest

# 将要被测试的排序函数
def sort(arr):
    l = len(arr)
    for i in range(0, l):
        for j in range(i+1, l):
            if arr[i] >= arr[j]:
                tmp = arr[i]
                arr[i] = arr[j]
                arr[j] = tmp

# 编写子类继承 unittest.TestCase
class TestSort(unittest.TestCase):

    # 以 test 开头的函数将会被测试
    def test_sort(self): 
        arr = [3, 4, 1, 5, 6]
        sort(arr)
        # assert 结果跟我们期待的一样
        self.assertEqual(arr, [1, 3, 4, 5, 6])

if __name__ == '__main__':
    # 在 IPython 或者 Jupyter 环境下， 使用这行代码
    unittest.main(argv=['first-arg-is-ignored'], exit=False)           


#%%
import unittest
from unittest.mock import MagicMock

class A(unittest.TestCase):
    def m1(self):
        val = self.m2()
        self.m3(val)

    def m2(self):
        pass
    
    def m3(self, val):
        pass

    def test_m1(self):
        a = A()
        a.m2 = MagicMock(return_value="custom_val")
        a.m3 = MagicMock()
        a.m1()
        self.assertTrue(a.m2.called) # 验证 m2 被调用过
        a.m3.assert_called_with("custom_val") # 验证 m3 被指定参数 call 过

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

#%%
from unittest.mock import MagicMock

def side_effect(arg):
    if (arg < 0):
        return 1
    else :
        return 2

mock = MagicMock()
mock.side_effect = side_effect

mock(-2)

#%%

