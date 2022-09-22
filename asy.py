# import asyncio
# import subprocess
# import time

# async def first():
#     print('first begin')
#     await asyncio.sleep(3)
#     print('first finish')

# async def func1(delay):
#     for i in range(10):
#         print("func 1:")
#         print(i)
#         print("\n")
#         await asyncio.sleep(delay)

# async def func2(delay):
#     for i in range(10):
#         print("func 2:")
#         print(i)
#         print("\n")
#         await asyncio.sleep(delay)

# async def main():
#     await  first()
#     await asyncio.gather(
#         func1(1),
#         func2(2)
#     )

# asyncio.run(main())


# coding:utf-8

import asyncio
import time
async def testa(x):
    print("in test a")
    await asyncio.sleep(3)
    print("Resuming a")
    return x


async def testb(x):
    print("in test b")
    await asyncio.sleep(1)
    print('Resuming b')
    return x


async def main():
    start = time.time()

    taska = asyncio.create_task(testa(1))
    taskb = asyncio.create_task(testb(2))
    taskc = asyncio.create_task(testa(1))
    # print(taska)
    # print(taskb)
    # print(taska.done(), taskb.done())
    # await taskb
    # await taska
    # print(taska.done(), taskb.done())
    asyncio.sleep(5)
    # print(taskb.result())
    # print(taska.result())
    # print("use %s time" % (time.time() - start))

if __name__ == '__main__':
    asyncio.run(main())
    # asyncio.run(testb(2))
    

import asyncio
import random
async def pushButton(gamepad,button,keepTime = 0.2):
    gamepad.press_button(button)
    await asyncio.sleep(keepTime+random.randint(0,50)/1000)
    gamepad.release_button(button)
    
async def moveStick(stick,valuex=1,valuey=1,keepTime = 1):
    stick(valuex,valuey)
    stick(0,0)

async def updateGamepad(gamepad,dt):
    while True:
        # gamepad.update()
        await asyncio.sleep(dt)
        # 这里可以设置一个检测按键的开关

queue = []

async def queueHandler():
    if queue:
        task = queue.pop(0)
        asyncio.create_task(task)
async def setGamepadStatus(gamepad,message = []):
    '''改变gamepad的状态'''

    # tasks = []
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete()
    
    
async def mainGamePad(gamepad,dt):
    await asyncio.gather(
        updateGamepad(gamepad,dt),
        setGamepadStatus(gamepad)
    )

# while True:
#     asyncio.run(mainGamePad(None,1/120))
