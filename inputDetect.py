import pyautogui as pag
import time
sampleF = 200 # 鼠标运动采样率Hz
sampleT = 1/sampleF
import win32gui


    
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
if __name__ == '__main__':
    # 鼠标采样
    with open('mouseLeftMove.csv', 'w+') as f:
        try:
            while True:
                if checkWindow():
                    screenWidth, screenHeight = pag.size()
                    x, y = pag.position() # 鼠标位置
                    print(
                        "Screen size: (%s %s),  Position : (%s, %s)\n" % (screenWidth, screenHeight, x, y)
                    )
                    f.write(str(x)+","+str(y)+"\n")
                time.sleep(sampleT)
        except KeyboardInterrupt:
            print('end')
        # f.write(buff)
            