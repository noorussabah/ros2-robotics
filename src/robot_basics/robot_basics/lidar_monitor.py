import math

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan


class LidarMonitor(Node):

    def __init__(self):
        super().__init__('lidar_monitor')

        self.subscription = self.create_subscription(
            LaserScan,
            '/scan',
            self.scan_callback,
            10
        )

        self.get_logger().info('LiDAR monitor started')

    def scan_callback(self, msg):

        # Store valid readings as:
        # (angle, distance)
        valid_readings = []

        for index, distance in enumerate(msg.ranges):

            # Ignore Inf, NaN, and out-of-range measurements
            if (
                not math.isfinite(distance)
                or distance < msg.range_min
                or distance > msg.range_max
            ):
                continue

            # Convert array index into LiDAR angle
            angle = (
                msg.angle_min
                + index * msg.angle_increment
            )

            # Normalize angle to -pi ... +pi
            angle = math.atan2(
                math.sin(angle),
                math.cos(angle)
            )

            valid_readings.append(
                (angle, distance)
            )

        if not valid_readings:
            self.get_logger().info(
                'No valid LiDAR readings'
            )
            return

        # ---------------------------------
        # Closest obstacle anywhere
        # ---------------------------------

        closest_angle, closest_distance = min(
            valid_readings,
            key=lambda reading: reading[1]
        )

        # ---------------------------------
        # Left side: 0° to +90°
        # ---------------------------------

        left_distances = [
            distance
            for angle, distance in valid_readings
            if 0.0 < angle <= math.pi / 2
        ]

        # ---------------------------------
        # Right side: -90° to 0°
        # ---------------------------------

        right_distances = [
            distance
            for angle, distance in valid_readings
            if -math.pi / 2 <= angle < 0.0
        ]

        left_clearance = (
            min(left_distances)
            if left_distances
            else float('inf')
        )

        right_clearance = (
            min(right_distances)
            if right_distances
            else float('inf')
        )

        # Convert closest angle to degrees
        closest_angle_degrees = math.degrees(
            closest_angle
        )

        # ---------------------------------
        # Print useful perception data
        # ---------------------------------

        self.get_logger().info(
            f'Closest: {closest_distance:.2f} m '
            f'at {closest_angle_degrees:.1f}° | '
            f'Left: {left_clearance:.2f} m | '
            f'Right: {right_clearance:.2f} m'
        )


def main(args=None):
    rclpy.init(args=args)

    node = LidarMonitor()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
