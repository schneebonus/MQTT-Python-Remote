# !/usr/bin/python
# -*- coding: utf-8 -*-

import paho.mqtt.client as mqtt
import os

CLIENT_ID = "x240"        # ToDo
TOPIC = "laptop/x240/+"   # ToDo
BROKER_ADDRESS = ""       # ToDo
PORT = 1883               # ToDo
USER = ""                 # ToDo
PASSWORD = ""             # ToDo

actions = {
    # (device, state) : command

    # hardware
    ("monitor", "on") : "xrandr lorem ipsum",
    ("monitor", "off") : "xrandr lorem ipsum",
    ("laptop", "off") : "shutdown -t now",
}

def on_message(client, userdata, message):
    # parse incoming message
    msg = str(message.payload.decode("utf-8"))
    action = message.topic.split("/")[2]
    # find matching action
    for a in actions:
        if a[0] == action and a[1] == msg:
            # execute matching command
            os.system(actions[a])

def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT Broker: " + BROKER_ADDRESS)
    client.subscribe(TOPIC)

if __name__ == "__main__":
    client = mqtt.Client(client_id=CLIENT_ID)
    client.username_pw_set(USER, PASSWORD)
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(BROKER_ADDRESS, PORT)

    client.loop_forever()
