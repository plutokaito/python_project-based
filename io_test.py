#!/usr/bin/env python
# coding: utf-8

# In[5]:


name = input('your name')
gender = input('u r a boy?(y/n)')

welcome_str = 'Welcome to matrix {prefix} {name}'
welcome_dic = {
    'prefix': 'Mr.' if gender == 'y' else 'Mrs.',
    'name': name
}

print('authorizing')
print(welcome_str.format(**welcome_dic))


# In[6]:


a = input()
b = input()

print(f'a + b = {a +b}')
print(f'a + b = {int(a) + int(b)}')


# In[ ]:




