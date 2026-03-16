import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import random
from depth_sensor.crypto_utils import encrypt_depth

class DepthSensorNode(Node):
    def __init__(self):
        super().__init__('depth_sensor')
        
        # Now publishes String instead of Float32
        # because encrypted data is a string
        self.publisher = self.create_publisher(String, '/rov/depth', 10)
        self.timer = self.create_timer(1.0, self.send_depth)
        self.get_logger().info('Depth Sensor Node started — encryption enabled 🔐')

    def send_depth(self):
        raw_depth = round(random.uniform(0.0, 30.0), 2)
        
        # Encrypt before publishing
        encrypted = encrypt_depth(raw_depth)
        
        msg = String()
        msg.data = encrypted
        
        self.publisher.publish(msg)
        self.get_logger().info(f'Raw: {raw_depth}m → Encrypted: {encrypted[:30]}...')

def main(args=None):
    rclpy.init(args=args)
    node = DepthSensorNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()