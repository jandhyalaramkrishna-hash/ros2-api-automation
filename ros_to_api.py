import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import requests

class ApiPublisher(Node):

    def __init__(self):
        super().__init__('api_publisher')
        self.subscription = self.create_subscription(
            String,
            'chatter',
            self.listener_callback,
            10)

    def listener_callback(self, msg):
        data = {"message": msg.data}
        try:
            response = requests.post("http://localhost:5000/data", json=data)
            self.get_logger().info(f"Sent to API: {data}")
        except Exception as e:
            self.get_logger().error(f"Error: {e}")

def main(args=None):
    rclpy.init(args=args)
    node = ApiPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
