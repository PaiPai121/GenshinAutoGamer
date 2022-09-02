from getApplicationCapture import WindowCapture
if __name__ == '__main__':
    cap = WindowCapture("《星际争霸II》")

    im = cap.getCapture()
    im.show()
    cap.release()
    # # im.show()
    # logger = loginChecker(1080/720)
    # logger.setCoff =1080/720
    # print(logger.checkExit(im,randomCoff=0))
    # print(logger.checkLogin(im,randomCoff=0))
    pass
    
# import ctypes

# EnumWindows = ctypes.windll.user32.EnumWindows

# EnumWindowsProc = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))

# GetWindowText = ctypes.windll.user32.GetWindowTextW

# GetWindowTextLength = ctypes.windll.user32.GetWindowTextLengthW

# IsWindowVisible = ctypes.windll.user32.IsWindowVisible

# titles = []

# def foreach_window(hwnd, lParam):

#     if IsWindowVisible(hwnd):

#         length = GetWindowTextLength(hwnd)

#     buff = ctypes.create_unicode_buffer(length + 1)

#     GetWindowText(hwnd, buff, length + 1)

#     titles.append(buff.value)

#     return True

# EnumWindows(EnumWindowsProc(foreach_window), 0)

# print(titles)