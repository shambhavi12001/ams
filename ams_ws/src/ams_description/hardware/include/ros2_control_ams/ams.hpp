#ifndef ROS2_CONTROL_AMS_HPP_
#define ROS2_CONTROL_AMS_HPP_
#include "hardware_interface/actuator_interface.hpp"
#include "rclcpp/macros.hpp"
#include "hardware_interface/types/hardware_interface_return_values.hpp"
#include "hardware_interface/handle.hpp"
#include "hardware_interface/hardware_info.hpp"
#include "rclcpp_lifecycle/node_interfaces/lifecycle_node_interface.hpp"
#include "rclcpp_lifecycle/state.hpp"
#include <memory>
#include <string>
#include <vector>
namespace ros2_control_ams
{
        class AMSPositionHardware : public hardware_interface::ActuatorInterface
        {
                public:
                        RCLCPP_SHARED_PTR_DEFINITIONS(AMSPositionHardware);
                        ROS2_CONTROL_AMS_PUBLIC
                        hardware_interface::CallbackReturn on_init(
                                const hardware_interface::HardwareInfo & info) override;

                        ROS2_CONTROL_AMS_PUBLIC
                        hardware_interface::CallbackReturn on_configure(
                                const rclcpp_lifecycle::State & previous_state) override;

                        ROS2_CONTROL_AMS_PUBLIC
                        std::vector<hardware_interface::StateInterface> export_state_interfaces() override;

                        ROS2_CONTROL_AMS_PUBLIC
                        std::vector<hardware_interface::CommandInterface> export_command_interfaces() override;

                        ROS2_CONTROL_AMS_PUBLIC
                        hardware_interface::CallbackReturn on_activate(
                                const rclcpp_lifecycle::State & previous_state) override;

                        ROS2_CONTROL_AMS_PUBLIC
                        hardware_interface::CallbackReturn on_deactivate(
                                const rclcpp_lifecycle::State & previous_state) override;

                        ROS2_CONTROL_AMS_PUBLIC
                        hardware_interface::return_type on_cleanup(
                                const rclcpp::Time & time, const rclcpp::Duration & period) override;
                        ROS2_CONTROL_AMS_PUBLIC
                        hardware_interface::return_type on_shutdown(
                                const rclcpp::Time & time, const rclcpp::Duration & period) override;

                        ROS2_CONTROL_AMS_PUBLIC
                        hardware_interface::return_type on_error(
                                const rclcpp::Time & time, const rclcpp::Duration & period) override;
			ROS2_CONTROL_AMS_PUBLIC
                        hardware_interface::return_type read(
                                const rclcpp::Time & time, const rclcpp::Duration & period) override;

                        ROS2_CONTROL_AMS_PUBLIC
                        hardware_interface::return_type write(
                                const rclcpp::Time & time, const rclcpp::Duration & period) override;
                private:
                        // Parameters for the RRBot simulation
                        double hw_start_sec_;
                        double hw_stop_sec_;
                        double hw_slowdown_;

                        // Store the command for the simulated robot
                        double hw_joint_command_;
                        double hw_joint_state_;

        };
}
#endif
