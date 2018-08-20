class Dynamixel(object):
	def __init__(self):
		ports=pypot.dynamixel.get_available_ports()
		if not ports:
			raise IOError("Port not found!")
		print "Available ports: ",ports[0]

		self.dxl=pypot.dynamixel.DxlIO(ports[0])
		
