import pypot.dynamixel
import time

ports=pypot.dynamixel.get_available_ports()
print ports


dxl=pypot.dynamixel.DxlIO(ports[0])


def forward():
	dxl.set_goal_position({1:0,2:0,3:0,4:0})
	dxl.set_goal_position({7:70,8:-70})
	c,d=-27,-27
	a,b=-25,-25
	while (True):
		dxl.set_moving_speed({1:100,2:100,3:100,4:100})
		dxl.set_goal_position({3:a,4:b})
		time.sleep(0.1)
		a,b=-a,-b
		dxl.set_goal_position({1:c,2:d})
		c,d=-c,-d
		time.sleep(0.1)
		dxl.set_goal_position({1:0,2:0,3:0,4:0})
		time.sleep(0.1)

def backward():
	c,d=27,27
	a,b=-22,-22
	while (True):
		dxl.set_moving_speed({1:100,2:100,3:100,4:100})
		dxl.set_goal_position({3:a,4:b})
		time.sleep(0.3)
		a,b=-a,-b
		dxl.set_goal_position({1:c,2:d})
		c,d=-c,-d
		time.sleep(0.3)
		dxl.set_goal_position({1:0,2:0,3:0,4:0})
forward()
