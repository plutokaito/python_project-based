from functools import wraps

def fib_cache(fn):
    cache = {}
    miss = object()
    @wraps(fn)
    def real_decorater(*args):
        result = cache.get(args, miss)
        if  result is miss:
            result = fn(*args)
            cache[args] = result
        return result
    return real_decorater


@fib_cache
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

print(fib(6))