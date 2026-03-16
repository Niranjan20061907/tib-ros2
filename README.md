# Tiburon ROV — Encrypted Depth Sensor System

A ROS 2 simulation of a secure underwater ROV communication system.
Built as preparation for the Tiburon robotics club software role.

## System Architecture
```
depth_sensor_node  →  encrypts data  →  /rov/depth topic  →  decrypts  →  navigation_node
```

## Nodes

### depth_sensor_node
- Simulates a depth sensor reading every 1 second
- Encrypts readings using AES-128 before publishing
- Publishes to `/rov/depth` topic

### navigation_node
- Subscribes to `/rov/depth` topic
- Decrypts incoming depth readings
- Makes safety decisions based on depth:
  - Below 5m → TOO SHALLOW
  - Above 25m → TOO DEEP  
  - 5-25m → DEPTH NOMINAL

### crypto_utils
- AES-128 encryption via Python cryptography library
- Shared key architecture (production would use HSM/TPM)
- Prevents unauthorized nodes from reading sensor data

## Security Concepts Demonstrated
- Symmetric encryption (AES-128) for real-time sensor data
- Key distribution architecture
- Encrypted pub/sub communication
- Defence against man-in-the-middle attacks on ROS 2 topics

## Computer Architecture Concepts Demonstrated
- Publisher/Subscriber communication model
- Real-time data processing with ROS 2
- ARM64 deployment (same architecture as Raspberry Pi)
- Inter-process communication via DDS middleware

## Tech Stack
- ROS 2 Jazzy
- Ubuntu 24.04 LTS ARM64
- Python 3.12
- cryptography library (AES-128/Fernet)

## Running the System

### Terminal 1 — Start depth sensor
```bash
source /opt/ros/jazzy/setup.bash
source install/setup.bash
ros2 run depth_sensor depth_sensor_node
```

### Terminal 2 — Start navigation node
```bash
source /opt/ros/jazzy/setup.bash
source install/setup.bash
ros2 run depth_sensor navigation_node
```

## What's Next
- HMAC authentication for command verification
- Multiple sensor nodes (pressure, temperature, IMU)
- Emergency protocol automation
- ROS 2 launch file for single-command startup