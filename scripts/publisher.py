#!/usr/bin/env python3
# license removed for brevity
import rospy
from std_msgs.msg import String

def publisher():
   pub = rospy.Publisher('topic', String, queue_size=10)
   rospy.init_node('publisher_node', anonymous=True)
   rate = rospy.Rate(10) # 10hz
   while not rospy.is_shutdown():
      hello_str = "hello world %s" % rospy.get_time()
      rospy.loginfo(hello_str)
      pub.publish(hello_str)
      rate.sleep()

      ## add add

if __name__ == '__main__':
   try:
      publisher()
   except rospy.ROSInterruptException:
      pass