#%%
import requests
import time

def download_one(url):
    resp = requests.get(url)
    print('Read {} from {}'.format(len(resp.content), url))

def download_all(urls):
    for url in urls:
        download_one(url)
        
def main():
    sites = [
        'https://docs.python.org/3/tutorial/index.html',
        'https://docs.python.org/3/tutorial/appetite.html',
        'https://docs.python.org/3/tutorial/interpreter.html',
        'https://docs.python.org/3/tutorial/introduction.html',
        'https://docs.python.org/3/tutorial/controlflow.html',
        'https://docs.python.org/3/tutorial/datastructures.html',
        'https://docs.python.org/3/tutorial/modules.html',
        'https://docs.python.org/3/tutorial/inputoutput.html',
        'https://docs.python.org/3/tutorial/errors.html',
        'https://docs.python.org/3/tutorial/classes.html',
        'https://docs.python.org/3/tutorial/stdlib.html',
        'https://docs.python.org/3/tutorial/stdlib2.html',
        'https://docs.python.org/3/tutorial/venv.html',
        'https://docs.python.org/3/tutorial/whatnow.html',
        'https://docs.python.org/3/tutorial/interactive.html',
        'https://docs.python.org/3/tutorial/floatingpoint.html',
        'https://docs.python.org/3/tutorial/appendix.html',
    ]
    start_time = time.perf_counter()
    download_all(sites)
    end_time = time.perf_counter()
    print('Download {} sites in {} seconds'.format(len(sites), end_time - start_time))
    
main()
#%%
import concurrent.futures
import requests
import threading
import time

def download_one(url):
    resp = requests.get(url)
    print('Read {} from {}'.format(len(resp.content), url))

def download_all(urls):
    #with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(download_one, urls)

def main():
    sites = [
        'https://docs.python.org/3/tutorial/index.html',
        'https://docs.python.org/3/tutorial/appetite.html',
        'https://docs.python.org/3/tutorial/interpreter.html',
        'https://docs.python.org/3/tutorial/introduction.html',
        'https://docs.python.org/3/tutorial/controlflow.html',
        'https://docs.python.org/3/tutorial/datastructures.html',
        'https://docs.python.org/3/tutorial/modules.html',
        'https://docs.python.org/3/tutorial/inputoutput.html',
        'https://docs.python.org/3/tutorial/errors.html',
        'https://docs.python.org/3/tutorial/classes.html',
        'https://docs.python.org/3/tutorial/stdlib.html',
        'https://docs.python.org/3/tutorial/stdlib2.html',
        'https://docs.python.org/3/tutorial/venv.html',
        'https://docs.python.org/3/tutorial/whatnow.html',
        'https://docs.python.org/3/tutorial/interactive.html',
        'https://docs.python.org/3/tutorial/floatingpoint.html',
        'https://docs.python.org/3/tutorial/appendix.html',
    ]
    start_time = time.perf_counter()
    download_all(sites)
    end_time = time.perf_counter()
    print('Download {} sites in {} seconds'.format(len(sites), end_time - start_time))

if __name__ == '__main__':
    main()

#%%
import concurrent.futures
import requests
import time

def download_one(url):
    try:
        resp = requests.get(url)
        print(f'Read {len(resp.content)} from {url}')
    except requests.ConnectionError as nce:
        print(f"Failed to Read {url},the reason is {nce}")
    except requests.Timeout as timeout:
        print(f"Failed to Read {url},the reason is {timeout}")
    except requests.RequestException as err:
        print(f"Failed to Read {url},the reason is {err}")

def download_all(urls):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        to_do = []
        for url in urls:
            future = executor.submit(download_one, url)
            to_do.append(future)
        try:
            for future in concurrent.futures.as_completed(to_do):
                future.result()
        except concurrent.futures.TimeoutError as timeout:
            print(f"Failed to Read {url}, the reason is {timeout}")

def main():
    sites = [
        'https://docs.python.org/3/tutorial/index.html',
        'https://docs.python.org/3/tutorial/appetite.html',
        'https://docs.python.org/3/tutorial/interpreter.html',
        'https://docs.python.org/3/tutorial/introduction.html',
        'https://docs.python.org/3/tutorial/controlflow.html',
        'https://docs.python.org/3/tutorial/datastructures.html',
        'https://docs.python.org/3/tutorial/modules.html',
        'https://docs.python.org/3/tutorial/inputoutput.html',
        'https://docs.python.org/3/tutorial/errors.html',
        'https://docs.python.org/3/tutorial/classes.html',
        'https://docs.python.org/3/tutorial/stdlib.html',
        'https://docs.python.org/3/tutorial/stdlib2.html',
        'https://docs.python.org/3/tutorial/venv.html',
        'https://docs.python.org/3/tutorial/whatnow.html',
        'https://docs.python.org/3/tutorial/interactive.html',
        'https://docs.python.org/3/tutorial/floatingpoint.html',
        'https://docs.python.org/3/tutorial/appendix.html',
    ]
    start_time = time.perf_counter()
    download_all(sites)
    end_time = time.perf_counter()
    print('Download {} sites in {} seconds'.format(len(sites), end_time - start_time))

if __name__ == '__main__':
    main()




#%%
