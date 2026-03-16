import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from depth_sensor.crypto_utils import decrypt_depth

class NavigationNode(Node):
    def __init__(self):
        super().__init__('navigation_node')
        
        # Now subscribes to String (encrypted data)
        self.subscription = self.create_subscription(
            String,
            '/rov/depth',
            self.depth_callback,
            10
        )
        self.get_logger().info('Navigation Node started — decryption enabled 🔐')

    def depth_callback(self, msg):
        # Decrypt the incoming message
        depth = decrypt_depth(msg.data)
        
        # Same safety logic as before
        if depth < 5.0:
            action = '⚠️  TOO SHALLOW — ascending risk!'
        elif depth > 25.0:
            action = '🔴 TOO DEEP — emergency ascend!'
        else:
            action = '✅ DEPTH NOMINAL — holding position'
            
        self.get_logger().info(f'Decrypted depth: {depth:.2f}m → {action}')

def main(args=None):
    rclpy.init(args=args)
    node = NavigationNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()