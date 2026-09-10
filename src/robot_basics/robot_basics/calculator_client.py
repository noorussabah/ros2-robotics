import sys

import rclpy
from rclpy.node import Node

from example_interfaces.srv import AddTwoInts


class CalculatorClient(Node):

    def __init__(self):
        super().__init__('calculator_client')

        self.client = self.create_client(
            AddTwoInts,
            'add_two_ints'
        )

        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for calculator service...')


    def send_request(self, a, b):

        request = AddTwoInts.Request()

        request.a = a
        request.b = b

        self.future = self.client.call_async(request)

        rclpy.spin_until_future_complete(self, self.future)

        return self.future.result()


def main(args=None):

    rclpy.init(args=args)

    node = CalculatorClient()

    a = int(sys.argv[1])
    b = int(sys.argv[2])

    response = node.send_request(a, b)

    node.get_logger().info(
        f'{a} + {b} = {response.sum}'
    )

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

