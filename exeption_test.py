#!/usr/bin/env python
# coding: utf-8

# In[1]:


10/0


# In[7]:


try:
    s = input('please enter two numbers separated by comma:')
    num1 = int(s.split(',')[0].strip())
    num2 = int(s.split(',')[1].strip())
    print(f"{num1}:{num2}")
except ValueError as err:
    print(f"Value Error {err}")

print('continue')


# In[15]:


# 自定义异常
class MyInputError(Exception):
    """Exception raised when there're errors in input"""
    def __init__(self, value): # 自定义异常的初始化
        self.value = value
    def __str__(self): # 自定义异常类型的string表达形式
        return ("{} is invalid input".format(repr(self.value)))

try:
    raise MyInputError(1) # 手动抛出异常
except MyInputError as err:
    print("error:{}".format(err))


# In[12]:





# In[ ]:




