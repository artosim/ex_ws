#HW 1
Выполнить в терминале следующие команды:
```
roscore 
rosrun turtlesim turtlesim_node
rosrun turtlesim turtle_teleop_key
rosservice call /spawn "{x: 5.0, y: 5.0, theta: 3.1415, name: 'leo'}"
catkin_make
source devel/setup.bash
rosrun turtle_commander catch_up.py
```
