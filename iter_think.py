def is_iterable(param):
    try:
        iter(param)
        return True
    except TypeError:
        return False

params = [
    12345,
    '12345',
    [1, 3, 4, 5, 10],
    set([1, 3, 4, 5]),
    {1:1, 2:2, 3:3},
    (1, 3, 4)
]

for param in params:
    print("{} is iterable?  {}".format(param, is_iterable(param)))