import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class NavigationNode(Node):
    def __init__(self):
        super().__init__('navigation_node')
        
        # Subscribe to the depth sensor topic
        self.subscription = self.create_subscription(
            Float32,
            '/rov/depth',
            self.depth_callback,
            10
        )
        self.get_logger().info('Navigation Node started — listening for depth data!')

    def depth_callback(self, msg):
        depth = msg.data
        
        # React to depth readings — ROV decision making
        if depth < 5.0:
            action = '⚠️  TOO SHALLOW — ascending risk!'
        elif depth > 25.0:
            action = '🔴 TOO DEEP — emergency ascend!'
        else:
            action = '✅ DEPTH NOMINAL — holding position'
            
        self.get_logger().info(f'Depth received: {depth:.2f}m → {action}')

def main(args=None):
    rclpy.init(args=args)
    node = NavigationNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
