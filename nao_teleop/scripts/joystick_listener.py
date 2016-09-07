#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Joy
from naoqi import ALProxy

memory = ALProxy("ALMemory", "pepper.local", 9559)

def callback(data):
    memory.raiseEvent("onJoystickButton", data.buttons)

def listener():
    rospy.init_node('joystick_listener', anonymous=True)

    rospy.Subscriber('/joy', Joy, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
