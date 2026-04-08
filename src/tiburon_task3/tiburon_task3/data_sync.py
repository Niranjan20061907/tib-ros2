import rclpy
from rclpy.node import Node
import message_filters
from sensor_msgs.msg import Image, Imu

class DataSyncNode(Node):
    def __init__(self):
        super().__init__('data_sync_node')
        
        # 1. Create message_filters subscribers (Notice we don't pass '10' for QoS here)
        self.image_sub = message_filters.Subscriber(self, Image, '/camera/image_raw')
        self.imu_sub = message_filters.Subscriber(self, Imu, '/imu/data')
        
        # 2. Synchronize them based on their header.stamp
        # queue_size=10, slop=0.1 (allows max 0.1s time difference between msgs)
        self.ts = message_filters.ApproximateTimeSynchronizer(
            [self.image_sub, self.imu_sub], queue_size=10, slop=0.1)
        
        # 3. Register the callback
        self.ts.registerCallback(self.sync_callback)
        self.get_logger().info('Data Sync Node started. Waiting for synchronized Image and IMU data...')

    def sync_callback(self, image_msg, imu_msg):
        # This only triggers when a matching pair is found
        image_time = f"{image_msg.header.stamp.sec}.{image_msg.header.stamp.nanosec}"
        imu_time = f"{imu_msg.header.stamp.sec}.{imu_msg.header.stamp.nanosec}"
        
        self.get_logger().info(f'Synced! Image Time: {image_time} | IMU Time: {imu_time}')

def main(args=None):
    rclpy.init(args=args)
    node = DataSyncNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()