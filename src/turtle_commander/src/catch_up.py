#! /usr/bin/python3

import rospy
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
import math


class Catch_up:
	def __init__(self):
		rospy.Subscriber('/turtle1/pose', Pose, self.callback)
		rospy.Subscriber('/leo/pose', Pose, self.callback_leo)
		self.pub = rospy.Publisher('/leo/cmd_vel', Twist, queue_size=10)
		self.leo_x = 0
		self.leo_y = 0
		self.leo_theta = 0
		self.x_dir = 1.0
		self.y_dir = 1.0
	
	def callback_leo(self, msg):
		self.leo_x = msg.x
		self.leo_y = msg.y
		self.leo_theta = msg.theta
		self.x_dir = math.cos(msg.theta)
		self.y_dir = math.sin(msg.theta)	
		
	def callback(self, msg):
		x = msg.x - self.leo_x
		y = msg.y - self.leo_y
		
		#alpha = math.acos((self.x_dir * x + self.y_dir * y) / (math.sqrt(x * x + y * y) * math.sqrt(self.x_dir ** 2 + self.y_dir ** 2)))
		alpha = math.acos(x / math.sqrt(x ** 2 + y ** 2))
		
		if self.leo_y > msg.y:
			alpha *= -1
			

		dif = alpha - self.leo_theta #разница угла движения и угол направления turtle1
		if dif > 3.1415:
			dif -= 3.1415
			dif *= -1
		msg_dv = Twist()
		
		msg_dv.linear.x = 1
		msg_dv.angular.z = dif
		self.pub.publish(msg_dv)

	

rospy.init_node('turtle_catch_up')
r = rospy.Rate(0.3)
Catch_up()
r.sleep()
rospy.spin()
