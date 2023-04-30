
from launch import LaunchDescription
from launch.substitutions import PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():

    position_goals = PathJoinSubstitution(
        [
            FindPackageShare("ros2_control_ams"),
            "config",
            "ams_position_controllers.yaml",
        ]   
    )
    return LaunchDescription(
        [
            Node(
                package="ros2_controllers_test_nodes",
                executable="publisher_position_controllers",
                name="publisher_position_controllers",
                parameters=[position_goals],
                output="both",
            )
        ]
    )
