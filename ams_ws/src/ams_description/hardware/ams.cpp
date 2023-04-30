#include "ams_hardware/ams.cpp"
#include <memory>
#include <string>
#include <vector>
#include <chrono>
#include <cmath>
#include <limits>

#include "hardware_interface/types/hardware_interface_type_values.hpp"
#include "rclcpp/rclcpp.hpp"

namespace ros2_control_ams
{
        hardware_interface::CallbackReturn AMSPositionHardware::on_init(
                const hardware_interface::HardwareInfo & info)
        {
                if (
                        hardware_interface::ActuatorInterface::on_init(info) !=
                        hardware_interface::CallbackReturn::SUCCESS)
                {
                        return hardware_interface::CallbackReturn::ERROR;
                }
                hw_joint_state_ = std::numeric_limits<double>::quiet_NaN();
                hw_joint_command_ = std::numeric_limits<double>::quiet_NaN();

                for (const hardware_interface::ComponentInfo & joint : info_.joints)
                {
                        if (joint.command_interfaces.size() != 1)
                        {
                                RCLCPP_FATAL(
                                                rclcpp::get_logger("AMSPositionHardware"),
                                                "Joint '%s' has %zu command interfaces found. 1 expected.", joint.name.c_str(),
                                                joint.command_interfaces.size());
                                return hardware_interface::CallbackReturn::ERROR;
                        }

                        if (joint.command_interfaces[0].name != hardware_interface::HW_IF_POSITION)
                        {
                                RCLCPP_FATAL(
                                                rclcpp::get_logger("AMSPositionHardware"),
                                                "Joint '%s' have %s command interfaces found. '%s' expected.", joint.name.c_str(),
                                                joint.command_interfaces[0].name.c_str(), hardware_interface::HW_IF_POSITION);
                                return hardware_interface::CallbackReturn::ERROR;
                        }

                        if (joint.state_interfaces.size() != 1)
                        {
                                RCLCPP_FATAL(
                                                rclcpp::get_logger("AMSPositionHardware"),
                                                "Joint '%s' has %zu state interface. 1 expected.", joint.name.c_str(),
                                                joint.state_interfaces.size());
                                return hardware_interface::CallbackReturn::ERROR;
				}

                        if (joint.state_interfaces[0].name != hardware_interface::HW_IF_POSITION)
                        {
                                RCLCPP_FATAL(
                                                rclcpp::get_logger("AMSPositionHardware"),
                                                "Joint '%s' have %s state interface. '%s' expected.", joint.name.c_str(),
                                                joint.state_interfaces[0].name.c_str(), hardware_interface::HW_IF_POSITION);
                                return hardware_interface::CallbackReturn::ERROR;
                        }

                }
                return hardware_interface::CallbackReturn::SUCCESS;
        }

        hardware_interface::CallbackReturn AMSPositionHardware::on_configure(
                        const rclcpp_lifecycle::State & /*previous_state*/)
        {
                RCLCPP_INFO(rclcpp::get_logger("AMSPositionHardware"), "Successfully configured!");
                return hardware_interface::CallbackReturn::SUCCESS;
        }


        std::vector<hardware_interface::StateInterface>
        AMSPositionHardware::export_state_interfaces()
        {
                std::vector<hardware_interface::StateInterface> state_interfaces;
                for (uint i = 0; i < info_.joints.size(); i++)
                {
                        state_interfaces.emplace_back(hardware_interface::StateInterface(
                                                info_.joints[i].name, hardware_interface::HW_IF_POSITION, &hw_states_[i]));
                }
                return state_interfaces;
        }

        std::vector<hardware_interface::CommandInterface>
        AMSPositionHardware::export_command_interfaces()
        {
                std::vector<hardware_interface::CommandInterface> command_interfaces;
                for (uint i = 0; i < info_.joints.size(); i++)
                {
                        command_interfaces.emplace_back(hardware_interface::CommandInterface(
                                                info_.joints[i].name, hardware_interface::HW_IF_POSITION, &hw_commands_[i]));
                }
                return command_interfaces;
        }
        hardware_interface::return_type AMSPositionHardware::on_activate(
                        const rclcpp_lifecycle::State & /*previous_state*/)
        {
                if (std::isnan(hw_joint_state_))
                {
                        hw_joint_state_ = 0;
                        hw_joint_command_ = 0;
                }
                RCLCPP_INFO(rclcpp::get_logger("AMSPositionHardware"), "Successfully activated!");
                return hardware_interface::CallbackReturn::SUCCESS;
        }

        hardware_interface::return_type AMSPositionHardware::on_deactivate(
                        const rclcpp_lifecycle::State & /*previous_state*/)
        {
                return hardware_interface::CallbackReturn::SUCCESS;
        }

        hardware_interface::return_type AMSPositionHardware::read(
                        const rclcpp::Time & /*time*/, const rclcpp::Duration & /*period*/)
        {
                return hardware_interface::return_type::OK;
        }

        hardware_interface::return_type AMSPositionHardware::write(
                        const rclcpp::Time & /*time*/, const rclcpp::Duration & /*period*/)
        {
                        return hardware_interface::return_type::OK;
        }

}
#include "pluginlib/class_list_macros.hpp"
PLUGINLIB_EXPORT_CLASS(
                ros2_control_ams::AMSPositionHardware, hardware_interface::ActuatorInterface)
