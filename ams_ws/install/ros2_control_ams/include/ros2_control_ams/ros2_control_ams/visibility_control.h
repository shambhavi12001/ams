#ifndef ROS2_CONTROL_AMS__VISIBILITY_CONTROL_H_
#define ROS2_CONTROL_AMS__VISIBILITY_CONTROL_H_

#if defined _WIN32 || defined __CYGWIN__
#ifdef __GNUC__
#define ROS2_CONTROL_AMS_EXPORT __attribute__((dllexport))
#define ROS2_CONTROL_AMS_IMPORT __attribute__((dllimport))
#else
#define ROS2_CONTROL_AMS_EXPORT __declspec(dllexport)
#define ROS2_CONTROL_AMS_IMPORT __declspec(dllimport)
#endif
#ifdef ROS2_CONTROL_AMS_BUILDING_DLL
#define ROS2_CONTROL_AMS_PUBLIC ROS2_CONTROL_AMS_EXPORT
#else
#define ROS2_CONTROL_DEMO_EXAMPLE_6_PUBLIC ROS2_CONTROL_DEMO_EXAMPLE_6_IMPORT
#endif
#define ROS2_CONTROL_AMS_PUBLIC_TYPE ROS2_CONTROL_AMS_PUBLIC
#define ROS2_CONTROL_AMS_LOCAL
#else
#define ROS2_CONTROL_AMS__EXPORT __attribute__((visibility("default")))
#define ROS2_CONTROL_AMS_IMPORT
#if __GNUC__ >= 4
#define ROS2_CONTROL_AMS_PUBLIC __attribute__((visibility("default")))
#define ROS2_CONTROL_AMS_LOCAL __attribute__((visibility("hidden")))
#else
#define ROS2_CONTROL_AMS_PUBLIC
#define ROS2_CONTROL_AMS_LOCAL
#endif
#define ROS2_CONTROL_AMS_PUBLIC_TYPE
#endif

#endif
