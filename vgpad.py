import vgamepad as vg

# gamepad = vg.VX360Gamepad()


import win32gui

import time

def checkWindow():
    hwnd = win32gui.GetForegroundWindow()
    # 获取窗口题目
    title = win32gui.GetWindowText(hwnd)
    if title == "原神":
        print("当前窗口为原神")
        return True
    else:
        print("当前为无关窗口")
        return False

gamepad = vg.VDS4Gamepad()
# while True:
#     if checkWindow():
#         # gamepad.right_joystick_float(1,0)
#         # gamepad.press_button(button = vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)
#         gamepad.press_button(button = vg.DS4_BUTTONS.DS4_BUTTON_CROSS)
#         # gamepad.left_joystick_float(-1,0)
#         gamepad.update()
#         time.sleep(1)
#         break

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
        gamepad.update()
        await asyncio.sleep(dt)
        # 这里可以设置一个检测按键的开关

async def setGamepadStatus(gamepad,message = []):
    '''改变gamepad的状态'''
    from Capture import PatternChecker
    import cv2
    checker = PatternChecker()
    # if checker.checkExit(cv2.imread('./assets/GamepadsettingMain.png')):
    if True:
        gamepad.press_button(vg.DS4_BUTTONS.DS4_BUTTON_CROSS)
        await asyncio.sleep(0.3)
        gamepad.reset()
    # for i in range(-100,100):
    #     await asyncio.sleep(0.01)
    #     gamepad.left_joystick_float(i/100,i/100)
    await asyncio.gather(pushButton(gamepad,vg.DS4_BUTTONS.DS4_BUTTON_CROSS),moveStick(gamepad.left_joystick_float))
    # tasks = []
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete()
    
    
async def mainGamePad(gamepad,dt):
    await asyncio.gather(
        updateGamepad(gamepad,dt),
        setGamepadStatus(gamepad)
    )


# async def setButtonX():

# async def setStickL():

# async def setStickR():


gamepad = vg.VDS4Gamepad()
while True:
    if checkWindow():
        ## 在原神窗口内开始
        asyncio.run(mainGamePad(gamepad,1/120))
