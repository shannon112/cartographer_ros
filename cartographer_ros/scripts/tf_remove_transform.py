#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright 2016 The Cartographer Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import rospy
from tf.msg import tfMessage


def main():
  rospy.init_node('tf_remove_transform')
  publisher = rospy.Publisher('/tf', tfMessage, queue_size=1)

  def callback(msg):
    # because there is a transformation between base_footprint and odom recorded,
    # it will conflict with cartographer broadcasting. Fortunely, that bad broadcasting length is unique and equal to 1
    if len(msg.transforms)>1:
      publisher.publish(msg)

  rospy.Subscriber('/tf_rm', tfMessage, callback)
  rospy.spin()


if __name__ == '__main__':
  main()
