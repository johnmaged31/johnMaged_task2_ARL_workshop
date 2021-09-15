#!/usr/bin/env python3
# license removed for brevity
import rospy
from std_msgs.msg import String
def talker():
	pub = rospy.publisher('/navigation_data', string , queue size=10)
	rospy.init_node('car_directories' , anonymous=true)
	L = 3
	K = 10
	wl = 20
	wr = 40
	r = 0.2
	# example for initial conditions
	front_wheelX = 0
	front_wheelY = 3
	rear_wheelX = 0
	rear_wheelY = 0
	targetX = 15
	TargetY = 30
	theta_dot = (r*(wl-wr))/2*L
	v = 60
	theta = 30
	while Ld != 0 :
		Ld = sqrt(pow(targetX-rear_wheelX,2)+pow(targetY-rear_wheelY,2))
		for line_directoryX in range (100):
			for line_directoryY in range(100):
				e=100
				if (sqrt(pow(targetX-line_directoryX,2)+pow(targetY-line_directoryY,2))<e):
					e=sqrt(pow(targetX-line_directoryX,2)+pow(targetY-line_directoryY,2))
		sin_alpha = e/Ld
		delta = math.atan(2*L*sin_alpha)/(K*V)
		pub.publish(delta)
		R = L/tan(delta)
		v = theta_dot*R
		y_dot = v*sin(theta)
		x_dot = v*cos(theta)
		for delta_t in range(10):
			theta = theta_dot * delta_t
			y_dot = v*sin(theta)
			x_dot = v*cos(theta)
			front_wheelX = front_wheelX + (x_dot*delta_t)
			front_wheelY = front_wheelY + (y_dot*delta_t)

if __name__ == '__main__':
     try:
          talker()
     except rospy.ROSInterruptException:
         pass
