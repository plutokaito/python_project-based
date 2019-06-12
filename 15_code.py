
# a = 10
# b = 10

# print(a == b)

# print(id(a)) # id() 获取对象的身份标示
# print(id(b))

# print(a is b)

# a = 257
# b = 257
# print(id(a))
# print(id(b))
# print(a is b)
# l1 = [1, 2, 3]
# l2 = list(l1)

# print(l2)
# print(id(l2[1]))
# print(id(l1[1]))

# t1 = (1, 2, 4)
# t2 = tuple(t1)

# print(id(t1))
# print(id(t2))

t1 = [[1, 3], (3, 4), {'df':'dfsd'}, {'sdf', 'dsfads'}]
t2 = list(t1)

print(t2)
t1.append('sdfadsf') # 原列表增加元素
print(t2) # t2的值没有变化
t1[0].append(455)
print(t2) # t2的值有变化
t1[1] += (444, 555)
print(f't1的值{t1}, t2的值{t2}') # t1的值改变，t2的值没有变

t1[2]['dsfsdf'] = 'sdfdasfadsffadf'
print(t2) # t2的值发生变化

t1[3].add('dsfffadsfasd')
print(t2) # t2的值发生变化


#### 元祖
a = (1, 3, 4)
b = a[:]
print(b)
a += (6, 7) # 元祖重新生成一块内存给了a
print(b)

#### 深拷贝
import copy
x = [1]
x.append(x)
print(x)
print(len(x)) # [1, [1, [1, ...]]],所以值是2
y = copy.deepcopy(x)
print(y)
print(x == y) # RecursionError: maximum recursion depth exceeded in comparison
import sys
print(sys.getrecursionlimit()) # 获取最大递归次数