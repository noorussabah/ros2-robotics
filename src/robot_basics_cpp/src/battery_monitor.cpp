#include <memory>

#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/float32.hpp"

class BatteryMonitor : public rclcpp::Node
{
public:
  BatteryMonitor()
  : Node("battery_monitor_cpp")
  {
    subscription_ = this->create_subscription<std_msgs::msg::Float32>(
      "/battery_level",
      10,
      std::bind(&BatteryMonitor::battery_callback, this, std::placeholders::_1)
    );
  }

private:
  void battery_callback(const std_msgs::msg::Float32::SharedPtr msg)
  {
    RCLCPP_INFO(
      this->get_logger(),
      "Battery level: %.2f",
      msg->data
    );
  }

  rclcpp::Subscription<std_msgs::msg::Float32>::SharedPtr subscription_;
};

int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<BatteryMonitor>());
  rclcpp::shutdown();

  return 0;
}
