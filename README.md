# ROS 2 Robotics

A hands-on robotics project exploring robot software development with ROS 2, Gazebo, Python, and C++.

The project is being developed incrementally, starting from ROS communication and robot control and progressing toward perception, mapping, path planning, and autonomous navigation.

## Current Progress

### ROS 2 Communication
- Built publisher and subscriber nodes in Python
- Published simulated battery data over ROS topics
- Created a battery monitoring subscriber
- Implemented ROS 2 service client/server communication

### Robot Control
- Set up TurtleBot3 simulation in Gazebo
- Controlled robot motion through `/cmd_vel`
- Worked with `geometry_msgs/TwistStamped`
- Implemented autonomous forward and turning behavior
- Built a controller that drives the robot in a square without keyboard input

## Project Structure

```text
robot_basics/
├── battery_publisher.py
├── battery_monitor.py
├── calculator_server.py
├── calculator_client.py
└── square_driver.py
