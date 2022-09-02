import pyautogui
from  inputDetect import checkWindow
screenWidth, screenHeight = pyautogui.size()
with open('mouseLeftMove.csv') as f:
    line = f.readline()
    while line:
        if checkWindow():
            xypos = line[:-1].split(",")
            pyautogui.moveTo(int(xypos[0]),int(xypos[1]),1/200)
            line = f.readline()

