import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math
import time

class ShapeDrawer(Node):
    def __init__(self):
        super().__init__('shape_drawer')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.pose_subscriber = self.create_subscription(Pose, '/turtle1/pose', self.update_pose, 10)
        self.current_pose = Pose()
        self.get_logger().info('Shape Drawer started. Waiting a second to connect...')
        time.sleep(1)

    def update_pose(self, data):
        self.current_pose = data

    def draw_square(self, side_length=2.0):
        self.get_logger().info('Drawing a square...')
        msg = Twist()
        for _ in range(4):
            # Move forward
            msg.linear.x = side_length
            msg.angular.z = 0.0
            self.publisher_.publish(msg)
            time.sleep(1.0)
            
            # Turn 90 degrees
            msg.linear.x = 0.0
            msg.angular.z = math.pi / 2  # 90 degrees in radians
            self.publisher_.publish(msg)
            time.sleep(1.0)
            
        msg.angular.z = 0.0
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = ShapeDrawer()
    node.draw_square()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()