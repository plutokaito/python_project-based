#!/usr/bin/env python
# coding: utf-8

# In[16]:


import time

def timmer(func):
    def inner(param):
        start = time.perf_counter()
        s = func(param)
        end = time.perf_counter()
        print('运行时间:{}'.format(end-start))
        return s
    return inner

@timmer
def str_append(s):
    '''
        1000
        10000000 3.7433260419929866
    '''
    for n in range(0, 100000):
        s += str(n)
    return s;

s = ''
s = str_append(s)
#f"输出的字符串为：{s}"


@timmer
def list_append(l):
    '''
    1000
    10000000 3.4244577790086623
    '''
    for n in range(0, 100000):
        l.append(str(n))
    return l

l = [];
l = list_append(l)
s = ' '.join(l)


# In[6]:





# In[ ]:




