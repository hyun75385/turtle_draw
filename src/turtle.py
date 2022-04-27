#!/usr/bin/env python
import turtle
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

turtlepose  = Pose()

def callback(data):
    global turtlepose
    turtlepose.x = data.x
    turtlepose.y = data.y
    turtlepose.theta = data.theta
    print turtlepose.x, turtlepose.y, turtlepose.theta

def main():
    global turtlepose
    rospy.init_node('turtle', anonymous=False)
    rospy.Subscriber("turtle1/pose", Pose, callback)
    pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10) # 10hz

    vel = Twist()
    vel.linear.x = 0
    vel.linear.y = 0
    vel.linear.z = 0
    vel.angular.x = 0
    vel.angular.y = 0
    vel.angular.z = 0

    while not rospy.is_shutdown():
        vel.linear.x = 1
        vel.angular.z = 1
        pub.publish(vel)
        rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass

