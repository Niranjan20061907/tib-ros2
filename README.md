# Tiburon Software Induction: ROS 2 Navigation & Communication

## 📌 Summary
This repository contains the software induction tasks for Team Tiburon, built using **ROS 2 Jazzy** on Ubuntu 24.04 (ARM64). It demonstrates core robotics software concepts across two main packages:
1. `tiburon_task1`: 2D kinematics, multi-agent tracking (Proportional control), and multithreaded GUI service calling using `turtlesim`.
2. `tiburon_task3`: Advanced ROS 2 node communication, featuring non-blocking frequency control and multi-sensor timestamp synchronization (IMU & Camera) using `message_filters`.

## 🚀 User Guide

### Prerequisites
* ROS 2 Jazzy installed on Ubuntu 24.04
* Python 3.12+ with `tkinter`
* `turtlesim` and `message_filters` ROS 2 packages

### Build & Install
```bash
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws/src
# Clone this repository here
cd ~/ros2_ws
colcon build
source install/setup.bash
