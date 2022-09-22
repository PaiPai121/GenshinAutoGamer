import asyncio
import vgamepad as vg
import random
class GamepadTaskHandler():
    def __init__(self,gamepad = None) -> None:
        self.gamepad = gamepad 
    # O
    async def pressButtonCircle(self,mode = 0):
        print("press button Circle")
        # # await asyncio.sleep(1)
        # print("release button Circle")
        # 0 快速按下，约150ms后释放
        if mode == 0:
            self.gamepad.press_button(vg.DS4_BUTTONS.DS4_BUTTON_CIRCLE)
            await asyncio.sleep(0.15)
            self.gamepad.release_button(vg.DS4_BUTTONS.DS4_BUTTON_CIRCLE)
            print("release button Circle")
        # 1 仅按下
        if mode == 1:
            self.gamepad.press_button(vg.DS4_BUTTONS.DS4_BUTTON_CIRCLE)
        
        # 2 仅松开
        if mode == 2:
            self.gamepad.release_button(vg.DS4_BUTTONS.DS4_BUTTON_CIRCLE)
        


    # X
    async def pressButtonCross(self,mode = 0):
        print("press button Cross")
        # await asyncio.sleep(1)
        # print("release button Cross")

        # 0 快速按下，约150ms后释放
        if mode == 0:
            self.gamepad.press_button(vg.DS4_BUTTONS.DS4_BUTTON_CROSS)
            await asyncio.sleep(0.125+random.randint(50)/1000)
            self.gamepad.release_button(vg.DS4_BUTTONS.DS4_BUTTON_CROSS)
        # 1 仅按下
        if mode == 1:
            self.gamepad.press_button(vg.DS4_BUTTONS.DS4_BUTTON_CROSS)
        
        # 2 仅松开
        if mode == 2:
            self.gamepad.release_button(vg.DS4_BUTTONS.DS4_BUTTON_CROSS)

    # []
    async def pressButtonSquare(self,mode = 0):
        # 0 快速按下，约150ms后释放
        if mode == 0:
            self.gamepad.press_button(vg.DS4_BUTTONS.DS4_BUTTON_SQUARE)
            await asyncio.sleep(0.125+random.randint(50)/1000)
            self.gamepad.release_button(vg.DS4_BUTTONS.DS4_BUTTON_SQUARE)
        # 1 仅按下
        if mode == 1:
            self.gamepad.press_button(vg.DS4_BUTTONS.DS4_BUTTON_SQUARE)
        
        # 2 仅松开
        if mode == 2:
            self.gamepad.release_button(vg.DS4_BUTTONS.DS4_BUTTON_SQUARE)
        # print("press button Square")
        # await asyncio.sleep(1)
        # print("release button Square")

    # Tri
    async def pressButtonTriangle(self,mode = 0):
        # 0 快速按下，约150ms后释放
        if mode == 0:
            self.gamepad.press_button(vg.DS4_BUTTONS.DS4_BUTTON_TRIANGLE)
            await asyncio.sleep(0.125+random.randint(50)/1000)
            self.gamepad.release_button(vg.DS4_BUTTONS.DS4_BUTTON_TRIANGLE)
        # 1 仅按下
        if mode == 1:
            self.gamepad.press_button(vg.DS4_BUTTONS.DS4_BUTTON_TRIANGLE)
        
        # 2 仅松开
        if mode == 2:
            self.gamepad.release_button(vg.DS4_BUTTONS.DS4_BUTTON_TRIANGLE)
        # print("press button Triangle")
        # await asyncio.sleep(1)
        # print("release button Triangle")

    # up
    async def pressButtonDpadUp(self,mode = 0):
        # 0 快速按下，约150ms后释放
        if mode == 0:
            self.gamepad.press_button(vg.DS4_DPAD_DIRECTIONS.DS4_BUTTON_DPAD_NORTH)
            await asyncio.sleep(0.125+random.randint(50)/1000)
            self.gamepad.release_button(vg.DS4_DPAD_DIRECTIONS.DS4_BUTTON_DPAD_NORTH)
        # 1 仅按下
        if mode == 1:
            self.gamepad.press_button(vg.DS4_DPAD_DIRECTIONS.DS4_BUTTON_DPAD_NORTH)
        
        # 2 仅松开
        if mode == 2:
            self.gamepad.release_button(vg.DS4_DPAD_DIRECTIONS.DS4_BUTTON_DPAD_NORTH)

        # print("press button O")
        # await asyncio.sleep(1)
        # print("release button O")

    # down
    async def pressButtonDpadDown(self,mode = 0):
        # 0 快速按下，约150ms后释放
        if mode == 0:
            self.gamepad.press_button(vg.DS4_DPAD_DIRECTIONS.DS4_BUTTON_DPAD_SOUTH)
            await asyncio.sleep(0.125+random.randint(50)/1000)
            self.gamepad.release_button(vg.DS4_DPAD_DIRECTIONS.DS4_BUTTON_DPAD_SOUTH)
        # 1 仅按下
        if mode == 1:
            self.gamepad.press_button(vg.DS4_DPAD_DIRECTIONS.DS4_BUTTON_DPAD_SOUTH)
        
        # 2 仅松开
        if mode == 2:
            self.gamepad.release_button(vg.DS4_DPAD_DIRECTIONS.DS4_BUTTON_DPAD_SOUTH)
        # print("press button X")
        # await asyncio.sleep(1)
        # print("release button X")

    # left
    async def pressButtonDpadLeft(self,mode = 0):
        # print("press button Square")
        # await asyncio.sleep(1)
        # print("release button Square")
        # 0 快速按下，约150ms后释放
        if mode == 0:
            self.gamepad.press_button(vg.DS4_DPAD_DIRECTIONS.DS4_BUTTON_DPAD_WEST)
            await asyncio.sleep(0.125+random.randint(50)/1000)
            self.gamepad.release_button(vg.DS4_DPAD_DIRECTIONS.DS4_BUTTON_DPAD_WEST)
        # 1 仅按下
        if mode == 1:
            self.gamepad.press_button(vg.DS4_DPAD_DIRECTIONS.DS4_BUTTON_DPAD_WEST)
        
        # 2 仅松开
        if mode == 2:
            self.gamepad.release_button(vg.DS4_DPAD_DIRECTIONS.DS4_BUTTON_DPAD_WEST)


    # right
    async def pressButtonDpadRight(self,mode = 0):
        print("press button DpadRight")
        # await asyncio.sleep(1)
        # print("release button DpadRight")
        # 0 快速按下，约150ms后释放
        if mode == 0:
            self.gamepad.press_button(vg.DS4_DPAD_DIRECTIONS.DS4_BUTTON_DPAD_EAST)
            await asyncio.sleep(0.125+random.randint(50)/1000)
            self.gamepad.release_button(vg.DS4_DPAD_DIRECTIONS.DS4_BUTTON_DPAD_EAST)
        # 1 仅按下
        if mode == 1:
            self.gamepad.press_button(vg.DS4_DPAD_DIRECTIONS.DS4_BUTTON_DPAD_EAST)
        
        # 2 仅松开
        if mode == 2:
            self.gamepad.release_button(vg.DS4_DPAD_DIRECTIONS.DS4_BUTTON_DPAD_EAST)




    # left stick
    async def setLeftStick(self,x=0,y=0):
        # print("turn left stick")
        self.gamepad.right_joystick_float(x,y)

    # right stick
    async def setRightStick(self,x=0,y=0):
        # print("turn right stick")
        self.gamepad.right_joystick_float(x,y)
        
    # left shoulder
    async def pressButtonShoulderLeft(self,mode = 0):
        # 0 快速按下，约150ms后释放
        if mode == 0:
            self.gamepad.press_button(vg.DS4_BUTTONS.DS4_BUTTON_SHOULDER_LEFT)
            await asyncio.sleep(0.125+random.randint(50)/1000)
            self.gamepad.release_button(vg.DS4_BUTTONS.DS4_BUTTON_SHOULDER_LEFT)
        # 1 仅按下
        if mode == 1:
            self.gamepad.press_button(vg.DS4_BUTTONS.DS4_BUTTON_SHOULDER_LEFT)
        
        # 2 仅松开
        if mode == 2:
            self.gamepad.release_button(vg.DS4_BUTTONS.DS4_BUTTON_SHOULDER_LEFT)

    # right shoulder
    async def pressButtonShoulderRight(self,mode = 0):
        # 0 快速按下，约150ms后释放
        if mode == 0:
            self.gamepad.press_button(vg.DS4_BUTTONS.DS4_BUTTON_SHOULDER_RIGHT)
            await asyncio.sleep(0.125+random.randint(50)/1000)
            self.gamepad.release_button(vg.DS4_BUTTONS.DS4_BUTTON_SHOULDER_RIGHT)
        # 1 仅按下
        if mode == 1:
            self.gamepad.press_button(vg.DS4_BUTTONS.DS4_BUTTON_SHOULDER_RIGHT)
        
        # 2 仅松开
        if mode == 2:
            self.gamepad.release_button(vg.DS4_BUTTONS.DS4_BUTTON_SHOULDER_RIGHT)

    # left trigger
    async def pressButtonTriggerLeft(self,mode = 0):
        # 0 快速按下，约150ms后释放
        if mode == 0:
            self.gamepad.press_button(vg.DS4_BUTTONS.DS4_BUTTON_TRIGGER_LEFT)
            await asyncio.sleep(0.125+random.randint(50)/1000)
            self.gamepad.release_button(vg.DS4_BUTTONS.DS4_BUTTON_TRIGGER_LEFT)
        # 1 仅按下
        if mode == 1:
            self.gamepad.press_button(vg.DS4_BUTTONS.DS4_BUTTON_TRIGGER_LEFT)
        
        # 2 仅松开
        if mode == 2:
            self.gamepad.release_button(vg.DS4_BUTTONS.DS4_BUTTON_TRIGGER_LEFT)

    # right trigger
    async def pressButtonTriggerRight(self,mode = 0):
        # 0 快速按下，约150ms后释放
        if mode == 0:
            self.gamepad.press_button(vg.DS4_BUTTONS.DS4_BUTTON_TRIGGER_LEFT)
            await asyncio.sleep(0.125+random.randint(50)/1000)
            self.gamepad.release_button(vg.DS4_BUTTONS.DS4_BUTTON_TRIGGER_LEFT)
        # 1 仅按下
        if mode == 1:
            self.gamepad.press_button(vg.DS4_BUTTONS.DS4_BUTTON_TRIGGER_LEFT)
        
        # 2 仅松开
        if mode == 2:
            self.gamepad.release_button(vg.DS4_BUTTONS.DS4_BUTTON_TRIGGER_LEFT)

    def pressCross(self,mode = 0):
        self.queueCross.put_nowait(self.pressButtonCross(mode))
    
    def pressSquare(self,mode = 0):
        self.queueSquare.put_nowait(self.pressButtonSquare(mode))

    def pressCircle(self,mode = 0):
        self.queueCircle.put_nowait(self.pressButtonCircle(mode))

    async def production_tasks(self): #,queueLeftStick,queueRightStick,queueCross,queueCircle,queueSquare,queueTriangle,queueDpadUp,queueDpadDown,queueDpadLeft,queueDpadRight,queueShoulderLeft,queueShoulderRight,queueTriggerLeft,queueTriggerRight):
        # queueCross.put_nowait(self.pressButtonCross())
        # queueDpadRight.put_nowait(self.pressButtonDpadRight())
        self.pressCross()
        # self.pressSquare()
        await asyncio.sleep(1)
        self.pressCircle()
        # queueCross.put_nowait(self.pressButtonCross())
        

    async def consumer(self,queue):
        while True:
            # 从队列中取出任务

            task = await queue.get()
            # 处理任务
            await task
            # 通知队列任务已被处理完成
            queue.task_done()




    async def queueHandle(self):
        # 创建 先进先出（FIFO）队列
        self.queueLeftStick = asyncio.Queue(10)
        self.queueRightStick = asyncio.Queue(10)
        self.queueCross = asyncio.Queue(10)
        self.queueCircle = asyncio.Queue(10)
        self.queueSquare = asyncio.Queue(10)
        self.queueTriangle = asyncio.Queue(10)
        self.queueDpadUp = asyncio.Queue(10)
        self.queueDpadDown = asyncio.Queue(10)
        self.queueDpadLeft = asyncio.Queue(10)
        self.queueDpadRight = asyncio.Queue(10)
        self.queueShoulderLeft = asyncio.Queue(10)
        self.queueShoulderRight = asyncio.Queue(10)
        self.queueTriggerLeft = asyncio.Queue(10)
        self.queueTriggerRight = asyncio.Queue(10)
        # 创建异步 生产任务
        consumerTask = asyncio.create_task(self.production_tasks( ))#queueLeftStick,queueRightStick ,queueCross,queueCircle,queueSquare,queueTriangle,queueDpadUp,queueDpadDown,queueDpadLeft,queueDpadRight,queueShoulderLeft,queueShoulderRight,queueTriggerLeft,queueTriggerRight))
        # 创建异步 消费任务
        leftStickTask = asyncio.create_task(self.consumer(self.queueLeftStick))
        
        rightStickTask = asyncio.create_task(self.consumer(self.queueRightStick))
        
        crossTask = asyncio.create_task(self.consumer(self.queueCross))

        circleTask = asyncio.create_task(self.consumer(self.queueCircle))

        squareTask = asyncio.create_task(self.consumer(self.queueSquare))

        triangleTask = asyncio.create_task(self.consumer(self.queueTriangle))

        dpadUpTask = asyncio.create_task(self.consumer(self.queueDpadUp))

        dpadDownTask = asyncio.create_task(self.consumer(self.queueDpadDown))

        dpadLeftTask = asyncio.create_task(self.consumer(self.queueDpadLeft))

        dpadRightTask = asyncio.create_task(self.consumer(self.queueDpadRight))
        
        shoulderLeftTask =asyncio.create_task(self.consumer(self.queueShoulderLeft))
        
        shoulderRightTask = asyncio.create_task(self.consumer(self.queueShoulderRight))
        
        triggerLeftTask = asyncio.create_task(self.consumer(self.queueTriggerLeft))
        
        triggerRightTask = asyncio.create_task(self.consumer(self.queueTriggerRight))

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
        await shoulderLeftTask
        await shoulderRightTask
        await triggerLeftTask
        await triggerRightTask


    async def setGamepadStatus(self,message = []):
        '''改变gamepad的状态'''
        while True:
            print("try to set gamepad")
            await asyncio.sleep(1)


    async def updateGamepad(self,dt):
        while True:
            self.gamepad.update()
            # print("update gamepad")
            await asyncio.sleep(dt)
            # 这里可以设置一个检测按键的开关
        
    async def mainGamePad(self,dt):
        await asyncio.gather(
            self.updateGamepad(dt),
            self.setGamepadStatus(),
            self.queueHandle()
        )

    def run(self):
        asyncio.run(self.mainGamePad(1/120))
if __name__ == "__main__":
    GPHD = GamepadTaskHandler(vg.VDS4Gamepad())
    GPHD.run()
