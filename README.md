# MQTT-Python-Remote
Service to remote control linux devices over MQTT.

### Install

- `pip install paho-mqtt`
- Copy `mqtt_agent.py` to `/opt/mqtt_agent/mqtt_agent.py`
- Copy `mqtt_agent.service` to `/etc/systemd/system/mqtt_agent.service`
- Set your `User` and `Group` in `mqtt_agent.service`
- `sudo systemctl daemon-reload`
- `sudo systemctl enable mqtt_agent`
- `sudo systemctl start mqtt_agent`
- Optional: for media keys install `xdotool`

### Change MQTT commands

MQTT Commands are defined in `mqtt_agent.py`:

```
actions = {
    # (device, state) : command
    # mqtt should look like:
    # msg.topic     = TOPIC/device
    # msg.payload   = state


    # hardware
    ("monitor", "on") : "xrandr lorem ipsum",
    ("monitor", "off") : "xrandr lorem ipsum",
    ("laptop", "off") : "shutdown now",
    
    # keys
    ("media", "pause") : "xdotool key XF86AudioPlay",
    ("media", "next") : "xdotool key XF86AudioNext",
    ("media", "last") : "xdotool key XF86AudioPrev",
    ("media", "mute") : "xdotool key XF86AudioMute",
    ("media", "lower") : "xdotool key XF86AudioLowerVolume",
    ("media", "raise") : "xdotool key XF86AudioRaiseVolume",
}
```

### Node-RED integration

Just add a function, set payload and topic and direct everything to your mqtt node:

![nodered integration](https://github.com/schneebonus/MQTT-Python-Remote/blob/main/nodered_integration.png?raw=true)

![nodered_alexa integration](https://github.com/schneebonus/MQTT-Python-Remote/blob/main/nodered_alexa_integration.png?raw=true)

### Credits

- https://smarthome-blogger.de/blog/tutorial/python-mqtt-tutorial/#mqtt-library
- https://www.digitalocean.com/community/tutorials/how-to-use-systemctl-to-manage-systemd-services-and-units
