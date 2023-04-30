cmake_minimum_required(VERSION 3.16)
project(ros2_control_ams LANGUAGES CXX)

if(CMAKE_CXX_COMPILER_ID MATCHES "(GNU|Clang)")
  add_compile_options(-Wall -Wextra)
endif()

# find dependencies
set(THIS_PACKAGE_INCLUDE_DEPENDS
  hardware_interface
  pluginlib
  rclcpp
  rclcpp_lifecycle
)

# find dependencies
find_package(ament_cmake REQUIRED)
foreach(Dependency IN ITEMS ${THIS_PACKAGE_INCLUDE_DEPENDS})
  find_package(${Dependency} REQUIRED)
endforeach()

## COMPILE
add_library(
  ros2_control_ams
  SHARED
  hardware/ams_actuator.cpp
)
target_compile_features(ros2_control_ams PUBLIC cxx_std_17)
target_include_directories(ros2_control_ams PUBLIC
$<BUILD_INTERFACE:${PROJECT_SOURCE_DIR}/hardware/include>
$<INSTALL_INTERFACE:include/ros2_control_ams>
)
ament_target_dependencies(
  ros2_control_ams PUBLIC
  ${THIS_PACKAGE_INCLUDE_DEPENDS}
)

# Causes the visibility macros to use dllexport rather than dllimport,
# which is appropriate when building the dll but not consuming it.
target_compile_definitions(${PROJECT_NAME} PRIVATE "ROS2_CONTROL_AMS_BUILDING_DLL")

# Export hardware plugins
pluginlib_export_plugin_description_file(hardware_interface ros2_control_ams.xml)

# INSTALL
install(
  DIRECTORY hardware/include/
  DESTINATION include/ros2_control_ams
)
install(
  DIRECTORY description/launch description/ros2_control description/urdf description/meshes description/rviz
  DESTINATION share/ros2_control_ams
)
install(
  DIRECTORY bringup/launch bringup/config
  DESTINATION share/ros2_control_ams
)
install(TARGETS ros2_control_ams
	EXPORT export_ros2_control_ams
	ARCHIVE DESTINATION lib
	LIBRARY DESTINATION lib
	RUNTIME DESTINATION bin
)
if(BUILD_TESTING)
  find_package(ament_cmake_gtest REQUIRED)
endif()

## EXPORTS
ament_export_targets(export_ros2_control_ams HAS_LIBRARY_TARGET)
ament_export_dependencies(${THIS_PACKAGE_INCLUDE_DEPENDS})
ament_package()

