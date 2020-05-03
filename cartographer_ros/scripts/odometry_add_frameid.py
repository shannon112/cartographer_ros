#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from nav_msgs.msg import Odometry
import tf
from geometry_msgs.msg import PoseWithCovariance 

pub = None

def callback(data):
    global pub
    modified_data = Odometry()
    modified_data = data
    modified_data.child_frame_id = "base_footprint"
    pub.publish(modified_data)

def listener():
    global pub
    rospy.init_node('odometry_add_frameid', anonymous=True)
    rospy.Subscriber("base_odometry/odom", Odometry, callback)
    pub = rospy.Publisher('base_odometry/odom_footprint', Odometry, queue_size=10)
    rospy.spin()

if __name__ == '__main__':
    listener()