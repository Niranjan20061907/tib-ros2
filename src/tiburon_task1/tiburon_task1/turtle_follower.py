import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from turtlesim.srv import Spawn
import math

class FollowerNode(Node):
    def __init__(self):
        super().__init__('turtle_follower')
        
        # 1. Spawn "girl" turtle
        self.spawn_cli = self.create_client(Spawn, '/spawn')
        self.spawn_girl()

        # 2. Publishers & Subscribers
        self.girl_pub = self.create_publisher(Twist, '/girl/cmd_vel', 10)
        self.follower_pub = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        
        self.girl_pose = Pose()
        self.follower_pose = Pose()

        self.create_subscription(Pose, '/girl/pose', self.update_girl_pose, 10)
        self.create_subscription(Pose, '/turtle1/pose', self.update_follower_pose, 10)

        # 3. Control Loop (20 Hz)
        self.timer = self.create_timer(0.05, self.control_loop)

    def spawn_girl(self):
        while not self.spawn_cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for spawn service...')
        req = Spawn.Request()
        req.x, req.y, req.theta, req.name = 8.0, 8.0, 0.0, "girl"
        self.spawn_cli.call_async(req)

    def update_girl_pose(self, msg):
        self.girl_pose = msg

    def update_follower_pose(self, msg):
        self.follower_pose = msg

    def control_loop(self):
        # Make the girl move in a continuous circle
        girl_msg = Twist()
        girl_msg.linear.x = 2.0
        girl_msg.angular.z = 1.0
        self.girl_pub.publish(girl_msg)

        # Calculate distance and angle for the follower (turtle1)
        distance = math.sqrt((self.girl_pose.x - self.follower_pose.x)**2 + 
                             (self.girl_pose.y - self.follower_pose.y)**2)
        angle_to_target = math.atan2(self.girl_pose.y - self.follower_pose.y, 
                                     self.girl_pose.x - self.follower_pose.x)

        # Proportional controller math
        follower_msg = Twist()
        if distance > 0.5: # Stop if close enough
            follower_msg.linear.x = 1.5 * distance
            follower_msg.angular.z = 4.0 * (angle_to_target - self.follower_pose.theta)
        
        self.follower_pub.publish(follower_msg)

def main(args=None):
    rclpy.init(args=args)
    node = FollowerNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()