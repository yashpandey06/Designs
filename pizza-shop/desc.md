## 🍕 Pizza Order Flow

```text
Customer
    │
    ▼
Place Pizza Order
    │
    ▼
Cashier (Producer)
    │
    │ Publish Order
    ▼
RabbitMQ Queue
    │
    │ Deliver Order
    ▼
Chef (Consumer)
    │
    ▼
Receive Order
    │
    ▼
Start Cooking 🍕
    │
    ▼
Simulate Cooking (5 seconds)
    │
    ▼
Pizza Ready ✅
    │
    ▼
Send Acknowledgment (ACK)
    │
    ▼
RabbitMQ Removes the Order from the Queue
```

### What happens at each step?

1. **Customer** places a pizza order.
2. **Cashier (Producer)** receives the order and publishes it to RabbitMQ.
3. **RabbitMQ Queue** safely stores the order until a chef is available.
4. **Chef (Consumer)** receives the order from the queue.
5. The chef prepares the pizza (simulated with a 5-second delay).
6. Once the pizza is ready, the chef sends an **ACK (Acknowledgment)** to RabbitMQ.
7. After receiving the ACK, **RabbitMQ permanently removes the order from the queue**.

> **Why is ACK important?**
>
> RabbitMQ does **not** remove the message as soon as it delivers it to the consumer. It waits until the consumer explicitly says, **"I have successfully processed this order."**
>
> If the chef crashes before sending the ACK, RabbitMQ assumes the order was **not completed** and can deliver the same order to another chef. This ensures that no customer order is lost.