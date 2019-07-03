# 多进程版本计算列表的平方和
import time
from multiprocessing import Pool

def square_cus(i):
    return i ** 2

def cpu_bound(number):
    return sum(i ** 2 for i in range(0, number))

def calc_sums(numbers):
    with Pool(processes=4) as pool:
        print(pool.map(cpu_bound, numbers))

def main():
    start_time = time.perf_counter()
    numbers = [10000000 + x for x in range(20)]
    calc_sums(numbers)
    end_time = time.perf_counter()
    print('calc_sums takes {} seconds'.format(end_time - start_time))

main()
