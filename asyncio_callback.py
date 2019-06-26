import asyncio

async def sleep():
    print('func sleep is start')
    await asyncio.sleep(1)
    print('func sleep is over')
    return 'stop'

async def continue_sleep():
    print('i wanna to sleep again')
    await asyncio.sleep(2)

def callback_test(future):
    print('Callback: {}'.format(future.result()))

async def main():
    task_1 = asyncio.create_task(sleep())
    task_2 = asyncio.create_task(continue_sleep())

    done, pending = await asyncio.wait({task_1, task_2})
    if task_1 in done:
        task_1.add_done_callback(callback_test)

asyncio.run(main())