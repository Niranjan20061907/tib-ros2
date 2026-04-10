# Team Tiburon Software Induction: ROS 2 Navigation & Communication

**Author:** Niranjan Krishnarajarajan - 124cs0009  
**Tech Stack:** ROS 2 Jazzy, Python 3.12, Ubuntu 24.04 LTS (ARM64), Tkinter  

## 📌 Project Overview
This repository contains the software induction tasks for Team Tiburon. The objective is to demonstrate proficiency in core robotics software concepts, including 2D kinematics, asynchronous multi-threading, dynamic multi-agent tracking, precise execution timing, multi-sensor data synchronization, and secure inter-node communication.

The workspace is divided into three primary packages:
1. **`tiburon_task1`**: 2D kinematics, multi-agent tracking (Proportional control), and multithreaded GUI service calling using `turtlesim`.
2. **`tiburon_task3`**: Advanced ROS 2 node communication, featuring non-blocking frequency control and multi-sensor timestamp synchronization using `message_filters`.
3. **`depth_sensor`**: Secure data transmission simulating ROV depth readings using AES-128 encryption.

---

## 🎥 Demonstration

[Task 1](https://drive.google.com/file/d/159mcSikkLCl1vF2VjTflnx8rBMfVAbDW/view?usp=sharing)
[Task 3](https://drive.google.com/file/d/14OEnMoRFZGx5zVZTDgvilmAC42mVAyUr/view?usp=sharing)

---

## 🧠 Problem Analysis & Solutions

### Task 1: Concurrency and Thread Blocking
**Problem:** Running a Tkinter `mainloop()` and a ROS 2 `rclpy.spin()` in the same thread causes a deadlock, freezing either the GUI or the ROS node.
**Solution:** A multi-threaded architecture was implemented. The ROS 2 Node runs on the main thread, while the Tkinter GUI is pushed to a background daemon thread. This allows UI buttons to safely trigger asynchronous ROS 2 service clients (`/reset`, `/spawn`, etc.) without interrupting the executor.

### Task 1: Dynamic Target Tracking
**Problem:** An agent must continuously adjust its velocity to track a moving target without erratic oscillations.
**Solution:** A geometric **Proportional (P) Controller** was utilized. The follower calculates linear velocity based on Euclidean distance, and angular velocity using `math.atan2` to find the target heading.

### Task 3: Execution Timing (Frequency Control)
**Problem:** Using `time.sleep()` blocks the entire thread, preventing the node from receiving callbacks.
**Solution:** Native ROS 2 Timers (`create_timer(0.1)`) were used to hook directly into the executor, guaranteeing that the publisher fires precisely at 10Hz without blocking background operations.

### Task 3: Asynchronous Data Synchronization
**Problem:** Disparate sensors (Camera, IMU) publish at different frequencies. Processing misaligned timestamps causes catastrophic failures in perception algorithms.
**Solution:** The `message_filters.ApproximateTimeSynchronizer` buffers incoming streams. Callbacks are only triggered when it identifies a pair of messages whose timestamps fall within a strict 0.1-second tolerance window.

### Depth Sensor: Secure Communication
**Problem:** Simulated physical data needed to be transmitted securely between nodes to prevent interception or tampering.
**Solution:** An AES-128 encryption pipeline (via the `cryptography.fernet` library) encrypts depth values before publishing them over standard `String` messages. The navigation node securely decrypts this payload to determine safety protocols (e.g., ascending if too deep).

---

## ⚖️ Architectural Trade-offs

* **Tkinter vs. PyQt:** Tkinter was chosen over PyQt. While PyQt offers robust "signals and slots," Tkinter requires zero heavy external dependencies, keeping the workspace highly portable and fast to deploy.
* **P-Control vs. PID:** A full PID controller was evaluated but deemed unnecessary mathematical overhead for `turtlesim` (a frictionless 2D environment). P-Control provided the optimal balance of simplicity and smooth tracking.
* **Approximate vs. Exact Synchronization:** `ExactTimeSynchronizer` mandates nanosecond-perfect alignment, which drops nearly 100% of packets in real-world hardware due to network jitter. `ApproximateTimeSynchronizer` was selected because it realistically mirrors physical ROV deployments.

---

## 🚀 Installation & Setup

### Prerequisites
* ROS 2 Jazzy installed on Ubuntu 24.04
* Python 3.12+
* `turtlesim` and `message_filters` ROS 2 packages
* `cryptography` Python package (for the depth sensor)



### Build Instructions
```bash
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws/src
# Clone this repository into the src folder
git clone [https://github.com/Niranjan20061907/tib-ros2.git](https://github.com/Niranjan20061907/tib-ros2.git) .
cd ~/ros2_ws
colcon build --symlink-install
source install/setup.bash
