import pypot.dynamixel
ports=pypot.dynamixel.get_available_ports()
print ports

dxl=pypot.dynamixel.DxlIO(ports[0])
print dxl.scan(range(11))
print dxl.get_present_position([1,2,3,4,5,6,7,8,9,10])
dxl.set_moving_speed({1:50, 2:50, 3:50, 4:50, 5:50, 6:50, 7:50, 8:50, 9:50, 10:50})
dxl.set_goal_position({1:-47.65, 2:49.71, 3:-0.15, 4:0.15, 5:-96.33, 6:96.63, 7:99.56, 8:-96.04, 9:0, 10:0})

dxl.set_moving_speed({1:50, 2:50, 3:50, 4:50, 5:50, 6:50, 7:50, 8:50, 9:50, 10:50})

dxl.set_goal_position({1:-36.8, 2:34.75, 3:-1.61, 4:-0.15, 5:-15.4, 6:14.52, 7:30.94, 8:-28.59, 9:0, 10:0})