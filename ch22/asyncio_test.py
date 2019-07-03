import asyncio
import aiohttp
import time

async def download_one(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, ssl=False) as resp:
            print(resp.content)
            print('Read {} from {}'.format(resp.content_length, url))
        
async def download_all(urls):
    tasks = [asyncio.create_task(download_one(url)) for url in urls]
    await asyncio.gather(*tasks)

def main():
    sites = [
        #'https://docs.python.org/zh-cn/3/reference/index.html',
        'http://docs.python.org/3/tutorial/index.html',
        'http://docs.python.org/3/tutorial/appetite.html'
        'https://docs.python.org/3/tutorial/interpreter.html',
        'https://docs.python.org/3/tutorial/introduction.html',
        'https://docs.python.org/3/tutorial/controlflow.html',
        'https://docs.python.org/3/tutorial/datastructures.html',
        'https://docs.python.org/3/tutorial/modules.html',
        'https://docs.python.org/3/tutorial/inputoutput.html'
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
    asyncio.run(download_all(sites))
    end_time = time.perf_counter()
    print('Download {} sites in {} seconds'.format(len(sites), end_time - start_time))

if __name__ == '__main__':
    main()