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
# vg.DS4_BUTTONS.DS4_BUTTON_SHOULDER_LEFT
# vg.DS4_BUTTONS.DS4_BUTTON_TRIGGER_LEFT


# vg.DS4_BUTTONS.DS4_BUTTON_OPTIONS
# vg.DS4_SPECIAL_BUTTONS.DS4_SPECIAL_BUTTON_PS

from GamepadTaskHandler import GamepadTaskHandler
gamepadTH = GamepadTaskHandler(gamepad)
import asyncio
async def messageSend():
    while True:
        print("send")
while True:
    if checkWindow():
        ## 在原神窗口内开始
        gamepadTH.run()
        
        # await asyncio.gather(gamepadTH.run(),messageSend())
        break
    
print("finish")



