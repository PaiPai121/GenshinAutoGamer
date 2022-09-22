# import asyncio
# import time
# # async def consumer(n,q):
# #     print("consumer {}:starting".format(n))
# #     while True:
# #         print('consumer {}: waiting for item'.format(n))
# #         item = await q.get()
# #         print('consumer {}: has item {}'.format(n,item))
# #         if item is None:
# #             q.task_done()
# #             break
# #         else:
# #             await asyncio.sleep(0.01 * item)
# #             q.task_done()
# #         print('consumer {}: ending'.format(n))

# # async def producer(buttonQ,stickQ, num_workers):
# #     print ( 'producer : starting')
# #     for i in range(1):
# #         await buttonQ.put(i)
# #         print('producer: added task {} to the queue {}'.format(i,"buttonQ"))
# #     for i in range(1):
# #         await stickQ.put(i)
# #         print('producer: added task {} to the queue {}'.format(i,"stickQ"))
# #     print('producer: adding stop signals to the queue')
# #     for i in range(1):
# #         await buttonQ.put(None)
# #     print('producer : waiting for queue to empty')
# #     await buttonQ.join()
# #     print("producer:ending")

# # async def main(loop,num_consumers):
# #     buttonQ = asyncio.Queue(maxsize = 5)
# #     StickQ = asyncio.Queue(maxsize = 5)
# #     consumers = [
# #         loop.create_task(consumer(i,[buttonQ,StickQ])) for i in ["ButtonControl","StickControl"]
# #     ]

# #     prod = loop.create_task(producer(buttonQ,StickQ,num_consumers))

# #     await asyncio.wait(consumers + [prod])

# # event_loop = asyncio.get_event_loop()
# # try:
# #     event_loop.run_until_complete(main(event_loop,2))
# # finally:
# #     event_loop.close()

# import random

# async def pressButton():
#     print("press Button")
#     await asyncio.sleep(1)
#     print("release Button")

# async def controlStick():
#     print("stick move")

# async def produce(queue,n):
#     for x in range(n):
#         print('producing {}/{}'.format(x,n))
#         await asyncio.sleep(random.random())
#         item = pressButton()# str(x)
#         await queue.put(item)


# async def consume(queue):
#     while True:
#         item = await queue.get()
#         await item
#         # print ( 'consuming {}...'.format(item))

#         await asyncio.sleep(random.random())

#         queue.task_done()

# async def run(n):
#     queue = asyncio.Queue()
#     consumer = asyncio.ensure_future(consume(queue))
#     await produce(queue,n)
#     await queue.join()
#     consumer.cancel()

# loop = asyncio.get_event_loop()
# loop.run_until_complete(run(10))
# loop.close()

import asyncio


async def pressButton(button = "x"):
    print("press Button {}".format(button))
    await asyncio.sleep(1)
    print("release Button")

async def controlStick():
    print("stick move")
    await asyncio.sleep(1)
    print("release stick")


# async def mul(first, second):

#     print(f"Calculating multiply of {first} and {second}")

#     await asyncio.sleep(1)

#     num_mul = first * second

#     print(f"Multiply is {num_mul}")

#     return num_mul

# async def sum(first, second):

#     print(f"Calculating sum of {first} and {second}")

#     await asyncio.sleep(1)

#     num_sum = first + second

#     print(f"Sum is {num_sum}")

#     return num_sum

# async def main(first, second):

#     sum_task = asyncio.create_task(sum(first, second))

#     mul_task = asyncio.create_task(mul(first, second))

#     for i in [sum_task,mul_task]:
#         await i
#     # await sum_task

#     # await mul_task

    

# asyncio.run(main(7, 8))
import asyncio
import random
import time


async def worker(name, queue):
    while True:
        # Get a "work item" out of the queue.
        sleep_for = await queue.get()

        # Sleep for the "sleep_for" seconds.
        await asyncio.sleep(sleep_for)

        # Notify the queue that the "work item" has been processed.
        queue.task_done()

        print(f'{name} has slept for {sleep_for:.2f} seconds')


async def main():
    # Create a queue that we will use to store our "workload".
    queue = asyncio.Queue()

    # Generate random timings and put them into the queue.
    total_sleep_time = 0
    for _ in range(20):
        sleep_for = random.uniform(0.05, 1.0)
        total_sleep_time += sleep_for
        queue.put_nowait(sleep_for)

    # Create three worker tasks to process the queue concurrently.
    tasks = []
    for i in range(3):
        task = asyncio.create_task(worker(f'worker-{i}', queue))
        tasks.append(task)

    # Wait until the queue is fully processed.
    started_at = time.monotonic()
    await queue.join()
    total_slept_for = time.monotonic() - started_at

    # Cancel our worker tasks.
    # for task in tasks:
    #     task.cancel()
    # Wait until all worker tasks are cancelled.
    await asyncio.gather(*tasks, return_exceptions=True)

    print('====')
    print(f'3 workers slept in parallel for {total_slept_for:.2f} seconds')
    print(f'total expected sleep time: {total_sleep_time:.2f} seconds')


asyncio.run(main())