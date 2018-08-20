import pypot.dynamixel
import time

ports = pypot.dynamixel.get_available_ports()
print ports

dxl = pypot.dynamixel.DxlIO(ports[0])
print dxl

print dxl.get_present_position(range(1,9))
def prone():
	dxl.set_moving_speed({1:50,2:50,3:50,4:50,5:50,6:50,7:50,8:50})
	dxl.set_goal_position({5:-150,6:150,3:-65,4:65,1:90,2:-90,7:90,8:-90}) #primary
	dxl.set_goal_position({5:-150,6:150,3:-33,4:33,1:90,2:-90,7:0,8:0})#2


