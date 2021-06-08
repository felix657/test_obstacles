# test_obstacles
my test seting

in TebLocalPlannerReconfigure.cfg

line 122:
grp_robot_carlike.add("max_steering_rate", double_t, 0,
  "EXPERIMENTAL: Maximum steering rate of a carlike robot (THIS SIGNIFICANTLY AFFECTS PERFORMANCE AT THE MOMENT) [deactivate: zero]",
  1.5, 1.0, 10.0)

line 286:
grp_optimization.add("weight_max_steering_rate", double_t, 0, 
  "EXPERIMENTAL: Optimization weight for enforcing a minimum steering rate of a carlike robot (TRY TO KEEP THE WEIGHT LOW OR DEACTIVATE, SINCE IT SIGNIFICANTLY AFFECTS PERFORMANCE AT THE MOMENT)",
  10, 10, 100)
  
  in rosrun rqt_reconfigure rqt_reconfigure
  weight_obstacle = 200
  min_turning_radius = 50
  wheelbase = 1
