# a = range(1, 10000)
# for i, index in enumerate(a):
#     print(f"{i}===={index}")

# expected outout:
#[{'name': 'jason', 'dob': '2000-01-01', 'gender': 'male'},
#{'name': 'mike', 'dob': '1999-01-01', 'gender': 'male'},
#{'name': 'nancy', 'dob': '2001-02-01', 'gender': 'female'}]
## 思考题：zip() 函数
attributes = ['name', 'dob', 'gender']
values = [['jason', '2000-01-01', 'male'],
['mike', '1999-01-01', 'male'],
['nancy', '2001-02-01', 'female']
]

alist = [];
for value in values:
    tmp_dict = {}
    for key,element in enumerate(value):
        tmp_dict[attributes[key]] = element
    alist.append(tmp_dict)

print(alist)

blist = [{attributes[key]:element} for value in values for key,element in enumerate(value)]
print(alist)

clist = []
for value in values:
    clist.append(dict(zip(attributes, value)))
print(clist)

dlist = [dict(zip(attributes, value)) for value in values]