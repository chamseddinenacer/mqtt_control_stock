
import paho.mqtt.client as mqtt
import time
 
client = mqtt.Client()
mqtt_running = False

def start_mqtt():
    global mqtt_running
    if not mqtt_running:
        client.connect("test.mosquitto.org", 1883)
        print("connect")
        client.loop_start()
        mqtt_running = True

def stop_mqtt():
    global mqtt_running
    if mqtt_running:
        client.loop_stop()
        client.disconnect()
        print("stop")
        mqtt_running = False

def is_mqtt_running():
    return mqtt_running
