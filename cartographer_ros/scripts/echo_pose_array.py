#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from rosgraph_msgs.msg import Log
from geometry_msgs.msg import PoseArray

pose_array_stored = None;

def callback(data):
    global pose_array_stored
    rospy.loginfo(rospy.get_caller_id() + "I heard %d", len(data.poses))
    pose_array_stored = PoseArray()
    pose_array_stored = data;

def listener():
    global pose_array_stored
    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("trajectory_pose_array", PoseArray, callback)

    # spin() simply keeps python from exiting until this node is stopped

    pub = rospy.Publisher('trajectory_pose_array_keep', PoseArray, queue_size=10)
    rate = rospy.Rate(2) # 10hz
    while 1:
        hello_str = "hello world %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        if pose_array_stored!=None:
            pub.publish(pose_array_stored)
        rate.sleep()


if __name__ == '__main__':
    listener()