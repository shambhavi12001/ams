from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, ThisLaunchFileDir
def generate_launch_description():
    # Declare arguments
    declared_arguments = []
    declared_arguments.append(
        DeclareLaunchArgument(
            "prefix",
            default_value='""',
            description="Prefix of the joint names, useful for \
        multi-robot setup. If changed, joint names in the controllers' configuration \
        also have to be updated.",
        )
    )
    declared_arguments.append(
        DeclareLaunchArgument(
            "slowdown", default_value="3.0", description="Slowdown factor of the AMS."
        )
    )
    declared_arguments.append(
        DeclareLaunchArgument(
            "robot_controller",
            default_value="position_controllers",
            description="Robot controller to start.",
        )
    )
    # Initialize Arguments
    prefix = LaunchConfiguration("prefix")
    slowdown = LaunchConfiguration("slowdown")
    robot_controller = LaunchConfiguration("robot_controller")
    base_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([ThisLaunchFileDir(), "/ams_base.launch.py"]),
        launch_arguments={
            "controllers_file": "ams_actuators.yaml",
            "description_file": "ams_actuators.urdf.xacro",
            "prefix": prefix,
            "use_mock_hardware": "false",
            "slowdown": slowdown,
            "robot_controller": robot_controller,
        }.items(),
    )

    return LaunchDescription(declared_arguments + [base_launch])
