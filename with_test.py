#%% 
for  x in range(10000000):
    f = open('text.txt', 'w')
    f.write('hello')

#%%
for x in range(100000000):
    with open('test.txt', 'w') as f:
        f.write('hello')

#%%
class FileManager:
    def __init__(self, name, mode):
        print('calling __init__ method')
        self.name = name
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        print('calling __enter__ method')
        self.file = open(self.name, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('calling __exit__ method')
        if self.file:
            self.file.close()

with FileManager('text.txt', 'w') as f:
    print('Ready to write to file')
    f.write('hello world')


#%%
from contextlib import contextmanager

@contextmanager
def file_manager(name, mode):
    try:
        f = open(name, mode)
        yield f
    finally:
        print('完成操作')
        f.close()


with file_manager('test.txt', 'w') as f:
    f.write('hello world')

#%%
