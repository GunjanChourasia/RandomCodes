import pypot.dynamixel
import time


ports=pypot.dynamixel.get_available_ports()
if not ports:
	raise RuntimeError("No available ports")
dxl=pypot.dynamixel.DxlIO(ports[0])
print ports[0]
ids=dxl.scan(range(15))

print ids