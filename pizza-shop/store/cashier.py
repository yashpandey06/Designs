# cashier is the producer

import pika
import json

connection=pika.BlockingConnection(
    pika.ConnectionParameters(host="localhost")
)

channel = connection.channel()

channel.queue_declare(queue="pizza-orders")

#  Pizza Order 

# Create a pizza order
order = {
    "customer": "Yash",
    "pizza": "Garlic Bread",
    "size": "small"
}

channel.basic_publish(
    exchange="",
    routing_key="pizza-orders",
    body=json.dumps(order)
)

print("🍕 Order sent to RabbitMQ!")

connection.close()