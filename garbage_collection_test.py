#%%
import os
import psutil

# 显示当前python程序占用的内存大小
def show_memory_info(hint):
    pid = os.getpid()
    p = psutil.Process(pid)

    info = p.memory_full_info()
    memory = info.uss / 1024. / 1024
    print('{} memory used: {} MB'.format(hint, memory))

def func():
    show_memory_info('initial')
    a = [i for i in range(100000000)]
    show_memory_info('after a created')

def global_param_func():
    show_memory_info('inital')
    global b
    b = [i for i in range(10000000)]
    show_memory_info('after a created global')

func()
global_param_func()
show_memory_info('finished')

#%%
import sys

a = []

print(sys.getrefcount(a))

def func(a):
    print(sys.getrefcount(a))

func(a)
print(sys.getrefcount(a))

#%%
import sys

a= [1]

print(sys.getrefcount(a))

b = a
print(sys.getrefcount(a))

c,d,e,f,g,h = b,b,c,e,d,a
# d = b
# e = c
# f = e
# g = d
print(g)
print(sys.getrefcount(a))

#%%
import gc
show_memory_info('initial')
a = [i for i in range(10000000)]
show_memory_info('after a created')

del a
gc.collect()
show_memory_info('finish')
print(a)

#%%
## 循环引用
def func():
    show_memory_info('initial')
    a = [i for i in range(100000000)]
    b = [i for i in range(100000000)]
    show_memory_info('after a,b  created')
    a.append(b)
    b.append(a)

func()
gc.collect()
show_memory_info('finished')

#%%
import objgraph

a = [1, 2, 3]
b = [4, 5, 6]

a.append(b)
b.append(a)

objgraph.show_refs([a])
objgraph.show_backrefs([a])
#%%
