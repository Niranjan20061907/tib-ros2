import rclpy
from rclpy.node import Node
from std_srvs.srv import Empty
from turtlesim.srv import Spawn, SetPen
import tkinter as tk
import threading
import random

class GuiNode(Node):
    def __init__(self):
        super().__init__('tkinter_gui_node')
        self.reset_cli = self.create_client(Empty, '/reset')
        self.clear_cli = self.create_client(Empty, '/clear')
        self.spawn_cli = self.create_client(Spawn, '/spawn')
        self.pen_cli = self.create_client(SetPen, '/turtle1/set_pen')

    def call_reset(self):
        self.reset_cli.call_async(Empty.Request())

    def call_clear(self):
        self.clear_cli.call_async(Empty.Request())

    def call_spawn(self):
        req = Spawn.Request()
        req.x, req.y, req.theta = random.uniform(2.0, 8.0), random.uniform(2.0, 8.0), 0.0
        req.name = f"turtle_{random.randint(2,100)}"
        self.spawn_cli.call_async(req)

    def call_random_pen(self):
        req = SetPen.Request()
        req.r, req.g, req.b = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
        req.width = 3
        req.off = 0
        self.pen_cli.call_async(req)

def run_gui(node):
    root = tk.Tk()
    root.title("Tiburon Turtlesim Control")
    root.geometry("300x250")

    tk.Label(root, text="Turtlesim Control Panel", font=("Arial", 14)).pack(pady=10)
    tk.Button(root, text="Reset Turtlesim", command=node.call_reset, width=20).pack(pady=5)
    tk.Button(root, text="Clear Background", command=node.call_clear, width=20).pack(pady=5)
    tk.Button(root, text="Spawn Random Turtle", command=node.call_spawn, width=20).pack(pady=5)
    tk.Button(root, text="Random Pen Color", command=node.call_random_pen, width=20).pack(pady=5)

    root.mainloop()

def main(args=None):
    rclpy.init(args=args)
    gui_node = GuiNode()
    
    # Run GUI in background thread
    threading.Thread(target=run_gui, args=(gui_node,), daemon=True).start()
    
    rclpy.spin(gui_node)
    gui_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()