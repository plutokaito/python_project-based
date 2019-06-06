import json

dict_a = {
    'name':'kaito',
    'age':30,
    'height':175.4,
}

str = json.dumps(dict_a)
print(f"type is:{type(str)}")

dict_b = json.loads(str)
print(f"type is:{type(dict_b)}")

str_test = "sdfdfasdfdsfds"
dict_c = json.loads(str_test)
print(f"type is {type(dict_c)}")