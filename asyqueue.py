import asyncio


# O
async def pressButtonCircle():
    print("press button Circle")
    await asyncio.sleep(1)
    print("release button Circle")

# X
async def pressButtonCross():
    print("press button Cross")
    await asyncio.sleep(1)
    print("release button Cross")

# []
async def pressButtonSquare():
    print("press button Square")
    await asyncio.sleep(1)
    print("release button Square")

# Tri
async def pressButtonTriangle():
    print("press button Triangle")
    await asyncio.sleep(1)
    print("release button Triangle")

# up
async def pressButtonDpadUp():
    print("press button O")
    await asyncio.sleep(1)
    print("release button O")

# down
async def pressButtonDpadDown():
    print("press button X")
    await asyncio.sleep(1)
    print("release button X")

# left
async def pressButtonDpadLeft():
    print("press button Square")
    await asyncio.sleep(1)
    print("release button Square")

# right
async def pressButtonDpadRight():
    print("press button Triangle")
    await asyncio.sleep(1)
    print("release button Triangle")


# left stick
async def setLeftStick(x=0,y=0):
    print("turn left stick")

# right stick
async def setRightStick(x=0,y=0):
    print("turn right stick")


async def production_tasks(queueLeftStick,queueRightStick,queueCross,queueCircle,queueSquare,queueTriangle,queueDpadUp,queueDpadDown,queueDpadLeft,queueDpadRight):
    # for i in range(5):
    #     # 创建任务
    #     task = Task(random.uniform(1.0, 2.0), f"T{i}")
    #     # 添加任务到队列中
    #     await queue.put(task)
    # asyncio.sleep(5)
    # for i in range(5):
    #         # 创建任务
    #     task = Task(random.uniform(1.0, 2.0), f"T{i}")
    #     # 添加任务到队列中
    #     await queue.put(task)
    queueCross.put_nowait(pressButtonCross())
    queueCircle.put_nowait(pressButtonCircle())
    queueSquare.put_nowait(pressButtonSquare())
    queueTriangle.put_nowait(pressButtonTriangle())
    queueDpadUp.put_nowait(pressButtonDpadUp())
    queueDpadDown.put_nowait(pressButtonDpadDown())
    queueDpadLeft.put_nowait(pressButtonDpadLeft())
    queueDpadRight.put_nowait(pressButtonDpadRight())
    queueLeftStick.put_nowait(setLeftStick())
    queueRightStick.put_nowait(setRightStick())
    await asyncio.sleep(6)

    queueCross.put_nowait(pressButtonCross())
    queueCircle.put_nowait(pressButtonCircle())
    queueSquare.put_nowait(pressButtonSquare())
    queueTriangle.put_nowait(pressButtonTriangle())
    queueDpadUp.put_nowait(pressButtonDpadUp())
    queueDpadDown.put_nowait(pressButtonDpadDown())
    queueDpadLeft.put_nowait(pressButtonDpadLeft())
    queueDpadRight.put_nowait(pressButtonDpadRight())
    queueLeftStick.put_nowait(setLeftStick(10,20))
    queueRightStick.put_nowait(setRightStick(5,15))

async def consumer(queueCross):
    while True:
        # 从队列中取出任务
        task = await queueCross.get()
        # 处理任务
        await task
        # 通知队列任务已被处理完成
        queueCross.task_done()




async def queueHandle():
    # 创建 先进先出（FIFO）队列
    queueLeftStick = asyncio.Queue(10)
    queueRightStick = asyncio.Queue(10)
    queueCross = asyncio.Queue(10)
    queueCircle = asyncio.Queue(10)
    queueSquare = asyncio.Queue(10)
    queueTriangle = asyncio.Queue(10)
    queueDpadUp = asyncio.Queue(10)
    queueDpadDown = asyncio.Queue(10)
    queueDpadLeft = asyncio.Queue(10)
    queueDpadRight = asyncio.Queue(10)
    # 创建异步 生产任务
    consumerTask = asyncio.create_task(production_tasks(queueLeftStick,queueRightStick ,queueCross,queueCircle,queueSquare,queueTriangle,queueDpadUp,queueDpadDown,queueDpadLeft,queueDpadRight))
    # 创建异步 消费任务
    leftStickTask = asyncio.create_task(consumer(queueLeftStick))
    
    rightStickTask = asyncio.create_task(consumer(queueRightStick))
    
    crossTask = asyncio.create_task(consumer(queueCross))

    circleTask = asyncio.create_task(consumer(queueCircle))

    squareTask = asyncio.create_task(consumer(queueSquare))

    triangleTask = asyncio.create_task(consumer(queueTriangle))

    dpadUpTask = asyncio.create_task(consumer(queueDpadUp))

    dpadDownTask = asyncio.create_task(consumer(queueDpadDown))

    dpadLeftTask = asyncio.create_task(consumer(queueDpadLeft))

    dpadRightTask = asyncio.create_task(consumer(queueDpadRight))

    await leftStickTask
    await rightStickTask
    await consumerTask
    await crossTask
    await circleTask
    await squareTask 
    await triangleTask 
    await dpadUpTask
    await dpadDownTask
    await dpadLeftTask
    await dpadRightTask


async def setGamepadStatus(gamepad = None,message = []):
    '''改变gamepad的状态'''
    while True:
        print("try to set gamepad")
        await asyncio.sleep(1)


async def updateGamepad(gamepad,dt):
    while True:
        # gamepad.update()
        print("update gamepad")
        await asyncio.sleep(dt)
        # 这里可以设置一个检测按键的开关
    
async def mainGamePad(gamepad,dt):
    await asyncio.gather(
        updateGamepad(gamepad,dt),
        setGamepadStatus(gamepad),
        queueHandle()
    )

if __name__ == "__main__":
    asyncio.run(mainGamePad(None,1))
