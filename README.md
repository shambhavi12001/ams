# AMS (Autonomous Mechanical Spider)

## Installation
[Ubuntu 22.04.01 Installation on Pi](https://ubuntu.com/tutorials/how-to-install-ubuntu-on-your-raspberry-pi)<br />
[ROS2 Humble Intsallation](https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debians.html)<br />

## Dependencies
Install colcon
```bash
sudo apt install python3-colcon-common-extensions
```
Installing tf2 and dependencies
```bash
sudo apt-get install ros-humble-turtle-tf2-py ros-humble-tf2-tools ros-humble-tf-transformations
```
Installing ROS2 Control
```bash
sudo apt install ros-humble-ros2-control
```
```bash
sudo apt install ros-humble-ros2-controllers
```
Build from Source
```bash
wget https://raw.githubusercontent.com/ros-controls/ros2_control/master/ros2_control.rolling.repos
vcs import src < ros2_control.repos
```
Resolve Dependencies
```bash
# cd if you're still in the ``src`` directory with the ``ros_tutorials`` clone
cd ..
sudo rosdep init
rosdep update
rosdep install -i --from-path src --rosdistro humble -y
```

## ROS Drivers
[LiDAR](https://github.com/Slamtec/sllidar_ros2)
```bash
ros2 launch sllidar_ros2 sllidar_launch.py
```
[GPS Module](https://github.com/ros-drivers/nmea_navsat_driver/tree/ros2)
```bash
ros2 launch nmea_navsat_driver nmea_serial_driver.launch.py
```
[9DOF IMU- I2C](https://github.com/flynneva/bno055)
```bash
ros2 launch bno055 bno055.launch.py
```

## Build (ROS2 Packages)
Resolving dependencies-
```bash
rosdep install -i --from-path src --rosdistro humble -y
```
Building a package-
```bash
colcon build --packages-select <package_name>
```
Source setup files-
```bash
. install/setup.bash
```



