#!/usr/bin/env python3
# license removed for brevity
import rospy
from std_msgs.msg import String

def callback(data):
	pub = rospy.Publisher('/coordinates', String, queue_size=10)
	rospy.init_node('car_coordinates', anonymous=True)
	rate = rospy.Rate(1)
	wr,wl,delta = data.data.split(' ')
	wr=int(wr)
	wl=int(wl)
	delta=int(delta)
	theta = 30
	theta_dot = (r*(wl-wr))/2*l
	R = l/tan(delta)
	v = theta_dot*R
	y_dot = v*sin(theta)
	x_dot = v*cos(theta)
	delta_t=0
	for delta_t in range(10):
		theta = theta_dot * delta_t
		y_dot = v*sin(theta)
		x_dot = v*cos(theta)
		x = x + (x_dot*delta_t)
		y = y + (y_dot*delta_t)
		coordinates="%s %s %s" % (x,y,theta)
		pub.publish(coordinates)
 def listener():
 	rospy.init_node('bicycle_model', anonymous=True)
   
       rospy.Subscriber("/raw_data", String, callback)
   
      # spin() simply keeps python from exiting until this node is stopped
       rospy.spin()
  
if __name__ == '__main__':
	listener()
