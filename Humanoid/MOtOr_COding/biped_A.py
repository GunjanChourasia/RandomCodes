import pypot.dynamixel
import time
import itertools
import numpy as np
import xml.etree.ElementTree as ET
from math import pi,atan,sin,cos,degrees
import rospy
from std_msgs.msg import String

#ang=(91.38, 87.34, 6.81, -47.16, 79.87, -80.31, -94.9, 124.18, -0.31, -2.68, 11.47, -12.7, -15.78, 14.55, -8.48, 3.91, -0.13, -4.26, 46.99)
darwin = {1: 90, 2: -90, 3: 67.5, 4: -67.5, 7: 45, 8: -45, 9: 'i', 10: 'i', 13: 'i', 14: 'i', 17: 'i', 18: 'i', 19 : 0, 20 : 0}
abmath = {11: 15, 12: -15, 13: -10, 14: 10, 15: -5, 16: 5}
hand = {5: 60, 6: -60}

class Dynamixel(object) :
	def __init__(self) :
		ports=pypot.dynamixel.get_available_ports()
		if not ports :
			raise IOError("Bhai ko ports nhi mili, port wali bakchodi")

		print "Bhai connection laga rha he",ports[0]

		self.dxl=pypot.dynamixel.DxlIO(ports[0])
		self.ids=self.dxl.scan(range(20))
		print self.ids
		self.dxl.enable_torque(self.ids)
		if len(self.ids)<19 :
			raise RuntimeError("Bhai ko motors nhi mile, motors not detected wali bakchodi")
		else :
			print "Bhai ko motors mil gaye"
		self.dxl.set_moving_speed(dict(zip(self.ids,itertools.repeat(100))))


	def setSpeed(self,speed,ids) :
		self.dxl.set_moving_speed(dict(zip(ids,itertools.repeat(speed))))

	def setPos(self,pose) :
		pos={ids:angle for ids,angle in pose.items()}
		self.dxl.set_goal_position(pos)
		print pos

	def listWrite(self,list) :
		pos=dict(zip(self.ids,list))
		self.dxl.set_goal_position(pos)

	def writePos(self,dicti) :
		
		self.dxl.set_goal_position(dicti)

	def writeAng(self,ids,pose) :
		self.dxl.set_goal_position({ids:pos})
		
	def returnPos(self,ids) :

		return self.dxl.get_present_position((ids,))	


x=Dynamixel()

class XML(object) :
	def __init__(self,file) :
		tree=ET.parse(file)
		self.root=tree.getroot()
		print self.root


	def parse(self,motion) :

		find="PageRoot/Page[@name='" +motion+ "']/steps/step"
		steps=[x for x in self.root.findall(find)]
		print steps
		p_frame=str()
		p_pose=str()
		for step in steps :
			print "in parse"
			Walk(step.attrib['frame'],step.attrib['pose'],p_frame,p_pose)
			p_frame=step.attrib['frame']
			p_pose=step.attrib['pose']
			
path = "/home/amrit/catkin/src/walk/scripts/data.xml"	
xml = XML(path)

class Walk(object) :
	def __init__(self,frame,pose,p_frame,p_pose) :
		self.frame=int(frame)
		self.begin={}
		self.end={}
		if not(p_pose) :
			self.frame_diff=10
			p_pose=pose
		else :
			self.frame_diff=self.frame-int(p_frame) 

		for ids,pos in enumerate(map(float,p_pose.split())) :
			self.end[ids+11]=pos	

		for ids,pos in enumerate(map(float,pose.split())) :
			self.begin[ids+11]=pos
		
			
		self.motion()
		self.set(offsets=[darwin])

	def offset(self,offset) :
		
		for key in offset.keys() :
			if offset[key] == 'i' :
				self.begin[key] = -self.begin[key]
				self.end[key] = -self.end[key]
			else :
				self.begin[key] += offset[key]
				self.end[key] += offset[key]
		
		

	def set(self,offsets=[]) :
		for offset in offsets :
			self.Offset(offset)
		self.motion()

	def motion(self) :
		write=[]
		ids=[]
		print "in motion"
		f_d=abs(self.frame_diff/10)
		for key in self.end.keys() :
			#pose_diff=abs(self.end[key]-self.begin[key])
			linp=np.linspace(self.end[key],self.begin[key],f_d)
			write.append(linp)
			#write.append(self.begin[key])
			ids.append(key)	
		print "out"
		for pose in zip(*write) :
			print "in"
			x.setPos(dict(zip(ids,pose)))
			time.sleep(0.08)


path = "/home/amrit/catkin/src/walk/scripts/data.xml"	
xml = XML(path)


def walk() :

	balance = xml.parse("2 Stand up")
	for i in range(10) :

		left = xml.parse("6 fl1") 
		time.sleep(0.3)
		right = xml.parse("7 fr1")
		time.sleep(0.3)

if __name__ == "__main__" :
	walk()