#!/usr/bin/env python

# Author: christoph.roesmann@tu-dortmund.de

import rospy, math
from costmap_converter.msg import ObstacleArrayMsg, ObstacleMsg
from geometry_msgs.msg import PolygonStamped, Point32


def publish_obstacle_msg():
  pub = rospy.Publisher('/test_optim_node/obstacles', ObstacleArrayMsg, queue_size=1)
  #pub = rospy.Publisher('/p3dx/move_base/TebLocalPlannerROS/obstacles', ObstacleArrayMsg, queue_size=1)
  rospy.init_node("test_obstacle_msg")


  obstacle_msg = ObstacleArrayMsg() 
  obstacle_msg.header.stamp = rospy.Time.now()
  obstacle_msg.header.frame_id = "odom" # CHANGE HERE: odom/map
  
  # Add point obstacle
  obstacle_msg.obstacles.append(ObstacleMsg())
  obstacle_msg.obstacles[0].id = 0
  obstacle_msg.obstacles[0].polygon.points = [Point32()]
  obstacle_msg.obstacles[0].polygon.points[0].x = 0
  obstacle_msg.obstacles[0].polygon.points[0].y = -2.0
  obstacle_msg.obstacles[0].polygon.points[0].z = 0


  # Add line obstacle
  obstacle_msg.obstacles.append(ObstacleMsg())
  obstacle_msg.obstacles[1].id = 1
  line_a_start = Point32()
  line_a_start.x = -5.0
  line_a_start.y = 0.55
  
  line_a_end = Point32()
  line_a_end.x = -1.5
  line_a_end.y = 0.55
  
  obstacle_msg.obstacles[1].polygon.points = [line_a_start, line_a_end]
  

  obstacle_msg.obstacles.append(ObstacleMsg())
  obstacle_msg.obstacles[1].id =2
  line_b_start = Point32()
  line_b_start.x = -5.0
  line_b_start.y = -0.55
  
  line_b_end = Point32()
  line_b_end.x = 3.0
  line_b_end.y = -0.55
  
  obstacle_msg.obstacles[2].polygon.points = [line_b_start, line_b_end]
  

  obstacle_msg.obstacles.append(ObstacleMsg())
  obstacle_msg.obstacles[1].id = 3
  line_c_start = Point32()
  line_c_start.x = 0.0
  line_c_start.y = -2
  
  line_c_end = Point32()
  line_c_end.x = 0.0
  line_c_end.y = 2.0
  
  obstacle_msg.obstacles[3].polygon.points = [line_c_start, line_c_end]
  

  obstacle_msg.obstacles.append(ObstacleMsg())
  obstacle_msg.obstacles[1].id =4
  line_d_start = Point32()
  line_d_start.x = -2.0
  line_d_start.y = 2.0
  
  line_d_end = Point32()
  line_d_end.x = 0.0
  line_d_end.y = 2.0
  
  obstacle_msg.obstacles[4].polygon.points = [line_d_start, line_d_end]

  # Add polygon obstacle
  #obstacle_msg.obstacles.append(ObstacleMsg())
  #obstacle_msg.obstacles[1].id = 2
  #v1 = Point32()
  #v1.x = -1
  #v1.y = -1
  #v2 = Point32()
  #v2.x = -0.5
  #v2.y = -1.5
  #v3 = Point32()
  #v3.x = 0
  #v3.y = -1
  #obstacle_msg.obstacles[2].polygon.points = [v1, v2, v3]
  

  r = rospy.Rate(10) # 10hz
  t = 0.0
  while not rospy.is_shutdown():
    
    # Vary y component of the point obstacle
    #obstacle_msg.obstacles[0].polygon.points[0].y = 1*math.sin(t)
    #t = t + 0.1
    
    pub.publish(obstacle_msg)
    
    r.sleep()



if __name__ == '__main__': 
  try:
    publish_obstacle_msg()
  except rospy.ROSInterruptException:
    pass

