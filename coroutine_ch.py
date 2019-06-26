#%%
import time

def crawl_page(url):
    print('crawling {}'.format(url))
    sleep_time = int(url.split('_')[-1])
    time.sleep(sleep_time)
    print('OK {}'.format(url))

def main(urls):
    for url in urls:
        crawl_page(url)

%time main(['url_1', 'url_2', 'url_3', 'url_4']) 

#%%
import asyncio
import nest_asyncio

nest_asyncio.apply()
async def crawl_page(url):
    print('crawling {}'.format(url))
    sleep_time = int(url.split('_')[-1])
    await asyncio.sleep(sleep_time)
    print('OK {}'.format(url))

async def main(urls):
    for url in urls:
        await crawl_page(url)

#result = await main(['url_1', 'url_2', 'url_3', 'url_4'])
#%time result
#asyncio.get_event_loop()
#print(crawl_page(' '))
%time asyncio.run(main(['url_1', 'url_2', 'url_3', 'url_4']))


#%%
import asyncio

async def crawl_page(url):
    print('crawling {}'.format(url))
    sleep_time = int(url.split('_')[-1])
    await asyncio.sleep(sleep_time)
    print('OK {}'.format(url))

async def main(urls):
    tasks = [asyncio.create_task(crawl_page(url)) for url in urls]
    # for task in tasks:
    #     await task
    await asyncio.gather(*tasks)
    
%time asyncio.run(main(['url_1', 'url_2', 'url_3', 'url_4']))


#%%
import asyncio 

async def worker_1():
    print('worker_1 start')
    await asyncio.sleep(1)
    print('worker_1 done')

async def worker_2():
    print('worker_2 start')
    await asyncio.sleep(2)
    print('worker_2 done')

async def worker_3():
    print('worker_3 start')
    await asyncio.sleep(3)
    print('worker_3 done')

async def main():
    print('before await')
    await worker_1()
    print('awaited work_1')
    await worker_2()
    print('awaited work_2')
    await worker_3()
    print('awaited work_3')

%time asyncio.run(main())

#%%
import asyncio 

async def worker_1():
    print('worker_1 start')
    await asyncio.sleep(1)
    print('worker_1 done')

async def worker_2():
    print('worker_2 start')
    await asyncio.sleep(2)
    print('worker_2 done')

async def main():
    task1 = asyncio.create_task(worker_1())
    task2 = asyncio.create_task(worker_2())
    print('before await')
    await task1
    print('awaited worker_1')
    await task2
    print('awaited worker_2')

%time  asyncio.run(main())

#%%
import asyncio

async def work_1():
    await  asyncio.sleep(1)
    return 1

async def work_2():
    await asyncio.sleep(2)
    return 2 / 0

async def work_3():
    await asyncio.sleep(3)
    return 3

async def main():
    task1 = asyncio.create_task(work_1())
    task2 = asyncio.create_task(work_2())
    task3 = asyncio.create_task(work_3())

    await asyncio.sleep(2)
    task3.cancel()

    res = await asyncio.gather(task1, task2, task3, return_exceptions=True)
    print(res)

%time asyncio.run(main())

#%%
import asyncio
import random 

async def consumer(queue, id):
    while True:
        val = await queue.get()
        print('{}获取的值是{}'.format(id, val))
        await asyncio.sleep(1)
    
async def producer(queue, id):
    for i in range(1, 5):
        val = random.randint(1, 10)
        await queue.put(val)
        print(f'{id}生产的值是{val}') 
        await asyncio.sleep(1)
    
async def main():
    queue = asyncio.Queue()

    consumer_1 = asyncio.create_task(consumer(queue, 'consumer_1'))
    consumer_2 = asyncio.create_task(consumer(queue, 'consumer_2'))
    producer_1 = asyncio.create_task(producer(queue, 'producer_1'))
    producer_2 = asyncio.create_task(producer(queue, 'producer_2'))

    await asyncio.sleep(10)

    consumer_1.cancel()
    consumer_2.cancel()

    await asyncio.gather(consumer_1, consumer_2, producer_1, producer_2, return_exceptions=True)

%time asyncio.run(main())

#%%
import requests
from bs4 import BeautifulSoup

def main():
    url = "http://movie.douban.com/cinema/later/hangzhou/"

    init_page = requests.get(url).content
    init_soup = BeautifulSoup(init_page, 'lxml')

    all_movies = init_soup.find('div', id="showing-soon")
    for each_movie in all_movies.find_all('div', class_='item'):
        all_a_tag = each_movie.find_all('a')
        all_li_tag = each_movie.find_all('li')

        movie_name = all_a_tag[1].text
        url_to_fetch = all_a_tag[1]['href']
        movie_date = all_li_tag[0].text

        response_item = requests.get(url_to_fetch).content
        soup_item =  BeautifulSoup(response_item, 'lxml')
        img_tag = soup_item.find('img')

        print('{} {} {}'.format(movie_name, movie_date, img_tag['src']))

%time main()
#%%
import asyncio
import aiohttp
import nest_asyncio
from bs4 import BeautifulSoup

nest_asyncio.apply()
# header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36
#  (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}
async def fetch_content(url):
    async with aiohttp.ClientSession(
        connector=aiohttp.TCPConnector(ssl=False)
    ) as session:
        async with session.get(url) as response:
            return await response.text()

async def main():
    url = 'http://movie.douban.com/cinema/later/hangzhou/'
    init_page = await fetch_content(url)
    init_soup = BeautifulSoup(init_page, 'lxml')
    movie_names,urls_to_fetch, movie_dates = [], [], []

    all_movies = init_soup.find('div', id="showing-soon")
    for each_movie in all_movies.find_all('div', class_="item"):
        all_a_tag = each_movie.find_all('a')
        all_li_tag = each_movie.find_all('li')

        movie_names.append(all_a_tag[1].text)
        urls_to_fetch.append(all_a_tag[1]['href'])
        movie_dates.append(all_li_tag[0].text)

    tasks = [fetch_content(url) for url in urls_to_fetch]
    pages = await asyncio.gather(*tasks)

    for movie_name, movie_date, page in zip(movie_names, movie_dates, pages):
        soup_item = BeautifulSoup(page, 'lxml')
        img_tag = soup_item.find('img')

        print('{} {} {}'.format(movie_name, movie_date, img_tag['src']))

%time asyncio.run(main())


#%%
import asyncio
import nest_asyncio
import functools

async def sleep():
    print('func sleep is start')
    await asyncio.sleep(1)
    print('func sleep is over')

async def continue_sleep():
    print('i wanna to sleep again')
    await asyncio.sleep(2)

def callback_test():
    print('Callback: stop')

async def main():
    loop = asyncio.get_event_loop()
    task_1 = asyncio.create_task(sleep())
    task_2 = asyncio.create_task(continue_sleep())

    done,pending = await asyncio.wait({task_1, task_2})
    if task_1 in done:
        print(task_1)
        task_1.add_done_callback(functools.partial(print, "Future:"))
    #print(done)
    # for task in done: 
    #     task_1.add_done_callback(callback_test)

nest_asyncio.apply()
%time asyncio.run(main())


#%%
