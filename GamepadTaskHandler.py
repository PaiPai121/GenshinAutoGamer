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
            # print("release button Circle")
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
            await asyncio.sleep(0.125)
            self.gamepad.release_button(vg.DS4_BUTTONS.DS4_BUTTON_CROSS)
        # 1 仅按下
        if mode == 1:
            self.gamepad.press_button(vg.DS4_BUTTONS.DS4_BUTTON_CROSS)
        
        # 2 仅松开
        if mode == 2:
            self.gamepad.release_button(vg.DS4_BUTTONS.DS4_BUTTON_CROSS)

    # []
    async def pressButtonSquare(self,mode = 0):
        print("press button Square")
        # 0 快速按下，约150ms后释放
        if mode == 0:
            self.gamepad.press_button(vg.DS4_BUTTONS.DS4_BUTTON_SQUARE)
            await asyncio.sleep(0.125)
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
        print("press button Triangle")
        # 0 快速按下，约150ms后释放
        if mode == 0:
            self.gamepad.press_button(vg.DS4_BUTTONS.DS4_BUTTON_TRIANGLE)
            await asyncio.sleep(0.125)
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

    # dpad
    async def pressButtonDpad(self,which = "up",mode = 0):
        print("press button Dpad")
        if which == "up" or which == 0:
            button = vg.DS4_DPAD_DIRECTIONS.DS4_BUTTON_DPAD_NORTH
        elif which == "down" or which == 1:
            button = vg.DS4_DPAD_DIRECTIONS.DS4_BUTTON_DPAD_SOUTH
        elif which == "left" or which == 2:
            button = vg.DS4_DPAD_DIRECTIONS.DS4_BUTTON_DPAD_WEST
        elif which == "right" or which == 3:
            button = vg.DS4_DPAD_DIRECTIONS.DS4_BUTTON_DPAD_EAST
        # 0 快速按下，约150ms后释放
        if mode == 0:
            self.gamepad.directional_pad(direction=button)
            # self.gamepad.press_button(vg.DS4_DPAD_DIRECTIONS.DS4_BUTTON_DPAD_NORTH)
            await asyncio.sleep(0.125)
            # self.gamepad.release_button(vg.DS4_DPAD_DIRECTIONS.DS4_BUTTON_DPAD_NORTH)
            self.gamepad.directional_pad(direction=vg.DS4_DPAD_DIRECTIONS.DS4_BUTTON_DPAD_NONE)
        # 1 仅按下
        if mode == 1:
            # self.gamepad.press_button(vg.DS4_DPAD_DIRECTIONS.DS4_BUTTON_DPAD_NORTH)
            self.gamepad.directional_pad(direction=button)
        
        # 2 仅松开
        if mode == 2:
            # self.gamepad.release_button(vg.DS4_DPAD_DIRECTIONS.DS4_BUTTON_DPAD_NORTH)
            self.gamepad.directional_pad(direction=vg.DS4_DPAD_DIRECTIONS.DS4_BUTTON_DPAD_NONE)
        # print("press button O")
        # await asyncio.sleep(1)
        # print("release button O")


    # left stick
    async def setLeftStick(self,x=0,y=0,mode = 1):
        print("turn left stick")
        if mode == 0:
            self.gamepad.left_joystick_float(x,y)
            await asyncio.sleep(0.125)
            self.gamepad.left_joystick_float(0,0)
        elif mode  == 1:
            self.gamepad.left_joystick_float(x,y)
            
    # right stick
    async def setRightStick(self,x=0,y=0,mode = 1):
        print("turn right stick")
        if mode ==0:
            self.gamepad.right_joystick_float(x,y)
            await asyncio.sleep(0.125)
            self.gamepad.right_joystick_float(0,0)
        elif mode == 1:
            self.gamepad.right_joystick_float(x,y)
    # left shoulder
    async def pressButtonShoulderLeft(self,mode = 0):
        print("press button ShoulderLeft")
        # 0 快速按下，约150ms后释放
        if mode == 0:
            self.gamepad.press_button(vg.DS4_BUTTONS.DS4_BUTTON_SHOULDER_LEFT)
            await asyncio.sleep(0.125)
            self.gamepad.release_button(vg.DS4_BUTTONS.DS4_BUTTON_SHOULDER_LEFT)
        # 1 仅按下
        if mode == 1:
            self.gamepad.press_button(vg.DS4_BUTTONS.DS4_BUTTON_SHOULDER_LEFT)
        
        # 2 仅松开
        if mode == 2:
            self.gamepad.release_button(vg.DS4_BUTTONS.DS4_BUTTON_SHOULDER_LEFT)

    # right shoulder
    async def pressButtonShoulderRight(self,mode = 0):
        print("press button ShoulderRight")
        # 0 快速按下，约150ms后释放
        if mode == 0:
            self.gamepad.press_button(vg.DS4_BUTTONS.DS4_BUTTON_SHOULDER_RIGHT)
            await asyncio.sleep(0.125)
            self.gamepad.release_button(vg.DS4_BUTTONS.DS4_BUTTON_SHOULDER_RIGHT)
        # 1 仅按下
        if mode == 1:
            self.gamepad.press_button(vg.DS4_BUTTONS.DS4_BUTTON_SHOULDER_RIGHT)
        
        # 2 仅松开
        if mode == 2:
            self.gamepad.release_button(vg.DS4_BUTTONS.DS4_BUTTON_SHOULDER_RIGHT)

    # left trigger
    async def pressButtonTriggerLeft(self,mode = 0):
        print("press button TriggerLeft")
        # 0 快速按下，约150ms后释放
        if mode == 0:
            self.gamepad.press_button(vg.DS4_BUTTONS.DS4_BUTTON_TRIGGER_LEFT)
            await asyncio.sleep(0.125)
            self.gamepad.release_button(vg.DS4_BUTTONS.DS4_BUTTON_TRIGGER_LEFT)
        # 1 仅按下
        if mode == 1:
            self.gamepad.press_button(vg.DS4_BUTTONS.DS4_BUTTON_TRIGGER_LEFT)
        
        # 2 仅松开
        if mode == 2:
            self.gamepad.release_button(vg.DS4_BUTTONS.DS4_BUTTON_TRIGGER_LEFT)

    # right trigger
    async def pressButtonTriggerRight(self,mode = 0):
        print("press button TriggerRight")
        # 0 快速按下，约150ms后释放
        if mode == 0:
            self.gamepad.press_button(vg.DS4_BUTTONS.DS4_BUTTON_TRIGGER_LEFT)
            await asyncio.sleep(0.125)
            self.gamepad.release_button(vg.DS4_BUTTONS.DS4_BUTTON_TRIGGER_LEFT)
        # 1 仅按下
        if mode == 1:
            self.gamepad.press_button(vg.DS4_BUTTONS.DS4_BUTTON_TRIGGER_LEFT)
        
        # 2 仅松开
        if mode == 2:
            self.gamepad.release_button(vg.DS4_BUTTONS.DS4_BUTTON_TRIGGER_LEFT)
    
    # option
    async def pressButtonOptions(self,mode = 0):
        print("press button Options")
        # 0 快速按下，约150ms后释放
        if mode == 0:
            self.gamepad.press_button(vg.DS4_BUTTONS.DS4_BUTTON_OPTIONS)
            await asyncio.sleep(0.125)
            self.gamepad.release_button(vg.DS4_BUTTONS.DS4_BUTTON_OPTIONS)
        # 1 仅按下
        if mode == 1:
            self.gamepad.press_button(vg.DS4_BUTTONS.DS4_BUTTON_OPTIONS)
        
        # 2 仅松开
        if mode == 2:
            self.gamepad.release_button(vg.DS4_BUTTONS.DS4_BUTTON_OPTIONS)
    
    # share
    async def pressButtonShare(self,mode = 0):
        print("press button Share")
        # 0 快速按下，约150ms后释放
        if mode == 0:
            self.gamepad.press_button(vg.DS4_BUTTONS.DS4_BUTTON_SHARE)
            await asyncio.sleep(0.125)
            self.gamepad.release_button(vg.DS4_BUTTONS.DS4_BUTTON_SHARE)
        # 1 仅按下
        if mode == 1:
            self.gamepad.press_button(vg.DS4_BUTTONS.DS4_BUTTON_SHARE)
        
        # 2 仅松开
        if mode == 2:
            self.gamepad.release_button(vg.DS4_BUTTONS.DS4_BUTTON_SHARE)
    
    # ps
    async def pressButtonPS(self,mode = 0):
        print("press button PS")
        # 0 快速按下，约150ms后释放
        if mode == 0:
            self.gamepad.press_button(vg.DS4_SPECIAL_BUTTONS.DS4_SPECIAL_BUTTON_PS)
            await asyncio.sleep(0.125)
            self.gamepad.release_button(vg.DS4_SPECIAL_BUTTONS.DS4_SPECIAL_BUTTON_PS)
        # 1 仅按下
        if mode == 1:
            self.gamepad.press_button(vg.DS4_SPECIAL_BUTTONS.DS4_SPECIAL_BUTTON_PS)
        
        # 2 仅松开
        if mode == 2:
            self.gamepad.release_button(vg.DS4_SPECIAL_BUTTONS.DS4_SPECIAL_BUTTON_PS)
    
    # pad
    async def pressButtonTouchpad(self,mode = 0):
        print("press button Touchpad")
        # 0 快速按下，约150ms后释放
        if mode == 0:
            self.gamepad.press_button(vg.DS4_SPECIAL_BUTTONS.DS4_SPECIAL_BUTTON_TOUCHPAD)
            await asyncio.sleep(0.125)
            self.gamepad.release_button(vg.DS4_SPECIAL_BUTTONS.DS4_SPECIAL_BUTTON_TOUCHPAD)
        # 1 仅按下
        if mode == 1:
            self.gamepad.press_button(vg.DS4_SPECIAL_BUTTONS.DS4_SPECIAL_BUTTON_TOUCHPAD)
        
        # 2 仅松开
        if mode == 2:
            self.gamepad.release_button(vg.DS4_SPECIAL_BUTTONS.DS4_SPECIAL_BUTTON_TOUCHPAD)



    def pressCross(self,mode = 0):
        self.queueCross.put_nowait(self.pressButtonCross(mode))
    
    def pressSquare(self,mode = 0):
        self.queueSquare.put_nowait(self.pressButtonSquare(mode))

    def pressCircle(self,mode = 0):
        self.queueCircle.put_nowait(self.pressButtonCircle(mode))
        
    def pressTriangle(self,mode = 0):
        self.queueTriangle.put_nowait(self.pressButtonTriangle(mode))
        
    def pressDpad(self,which = "up",mode = 0):
        self.queueDpad.put_nowait(self.pressButtonDpad(which,mode))
        
    def pressOptions(self,mode = 0):
        self.queueOptions.put_nowait(self.pressButtonOptions(mode))
        
    def pressShare(self,mode = 0):
        self.queueShare.put_nowait(self.pressButtonShare(mode))
        
    def pressPS(self,mode = 0):
        self.queuePS.put_nowait(self.pressButtonPS(mode))

    def pressTouchpad(self,mode = 0):
        self.queueTouchpad.put_nowait(self.pressButtonTouchpad(mode))
        
    def leftStick(self,x,y):
        self.queueLeftStick.put_nowait(self.setLeftStick(x,y))
        
    def rightStick(self,x,y):
        self.queueRightStick.put_nowait(self.setRightStick(x,y))
        
    def pressL1(self,mode = 0):
        self.queueShoulderLeft.put_nowait(self.pressButtonShoulderLeft(mode))

    def pressL2(self,mode = 0):
        self.queueTriggerLeft.put_nowait(self.pressButtonTriggerLeft(mode))

    def pressR1(self,mode = 0):
        self.queueShoulderRight.put_nowait(self.pressButtonShoulderRight(mode))

    def pressR2(self,mode = 0):
        self.queueTriggerRight.put_nowait(self.pressButtonTriggerRight(mode))



    async def production_tasks(self): 
        ## 如何决策
        # for i in range(4):
        #     self.pressCross()
        #     # self.pressSquare()
        #     await asyncio.sleep(1)
        #     self.pressDpad(i)
        #     await asyncio.sleep(1)
        # queueCross.put_nowait(self.pressButtonCross())
        async def changeToKeyboard():
            # self.pressOptions()
            # await asyncio.sleep(1)
            # self.leftStick(1.0,0)
            # self.pressTouchpad(mode=1)
            # self.pressDpad("down")
            # await asyncio.sleep(1)
            # self.leftStick(0,1) # 选中最上方
            # await asyncio.sleep(3)
            # self.pressCircle() # 确认
            # await asyncio.sleep(0.61)
            # self.pressCircle() # 修改键鼠
            # await asyncio.sleep(0.61)
            self.pressCircle() # 确认修改键鼠
            # await asyncio.sleep(2)
            # self.leftStick(0,0)
            # self.pressCross()
            # self.pressDpad("left")
        task = asyncio.create_task(changeToKeyboard())
        await task

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
        self.queueDpad = asyncio.Queue(10)
        self.queueShoulderLeft = asyncio.Queue(10)
        self.queueShoulderRight = asyncio.Queue(10)
        self.queueTriggerLeft = asyncio.Queue(10)
        self.queueTriggerRight = asyncio.Queue(10)
        self.queueOptions = asyncio.Queue(10)
        self.queueShare = asyncio.Queue(10)
        self.queuePS = asyncio.Queue(10)
        self.queueTouchpad = asyncio.Queue(10)
        # 创建异步 生产任务
        consumerTask = asyncio.create_task(self.production_tasks( ))#queueLeftStick,queueRightStick ,queueCross,queueCircle,queueSquare,queueTriangle,queueDpadUp,queueDpadDown,queueDpadLeft,queueDpadRight,queueShoulderLeft,queueShoulderRight,queueTriggerLeft,queueTriggerRight))
        # 创建异步 消费任务
        leftStickTask = asyncio.create_task(self.consumer(self.queueLeftStick))
        
        rightStickTask = asyncio.create_task(self.consumer(self.queueRightStick))
        
        crossTask = asyncio.create_task(self.consumer(self.queueCross))

        circleTask = asyncio.create_task(self.consumer(self.queueCircle))

        squareTask = asyncio.create_task(self.consumer(self.queueSquare))

        triangleTask = asyncio.create_task(self.consumer(self.queueTriangle))

        dpadTask = asyncio.create_task(self.consumer(self.queueDpad))
        
        shoulderLeftTask =asyncio.create_task(self.consumer(self.queueShoulderLeft))
        
        shoulderRightTask = asyncio.create_task(self.consumer(self.queueShoulderRight))
        
        triggerLeftTask = asyncio.create_task(self.consumer(self.queueTriggerLeft))
        
        triggerRightTask = asyncio.create_task(self.consumer(self.queueTriggerRight))
        
        optionsTask = asyncio.create_task(self.consumer(self.queueOptions))
        
        shareTask = asyncio.create_task(self.consumer(self.queueShare))
        
        psTask = asyncio.create_task(self.consumer(self.queuePS))
        
        touchpadTask = asyncio.create_task(self.consumer(self.queueTouchpad))

        await leftStickTask
        await rightStickTask
        await consumerTask
        await crossTask
        await circleTask
        await squareTask 
        await triangleTask 
        await dpadTask
        await shoulderLeftTask
        await shoulderRightTask
        await triggerLeftTask
        await triggerRightTask
        await optionsTask
        await shareTask
        await psTask
        await touchpadTask


    # async def setGamepadStatus(self,message = []):
    #     '''改变gamepad的状态'''
    #     while True:
    #         print("try to set gamepad")
    #         await asyncio.sleep(1)


    async def updateGamepad(self,dt):
        while True:
            self.gamepad.update()
            # print("update gamepad")
            await asyncio.sleep(dt)
            # 这里可以设置一个检测按键的开关
        
    async def mainGamePad(self,dt):
        await asyncio.gather(
            self.updateGamepad(dt),
            # self.setGamepadStatus(),
            self.queueHandle()
        )

    def run(self):
        asyncio.run(self.mainGamePad(1/120))






if __name__ == "__main__":
    GPHD = GamepadTaskHandler(vg.VDS4Gamepad())
    GPHD.run()
