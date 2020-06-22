#include "ros/ros.h"
#include "sensor_msgs/PointCloud2"

void pcCallback(const sensor_msgs::PointCloud2::ConstPtr& msg)
{
  ROS_INFO("I heard: [%s]", msg->data.c_str());
}

int main(int argc, char **argv)
{
  ros::init(argc, argv, "listener_pc");
  ros::NodeHandle n;
  ros::Subscriber sub = n.subscribe("/camera/depth_registered/points", 1000, pcCallback);
  ros::spin();

  return 0;
}