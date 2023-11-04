# Import necessary libraries
import ssl
import paho.mqtt.client as mqtt
import paho.mqtt.subscribe as subscribe
import json
import os
import sys

# Load credentials from the JSON configuration file
with open('./HiveMQCloud/hivemq_creds/pranshu.json', 'r') as config_file:
    config = json.load(config_file)
    mqtt_credentials = config.get("mqtt_credentials")

# Check if the credentials are loaded successfully
if not mqtt_credentials:
    print("Error: Unable to load MQTT credentials from the configuration file.")
    exit(1)

# Extract MQTT credentials
hostname = mqtt_credentials["hostname"]
username = mqtt_credentials["username"]
password = mqtt_credentials["password"]

port=8883

# Create an SSL context for a secure connection with HiveMQ Cloud
ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS)

# Callback function to print received MQTT messages
def print_msg(client, userdata, message):
    print(f"{message.topic}: {message.payload}")

# Establish the MQTT connection and subscribe to all topics ('#')
auth = {'username': username, 'password': password}
subscribe.callback(print_msg, "#", hostname=hostname, port=port, auth=auth, tls=ssl_context, protocol=mqtt.MQTTv31)

# Keep the script running to continue receiving messages
while True:
    pass
