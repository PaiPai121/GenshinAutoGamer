import pyvjoy
MAX_VJOY = 32767

j = pyvjoy.VJoyDevice(1)
for i in range(0x1,0x8000):
    
    j.set_axis(pyvjoy.HID_USAGE_X, i)
    
    # j.set_button(pyvjoy.)
    
MAX_VJOY = 32767
j = pyvjoy.VJoyDevice(1)

def play_function(self,X,Y,Z,XRot):
    self.j.data.wAxisX = int(X * self.MAX_VJOY)
    self.j.data.wAxisY = int(Y * self.MAX_VJOY)
    self.j.data.wAxisZ = int(Z * self.MAX_VJOY)
    self.j.data.wAxisXRot = int(XRot * self.MAX_VJOY)
    j.update()