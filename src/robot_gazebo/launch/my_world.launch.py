import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import ExecuteProcess, SetEnvironmentVariable


def generate_launch_description():

    # Our robot_gazebo package
    package_share = get_package_share_directory('robot_gazebo')

    # Our custom SDF world
    world_file = os.path.join(
        package_share,
        'worlds',
        'my_world.sdf'
    )

    # TurtleBot3 Gazebo package
    turtlebot3_gazebo_share = get_package_share_directory(
        'turtlebot3_gazebo'
    )

    # Gazebo needs this path to find TurtleBot3 meshes
    turtlebot_models = os.path.join(
        turtlebot3_gazebo_share,
        'models'
    )

    existing_resource_path = os.environ.get(
        'GZ_SIM_RESOURCE_PATH',
        ''
    )

    resource_path = (
        turtlebot_models
        + os.pathsep
        + '/opt/ros/jazzy/share'
        + os.pathsep
        + existing_resource_path
    )

    return LaunchDescription([

        # Fix TurtleBot mesh lookup
        SetEnvironmentVariable(
            name='GZ_SIM_RESOURCE_PATH',
            value=resource_path
        ),

        # Start Gazebo with our world
        ExecuteProcess(
            cmd=['gz', 'sim', '-r', world_file],
            output='screen'
        ),

        # Spawn TurtleBot3 Burger
        ExecuteProcess(
            cmd=[
                'ros2', 'run', 'ros_gz_sim', 'create',
                '-world', 'my_world',
                '-file',
                '/opt/ros/jazzy/share/turtlebot3_gazebo/models/turtlebot3_burger/model.sdf',
                '-name', 'turtlebot3',
                '-x', '0',
                '-y', '2',
                '-z', '0.05'
            ],
            output='screen'
        ),
	# Bridge ROS 2 /cmd_vel to Gazebo /cmd_vel
        ExecuteProcess(
            cmd=[
                'ros2',
                'run',
                'ros_gz_bridge',
                'parameter_bridge',
                '/cmd_vel@geometry_msgs/msg/Twist@gz.msgs.Twist'
            ],
            output='screen'
        ),
	# Bridge Gazebo /scan to ROS 2 /scan
	ExecuteProcess(
	    cmd=[
	        'ros2',
	        'run',
	        'ros_gz_bridge',
	        'parameter_bridge',
	        '/scan@sensor_msgs/msg/LaserScan@gz.msgs.LaserScan'
	    ],
	    output='screen'
	),
    ])
