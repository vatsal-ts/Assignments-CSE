import ssl
from paho import mqtt
import paho.mqtt.client as paho
import paho.mqtt.publish as publish
import json
import os
import sys

# Set up the MQTT broker connection parameters
sys.path.append('D:/btp/BTP_MQTT/HiveMQCloud')

with open('./HiveMQCloud/hivemq_creds/vatsal.json', 'r') as config_file:
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

# Create an SSL context for secure connection with HiveMQ Cloud
sslSettings = ssl.SSLContext(mqtt.client.ssl.PROTOCOL_TLS)

# Connect to the MQTT broker
client = paho.Client()
client.username_pw_set(username, password)
client.tls_set_context(sslSettings)
client.connect(hostname, port)

while True:
    # Take user input from the terminal
    message = input("Enter a message to send (or 'exit' to quit): ")

    # Check if the user wants to exit
    if message.lower() == 'exit':
        break

    # Publish the message to the MQTT topic
    topic = "paho/test/multiple"
    client.publish(topic, message)

# Disconnect from the MQTT broker
client.disconnect()

'''
# Connect to the MQTT broker
client = paho.Client()
client.username_pw_set(username, password)
client.connect(hostname, port)

while True:
    # Take user input from the terminal
    message = input("Enter a message to send (or 'exit' to quit): ")

    # Check if the user wants to exit
    if message.lower() == 'exit':
        break

    # Publish the message to the MQTT topic
    topic = "paho/test/multiple"
    client.publish(topic, message)

# Disconnect from the MQTT broker
client.disconnect()
'''