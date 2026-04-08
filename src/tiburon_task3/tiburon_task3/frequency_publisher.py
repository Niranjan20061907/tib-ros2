import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class FrequencyPublisher(Node):
    def __init__(self):
        super().__init__('freq_publisher')
        self.publisher_ = self.create_publisher(String, 'sensor_data', 10)
        
        # Frequency Control: 10 Hz = 0.1 seconds per tick
        timer_period = 0.1  
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = String()
        msg.data = f'Data packet: {self.i} (Published exactly at 10Hz)'
        self.get_logger().info(f'Publishing: "{msg.data}"')
        self.publisher_.publish(msg)
        self.i += 1

def main(args=None):
    rclpy.init(args=args)
    node = FrequencyPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()