import paho.mqtt.client as mqtt
def on_message(client, userdata, msg):
    print(f"📲 Received Alert: {msg.payload.decode()}")
client = mqtt.Client()
client.connect("test.mosquitto.org", 1883, 60)
client.subscribe("home/alert")
client.on_message = on_message

client.loop_forever()
