#! /usr/bin/env python3

from std_srvs.srv import Empty, EmptyResponse
import rospy
import time

def go_home(request):
    rospy.loginfo("Going to home.")
    rospy.sleep(2)
    rospy.loginfo("Arrived.")
    return EmptyResponse()

def go_to_kitchen(request):
    rospy.loginfo("Going to kitchen.")
    rospy.sleep(2)
    rospy.loginfo("Arrived.")
    return EmptyResponse()
    
def stop(request):
    rospy.loginfo("Stop!")
    return EmptyResponse()

if __name__ == "__main__":
    rospy.init_node("matika_naruepan")
    rospy.Service("/go_home", Empty, go_home)
    rospy.Service("/go_to_kitchen", Empty, go_to_kitchen)
    rospy.Service("/stop", Empty, stop)
    rospy.spin()