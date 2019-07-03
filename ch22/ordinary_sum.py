# 计算0到这个元素的所有的平方和
import time
def cpu_bound(number):
    print(sum(i ** 2 for i in range(0, number)))

def calc_sums(numbers):
    for number in numbers:
        cpu_bound(number)

def main():
    start_time = time.perf_counter()
    numbers = [10000000 + x for x in range(20)]
    calc_sums(numbers)
    end_time = time.perf_counter()
    print('calc_sums takes {} seconds'.format(end_time - start_time))

main()