#!/usr/bin/python3
import rclpy
from rclpy.node import Node
from person_msgs.msg import Int16

class Talker():
    def__init__(self, node):
       self.pub = node.create_publisher(Int16, "countup", 10)
       self.n = 0
       node.create_timer(0.5, self.cb)
    
    def cb(self):
       msg = Int16()
       msg.date = self.n
       self.pub.publish(msg)
       self.n += 1
def main():
    rclpy.init()
    node = Node("talker")
    talker = Talker(node)
    rclpy.spin(node)
