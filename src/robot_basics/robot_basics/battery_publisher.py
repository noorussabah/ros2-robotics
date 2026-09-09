import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32


class BatteryPublisher(Node):

    def __init__(self):
        super().__init__('battery_publisher')

        self.publisher_ = self.create_publisher(
            Float32,
            'battery_level',
            10
        )

        self.battery = 100.0

        self.timer = self.create_timer(
            1.0,
            self.publish_battery
        )

    def publish_battery(self):
        msg = Float32()
        msg.data = self.battery

        self.publisher_.publish(msg)

        self.get_logger().info(
            f'Battery: {self.battery:.1f}%'
        )

        self.battery -= 5.0

        if self.battery < 0:
            self.battery = 100.0


def main(args=None):
    rclpy.init(args=args)

    node = BatteryPublisher()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
