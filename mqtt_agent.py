# !/usr/bin/python
# -*- coding: utf-8 -*-

import paho.mqtt.client as mqtt
import os

CLIENT_ID = "x240"        # ToDo
TOPIC = "laptop/x240"     # ToDo
BROKER_ADDRESS = ""       # ToDo
PORT = 1883               # ToDo
USER = ""                 # ToDo
PASSWORD = ""             # ToDo

LAST_WILL = "off"
QOS = 1

actions = {
    # (device, state) : command
    # mqtt should look like:
    # msg.topic     = TOPIC/device
    # msg.payload   = state

    # hardware
    ("monitor", "on") : "xrandr --output eDP-1 --mode 1366x768 --pos 3600x312 --rotate normal --output DP-1 --off --output HDMI-1 --off --output DP-2 --off --output HDMI-2 --off --output DP-2-1 --off --output DP-2-2 --mode 1680x1050 --pos 0x0 --rotate normal --output DP-2-3 --primary --mode 1920x1080 --pos 1680x0 --rotate normal",
    ("monitor", "off") : "xrandr --output eDP-1 --off --output DP-1 --off --output HDMI-1 --off --output DP-2 --off --output HDMI-2 --off --output DP-2-1 --off --output DP-2-2 --mode 1680x1050 --pos 0x0 --rotate normal --output DP-2-3 --primary --mode 1920x1080 --pos 1680x0 --rotate normal",
    ("laptop", "off") : "shutdown -t now",
    
    # media keys
    ("media", "pause") : "xdotool key XF86AudioPlay",
    ("media", "next") : "xdotool key XF86AudioNext",
    ("media", "last") : "xdotool key XF86AudioPrev",
    ("media", "mute") : "xdotool key XF86AudioMute",
    ("media", "lower") : "xdotool key XF86AudioLowerVolume",
    ("media", "raise") : "xdotool key XF86AudioRaiseVolume",
    }

def on_message(client, userdata, message):
    # parse incoming message
    msg = str(message.payload.decode("utf-8"))
    action = message.topic.split("/")[2]
    # find matching action
    for a in actions:
        if a[0] == action and a[1] == msg:
            # execute matching command
            os.system("export DISPLAY=:0.0;" + code)

def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT Broker: " + BROKER_ADDRESS)
    client.subscribe(TOPIC + "/#")

if __name__ == "__main__":
    client = mqtt.Client(client_id=CLIENT_ID)
    client.username_pw_set(USER, PASSWORD)

    client.on_connect = on_connect
    client.on_message = on_message

    client.will_set(TOPIC, LAST_WILL, qos=QOS, retain=False)

    client.connect(BROKER_ADDRESS, PORT)

    client.publish(TOPIC, "on", qos=QOS)

    client.loop_forever()
