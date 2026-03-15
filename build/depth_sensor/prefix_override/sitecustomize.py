import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/niranjan/tiburon-projects/ros2_ws/install/depth_sensor'
