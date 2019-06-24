#%%
import os
import psutil

def show_memory_info(hint):
    pid = os.getpid()
    p = psutil.Process(pid)

    info = p.memory_full_info()
    memory = info.uss / 1024. /1024
    print('{} memory used:{} MB'.format(hint, memory))

def test_iterator():
    show_memory_info('initing iterator')
    list_1 = [i for i in range(100000000)]
    show_memory_info('after iterator initiated')
    print(sum(list_1))
    show_memory_info('after sum called')

def test_generatir():
    show_memory_info('initing generator')
    list_2 = (range(100000000))
    show_memory_info('after generator initiated')
    print(sum(list_2))
    show_memory_info('after sum called')

%time test_generatir()
%time test_iterator()

#%%
## 验证（1 + 2 + 3 + ... + n）^2 = 1^3+2^3+...+n^3
def generator(k):
    i = 1
    while True:
        yield i ** k
        i += 1
gen_1 = generator(1)
gen_2 = generator(3)
print(gen_1)
print(gen_2)

def get_sum(n):
    sum_1,sum_3 = 0, 0
    for i in range(n):
        next_1 = next(gen_1)
        next_3 = next(gen_2)
        print('next_1 = {}, next_3 = {}'.format(next_1, next_3))
        sum_1 += next_1
        sum_3 += next_3
    print(sum_1 ** 2, sum_3)

get_sum(8)

#%%
def index_normal(L, target):
    result = []
    for i, num in enumerate(L):
        if num == target:
            result.append(i)
    return result

print(index_normal([1, 6, 2, 4, 5, 2, 8, 6, 3, 2], 2))



#%%
def index_generator(L, target):
    for i, num in enumerate(L):
        if num == target:
            yield i

print(index_generator([1, 6, 2, 4, 5, 2, 8, 6, 3, 2], 2))

#%%

# 给定两个序列，判断第一个是不是第二个子序
def is_subsequence(a, b):
    b =  iter(b)
    return all(i in b for i in a)

print(is_subsequence([1, 3, 5], [1, 2, 3, 4, 5]))
print(is_subsequence([1, 4, 6], [1, 2, 3, 4, 5]))

#%%
def is_subsequence_detail(a, b):
    b = iter(b)
    #print(b)

    gen = (i for i in a)
    #print(gen)

    for i in gen:
        print(i)
    
    

    gen = ((i in b) for i in a)
    print(list(gen))

    for i in gen:
        print(i)
    
    #print(next(b))

    return all(gen)

print(is_subsequence_detail([1, 3, 5], [1, 2, 3, 4, 5]))
print(is_subsequence_detail([1, 6, 5], [1, 2, 3, 4, 5]))


#%%
