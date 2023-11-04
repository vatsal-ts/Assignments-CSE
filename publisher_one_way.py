import ssl
from paho import mqtt
import paho.mqtt.client as paho
import paho.mqtt.publish as publish

# Set up the MQTT broker connection parameters
from creds.vatsal import hostname, username, password  # Import credentials from credentials.py
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