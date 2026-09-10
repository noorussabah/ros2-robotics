import rclpy
from rclpy.node import Node
from geometry_msgs.msg import TwistStamped


class SquareDriver(Node):

    def __init__(self):
        super().__init__('square_driver')

        self.publisher = self.create_publisher(
            TwistStamped,
            '/cmd_vel',
            10
        )

        self.state = 'FORWARD'
        self.counter = 0

        self.timer = self.create_timer(
            0.1,
            self.timer_callback
        )

    def timer_callback(self):
        msg = TwistStamped()

        if self.state == 'FORWARD':
            msg.twist.linear.x = 0.15
            msg.twist.angular.z = 0.0

            self.counter += 1

            if self.counter >= 30:
                self.state = 'TURN'
                self.counter = 0

        elif self.state == 'TURN':
            msg.twist.linear.x = 0.0
            msg.twist.angular.z = 0.8

            self.counter += 1

            if self.counter >= 20:
                self.state = 'FORWARD'
                self.counter = 0

        self.publisher.publish(msg)


def main(args=None):
    rclpy.init(args=args)

    node = SquareDriver()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
