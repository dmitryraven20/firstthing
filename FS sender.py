import time
import paho.mqtt.client as paho
import random

def on_message(client, userdata, message):
    data = str(message.payload.decode("utf-8"))
    print("received message =", data)

broker = "broker.emqx.io"

client = paho.Client("client-isu-114")

print("Connecting to broker", broker)
client.connect(broker)
client.subscribe("house/dmit")
client.loop_start()
client.on_message = on_message

print("Publishing")

while True:
    state = input()
    print(f"state is {state}, help")
    client.publish("house/stat", state)

    while True:
        if client.is_connected():
            break
        time.sleep(0.1)

    time.sleep(random.randint(4, 10))