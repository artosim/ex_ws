#! /usr/bin/python3
import rospy
from turtlesim.msg import Pose

def callback(msg):
	rospy.loginfo(msg)

rospy.init_node('turtle_log_pose')
rospy.Subscriber('/turtle1/pose', Pose, callback)

rospy.spin()
