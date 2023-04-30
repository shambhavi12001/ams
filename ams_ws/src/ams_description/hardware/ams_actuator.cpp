
#include "ros2_control_ams/ams_actuator.hpp"

#include <chrono>
#include <cmath>
#include <limits>
#include <memory>
#include <vector>

#include "hardware_interface/actuator_interface.hpp"
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

  const hardware_interface::ComponentInfo & joint = info_.joints[0];
  // AMSPositionHardware has exactly one state and command interface on each joint
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
      rclcpp::get_logger("AMSPositionHardware"), "Joint '%s' has %zu state interface. 1 expected.",
      joint.name.c_str(), joint.state_interfaces.size());
    return hardware_interface::CallbackReturn::ERROR;
  }

  if (joint.state_interfaces[0].name != hardware_interface::HW_IF_POSITION)
  {
    RCLCPP_FATAL(
      rclcpp::get_logger("AMSPositionHardware"), "Joint '%s' have %s state interface. '%s' expected.",
      joint.name.c_str(), joint.state_interfaces[0].name.c_str(),
      hardware_interface::HW_IF_POSITION);
    return hardware_interface::CallbackReturn::ERROR;
  }

  return hardware_interface::CallbackReturn::SUCCESS;
}

std::vector<hardware_interface::StateInterface> AMSPositionHardware::export_state_interfaces()
{
  std::vector<hardware_interface::StateInterface> state_interfaces;

  state_interfaces.emplace_back(hardware_interface::StateInterface(
    info_.joints[0].name, hardware_interface::HW_IF_POSITION, &hw_joint_state_));

  return state_interfaces;
}

std::vector<hardware_interface::CommandInterface> AMSPositionHardware::export_command_interfaces()
{
  std::vector<hardware_interface::CommandInterface> command_interfaces;

  command_interfaces.emplace_back(hardware_interface::CommandInterface(
    info_.joints[0].name, hardware_interface::HW_IF_POSITION, &hw_joint_command_));

  return command_interfaces;
}

hardware_interface::CallbackReturn AMSPositionHardware::on_activate(
  const rclcpp_lifecycle::State & /*previous_state*/)
{
  // BEGIN: This part here is for exemplary purposes - Please do not copy to your production code
  RCLCPP_INFO(rclcpp::get_logger("AMSPositionHardware"), "Activating ...please wait...");

  for (int i = 0; i < hw_start_sec_; i++)
  {
    rclcpp::sleep_for(std::chrono::seconds(1));
    RCLCPP_INFO(rclcpp::get_logger("AMSPositionHardware"), "%.1f seconds left...", hw_start_sec_ - i);
  }
  // END: This part here is for exemplary purposes - Please do not copy to your production code

  // set some default values for joints
  if (std::isnan(hw_joint_state_))
  {
    hw_joint_state_ = 0;
    hw_joint_command_ = 0;
  }

  RCLCPP_INFO(rclcpp::get_logger("AMSPositionHardware"), "Successfully activated!");

  return hardware_interface::CallbackReturn::SUCCESS;
}

hardware_interface::CallbackReturn AMSPositionHardware::on_deactivate(
  const rclcpp_lifecycle::State & /*previous_state*/)
{
  // BEGIN: This part here is for exemplary purposes - Please do not copy to your production code
  RCLCPP_INFO(rclcpp::get_logger("AMSPositionHardware"), "Deactivating ...please wait...");

  for (int i = 0; i < hw_stop_sec_; i++)
  {
    rclcpp::sleep_for(std::chrono::seconds(1));
    RCLCPP_INFO(rclcpp::get_logger("AMSPositionHardware"), "%.1f seconds left...", hw_stop_sec_ - i);
  }

  RCLCPP_INFO(rclcpp::get_logger("AMSPositionHardware"), "Successfully deactivated!");
  // END: This part here is for exemplary purposes - Please do not copy to your production code

  return hardware_interface::CallbackReturn::SUCCESS;
}

hardware_interface::return_type AMSPositionHardware::read(
  const rclcpp::Time & /*time*/, const rclcpp::Duration & /*period*/)
{

  return hardware_interface::return_type::OK;
}

hardware_interface::return_type ros2_control_ams::AMSPositionHardware::write(
  const rclcpp::Time & /*time*/, const rclcpp::Duration & /*period*/)
{

  return hardware_interface::return_type::OK;
}

}  // namespace ros2_control_ams

#include "pluginlib/class_list_macros.hpp"

PLUGINLIB_EXPORT_CLASS(
  ros2_control_ams::AMSPositionHardware, hardware_interface::ActuatorInterface)

