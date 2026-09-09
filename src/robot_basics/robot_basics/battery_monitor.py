import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32


class BatteryMonitor(Node):

    def __init__(self):
        super().__init__('battery_monitor')

        self.subscription = self.create_subscription(
            Float32,
            'battery_level',
            self.battery_callback,
            10
        )

    def battery_callback(self, msg):

        if msg.data <= 20:
            self.get_logger().warn(
                f'LOW BATTERY: {msg.data:.1f}%'
            )
        else:
            self.get_logger().info(
                f'Battery OK: {msg.data:.1f}%'
            )


def main(args=None):
    rclpy.init(args=args)

    node = BatteryMonitor()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
