# chef is the consumer

import pika
import json 
import time

connection=pika.BlockingConnection(
    pika.ConnectionParameters(host="localhost")
)

channel = connection.channel()

channel.queue_declare(queue="pizza-orders")

def cook_pizza(ch, method, properties, body):
    order=json.loads(body)
    
    print("\n🍕 ===== New Pizza Order =====")
    print(f"Customer : {order['customer']}")
    print(f"Pizza    : {order['pizza']}")
    print(f"Size     : {order['size']}")
    
    print("\n👨‍🍳 Cooking pizza...")
    time.sleep(5)  # Simulate cooking time
    
    print(":) Pizza ready !!!")
    ch.basic_ack(delivery_tag=method.delivery_tag)
    


channel.basic_consume(
    queue="pizza-orders",
    on_message_callback=cook_pizza
)

print("👨‍🍳 Chef is waiting for pizza orders...")

channel.start_consuming()