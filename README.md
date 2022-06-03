# MQTT-Python-Remote
MQTT service to remote control my linux devices.

### Install

- `pip install paho-mqtt`
- copy `mqtt_agent.py` to `/opt/mqtt_agent/mqtt_agent.py`
- `sudo chmod +x /opt/mqtt_agent/mqtt_agent.py`
- ToDo: install service

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
    ("laptop", "off") : "shutdown -t now",
}
```

### Node-RED integration

Just add a function, set payload and topic and direct everything to your mqtt node:

![nodered integration](https://github.com/schneebonus/MQTT-Python-Remote/blob/main/nodered_integration.png?raw=true)
