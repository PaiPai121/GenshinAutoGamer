import vgamepad as vg

gamepad = vg.VX360Gamepad()


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
    
while True:
    if checkWindow():
        # gamepad.right_joystick_float(1,0)
        gamepad.press_button(button = vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)
        gamepad.update()
        time.sleep(1)
        break
