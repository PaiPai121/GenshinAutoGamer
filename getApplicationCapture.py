import win32gui
import win32ui
from ctypes import windll
from PIL import Image
import cv2
import numpy as np

class WindowCapture():
    def __init__(self,windowName = "原神"):
        # 注意窗口不能最小化，不能移除屏幕外
        self.hwnd = win32gui.FindWindow(None, windowName) # 获取窗口
        # 获取句柄
        self.hwndDC = win32gui.GetWindowDC(self.hwnd)
        self.mfcDC = win32ui.CreateDCFromHandle(self.hwndDC)
        self.saveDC = self.mfcDC.CreateCompatibleDC()
        self.saveBitMap = win32ui.CreateBitmap()
        self.width = 0
        self.height = 0
    def getCapture(self):
        # Get window bounds
        left, top, right, bot = win32gui.GetClientRect(self.hwnd)
        # left, top, right, bot = win32gui.GetWindowRect(self.hwnd)
        w = right - left
        h = bot - top

        
        self.saveBitMap.CreateCompatibleBitmap(self.mfcDC, w, h)

        self.saveDC.SelectObject(self.saveBitMap)

        result = windll.user32.PrintWindow(self.hwnd, self.saveDC.GetSafeHdc(), 1)
        # print(result)

        bmp_info = self.saveBitMap.GetInfo()
        bmp_str = self.saveBitMap.GetBitmapBits(True)
        # print(bmp_str)
        # img = cv2.resize(np.fromstring(bmp_str,np.uint8).reshape(bmp_info['bmWidth'], bmp_info['bmHeight']),cv2.IMREAD_COLOR)
        # img = cv2.resize(np.frombuffer(bmp_str,np.uint8),3,(bmp_info['bmWidth'], bmp_info['bmHeight']))
        # 折腾半天也没成功的拿opencv直接读内存中的图像，就转一道吧
        # cv2.imshow("123123",img)
        # img.show()
        im = Image.frombuffer(
            'RGB',
            (bmp_info['bmWidth'], bmp_info['bmHeight']),
            bmp_str, 'raw', 'BGRX', 0, 1)
        self.width = bmp_info['bmWidth']
        self.height = bmp_info['bmHeight']
        if not np.any(im):
            print("未捕获到图像，请检查窗口是否激活")
            return None
        return cv2.cvtColor(np.asarray(im),cv2.COLOR_RGB2BGR)

    def release(self):
        # 释放
        win32gui.DeleteObject(self.saveBitMap.GetHandle())
        self.saveDC.DeleteDC()
        self.mfcDC.DeleteDC()
        win32gui.ReleaseDC(self.hwnd, self.hwndDC)
        # im.show()

from uiMatch import PatternChecker

if __name__ == "__main__":
    cap = WindowCapture()
    im = cap.getCapture()
    
    cap.release()
    # im.show()
    logger = PatternChecker(1080/720)
    logger.setCoff =1080/720
    print(logger.checkExit(im,randomCoff=0))
    print(logger.checkLogin(im,randomCoff=0))