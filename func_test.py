list_a = [122, 12123]
ab = {}
set_a = set('')

def func(list_a, ab, set_a):
    list_a += [444, 5555]
    ab['name'] = 111
    set_a.add(1222)
func(list_a, ab, set_a)

print(list_a)
print(ab)
print(set_a)