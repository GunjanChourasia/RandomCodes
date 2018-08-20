import pypot.dynamixel
import time

ports=pypot.dynamixel.get_available_ports()
print ports


dxl=pypot.dynamixel.DxlIO(ports[0])
print dxl.get_present_position((5,6,7,8))

'''dxl.set_goal_position({1:0,2:0,3:0,4:0})
dxl.set_goal_position({7:87,8:-87,5:-117,6:117,7:70,8:-70})
dxl.set_moving_speed({1:100,2:100,3:100,4:100})
c,d=-27,-27
a,b=-22,-22
while (True):
	
	dxl.set_goal_position({3:a,4:b})
	time.sleep(0.3)
	a,b=-a,-b
	dxl.set_goal_position({1:c,2:d})
	c,d=-c,-d
	time.sleep(0.3)
	dxl.set_goal_position({1:0,2:0,3:0,4:0})'''





#Forward:
#(-82.26, 93.4, 47.95, -57.92)(5,6,7,8)
#(-27,-27)(c,d)    (-22,-22)(a,b)
#speed(100)(1,2,3,4)


#Backward
#(-150.0, 150.0, 9.24, -22.43)(5,6,7,8)
#(-126.54, 117.16, 86.95, -86.95)

