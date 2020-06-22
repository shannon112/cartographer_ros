#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from nav_msgs.msg import Odometry
from tf2_msgs.msg import TFMessage
from geometry_msgs.msg import TransformStamped

pub = None
tf_static_list = TFMessage()

def callback(datas):
    for data in datas.transforms:
        tf_static_list.transforms.append(data)

def callbackPub(datas):
    global pub, tf_static_list
    for tf in tf_static_list.transforms:
        tf.header.stamp = datas.transforms[0].header.stamp
    pub.publish(tf_static_list)

def listener():
    global pub
    rospy.init_node('tf_static_keeper', anonymous=True)
    pub = rospy.Publisher('tf_static', TFMessage, queue_size=10)
    rospy.Subscriber("tf_static", TFMessage, callback)
    rospy.Subscriber("tf", TFMessage, callbackPub)
    rospy.spin()

if __name__ == '__main__':
    listener()