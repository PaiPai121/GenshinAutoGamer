
import cv2
import numpy as np
from random import randint
resolutionW = 1280
resolutionH = 720
def patternTransfer(pattern):
    # 用于将模版图片转换为对应的分辨率。基本模版为1280*720分辨率下截图。    
    pass

uipng = cv2.imread('gameui.png')
loginpng = cv2.imread('login.png')
# 图像格式 ： 720* 1280* 3

# cv2.imshow("123",uipng[100:700,1000:1200,:])
# cv2.imshow("234",uipng)
# cv2.waitKey(0)
# cv2.destoryAllWindows()
def show(img):
    cv2.imshow("234",img)
    cv2.waitKey(0)
    cv2.destoryAllWindows()
def MapCut(img:np.array,y,x,w,h):
    ## [x,y,w,h]
    return img[y:y+w,x:x+h,:]








## 从左593开始匹配是否有开始游戏 93*30



# ## uid 右下角190*3
# regionXoffset = resolutionW - 190
# regionYoffset = resolutionH - 30
# regionHeigh = 30
# regionWidth = 190
# # if __name__ == "__main__":
# #     clickPoint = patternMatch(logoffPattern,loginpng,regionYoffset,regionXoffset,regionWidth,regionHeigh,True)


# print(clickPoint)

class PatternChecker():
    def __init__(self,coff = 1):
        self.coff = coff
    def setCoff(self,coff):
        self.coff = coff
    def checkExit(self,img,showFlag = True,randomCoff = 1):
        ## 从左下开始120 120 区域匹配是否有退出键
        logoffPattern = cv2.imread('./assets/logoff.png')
        patternHeight,patternWidth,rubbish = np.shape(logoffPattern)
        logoffPattern = cv2.resize(logoffPattern,  (int(patternHeight*self.coff), int(patternWidth*self.coff)))
        regionXoffset = int(0*self.coff)
        regionYoffset = int((resolutionH-120)*self.coff)
        regionWidth = int(150*self.coff)
        regionHeigh = int(150*self.coff)
        # if __name__ == "__main__":
        clickPoint = self.patternMatch(logoffPattern,img,regionYoffset,regionXoffset,regionWidth,regionHeigh,showFlag,randomCoff )
        return clickPoint

    def checkLogin(self,img,showFlag = True,randomCoff = 1):
        loginPattern = cv2.imread('./assets/login.png')
        patternHeight,patternWidth,rubbish = np.shape(loginPattern)
        loginPattern = cv2.resize(loginPattern,  (int(patternHeight*self.coff), int(patternWidth*self.coff)))
        regionXoffset = int(550*self.coff)
        regionYoffset = int((resolutionH - 100)*self.coff)
        regionWidth = int(self.coff*200)
        regionHeigh = int(self.coff*100)
        clickPoint = self.patternMatch(loginPattern,img,regionYoffset,regionXoffset,regionWidth,regionHeigh,showFlag,randomCoff )
        return clickPoint
    
    def patternMatch(self,pattern:np.array,img:np.array,regionYoffset=0,regionXoffset=0,regionWidth=1280,regionHeigh=720,show = False,randomCoff = 1):
        ## 输入匹配模版和被匹配图像
        region = MapCut(img,regionYoffset,regionXoffset,regionHeigh,regionWidth) # 需要匹配的区域
        # show(region)
        height, width, c = pattern.shape  # 模版的参数

        ## 获取匹配结果
        results = cv2.matchTemplate(region, pattern, cv2.TM_SQDIFF_NORMED)
        minValue, maxValue, resultPoint1, resultPoint2 = cv2.minMaxLoc(results)
        print(minValue,maxValue)
        if minValue < 0.1:
            print("find position")
        else:
            return None
        #  = (resultPoint1[0] + width, resultPoint1[1] + height)
        clickPoint = (resultPoint1[0] + int(width/2 * (1+0.4/self.coff*randomCoff*randint(1,100)/100)) + regionXoffset, resultPoint1[1] +int( height/2 * (1+0.4**randomCoff*randint(1,100)/100) )+ regionYoffset)
        if show:
            cv2.rectangle(img,(resultPoint1[0]+regionXoffset,resultPoint1[1]+regionYoffset),(resultPoint1[0]+regionXoffset+width,resultPoint1[1]+regionYoffset+height),(255,0,0),2)
            img = cv2.circle(img,clickPoint ,5,(0, 0, 255), 2)
            cv2.imshow("img",img)
            cv2.waitKey()
            cv2.destroyAllWindows()
        return clickPoint
    def MatchInGrey(self,img,pattern):
        # 取出Alpha通道
        alpha = img[:,:,3]
        # 模板匹配，将alpha作为mask，TM_CCORR_NORMED方法的计算结果范围为[0, 1]，越接近1越匹配
        result = cv2.matchTemplate(pattern, img, cv2.TM_CCORR_NORMED, mask=alpha)
        return result
## uid 右下角190*3

if __name__ == "__main__":
    regionXoffset = resolutionW - 190
    regionYoffset = resolutionH - 30
    regionHeigh = 30
    regionWidth = 190
    checker = PatternChecker()
    checker.checkExit(cv2.imread('login.png'))
    # clickPoint = patternMatch(logoffPattern,loginpng,regionYoffset,regionXoffset,regionWidth,regionHeigh,True)
    
    
    
    
    
# import cv2
# import numpy as np

# # 读取图片，丢弃Alpha通道，转为灰度图
# a = cv2.imread('pc_activity_btn.png', cv2.IMREAD_GRAYSCALE)
# # 读取图片，并保留Alpha通道
# b = cv2.imread('transparent_activity_btn.png', cv2.IMREAD_UNCHANGED)
# # 取出Alpha通道
# alpha = b[:,:,3]
# # 模板匹配，将alpha作为mask，TM_CCORR_NORMED方法的计算结果范围为[0, 1]，越接近1越匹配
# result = cv2.matchTemplate(a, b, cv2.TM_CCORR_NORMED, mask=alpha)
# # 获取结果中最大值和最小值以及他们的坐标
# print(cv2.minMaxLoc(result))

# # 运行结果：
# # (0.9999997615814209, 0.9999997615814209, (0, 0), (0, 0))

