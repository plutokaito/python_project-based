#%%
def CountDown(n):
    while n > 0:
        n -= 1

%time CountDown(100000000)

#%%
from threading import Thread

def CountDown(n):
    while n > 0:
        n -= 1

def main():
    n = 100000000
    t1 = Thread(target=CountDown, args=[n//2])
    t2 = Thread(target=CountDown, args=[n//2])
    t1.start()
    t2.start()
    t1.join()
    t2.join()

%time main()

#%%
import sys
a = []
b = a
sys.getrefcount(a)

#%%
import threading

n = 0
def foo():
    global n
    n += 1
threads = []
for i in range(100):
    t = threading.Thread(target=foo)
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()

n

#%%
import dis
#n = 0
def foo():
    global n
    n += 1
dis.dis(foo)

#%%
import threading

n = 0
lock = threading.Lock()
def foo():
    global n
    with lock:
        n += 1
threads = []
for i in range(100):
    t = threading.Thread(target=foo)
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()

n

#%%
