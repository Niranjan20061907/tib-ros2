import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import random

class DepthSensorNode(Node):
    def __init__(self):
        # Initialize the node with a name
        super().__init__('depth_sensor')
        
        # Create a publisher
        # Topic: /rov/depth
        # Message type: Float32
        # Queue size: 10
        self.publisher = self.create_publisher(Float32, '/rov/depth', 10)
        
        # Create a timer that calls send_depth every 1 second
        self.timer = self.create_timer(1.0, self.send_depth)
        
        self.get_logger().info('Depth Sensor Node started!')

    def send_depth(self):
        msg = Float32()
        # Simulate depth reading between 0 and 30 meters
        msg.data = round(random.uniform(0.0, 30.0), 2)
        
        # Publish to /rov/depth topic
        self.publisher.publish(msg)
        self.get_logger().info(f'Publishing depth: {msg.data} meters')

def main(args=None):
    rclpy.init(args=args)          # Start ROS 2
    node = DepthSensorNode()       # Create our node
    rclpy.spin(node)               # Keep it running
    rclpy.shutdown()               # Clean up

if __name__ == '__main__':
    main()
