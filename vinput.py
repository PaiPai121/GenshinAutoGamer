import pygame
import time
import numpy as np
pygame.init()
pygame.joystick.init()
done=False
import matplotlib.pyplot as plt
axis1data = []
axis2data = []
count = 10000
while count >0:
    count -=1
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
    joystick_count = pygame.joystick.get_count()
    time_start = time.time()
    for i in range(0,1):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()

    
        print( "Joystick {}".format(i) )
        # Get the name from the OS for the controller/joystick
        name = joystick.get_name()
        print( "Joystick name: {}".format(name) )
        
        # Usually axis run in pairs, up/down for one, and left/right for
        # the other.
        axes = joystick.get_numaxes()
        print("Number of axes: {}".format(axes) )
        # textPrint.indent()
        
        for i in range( axes ):
            axis = joystick.get_axis( i )
            print( "Axis {} value: {:>6.3f}".format(i, axis) )
            if i == 1:
                axis1data.append(axis)
            if i == 2:
                axis1data.append(axis)
        # textPrint.unindent()
            
        # buttons = joystick.get_numbuttons()
        # textPrint.print(screen, "Number of buttons: {}".format(buttons) )
        # textPrint.indent()
 
        # for i in range( buttons ):
        #     button = joystick.get_button( i )
        #     textPrint.print(screen, "Button {:>2} value: {}".format(i,button) )
        # textPrint.unindent()
            
        # # Hat switch. All or nothing for direction, not like joysticks.
        # # Value comes back in an array.
        # hats = joystick.get_numhats()
        # textPrint.print(screen, "Number of hats: {}".format(hats) )
        # textPrint.indent()
 
        # for i in range( hats ):
        #     hat = joystick.get_hat( i )
        #     textPrint.print(screen, "Hat {} value: {}".format(i, str(hat)) )
        # textPrint.unindent()
        
        # textPrint.unindent()
time_end = time.time()
time = time_end-time_start
print(time)
t = np.linspace(0,time,len(axis1data))
# [ 0time ]
plt.plot(t,axis1data)
plt.show()
# ————————————————
# 版权声明：本文为CSDN博主「来自江南的你」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/qq_41556318/article/details/86305263