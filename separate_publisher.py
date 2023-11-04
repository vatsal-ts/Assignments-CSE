import ssl
from paho import mqtt
import paho.mqtt.client as paho
import paho.mqtt.publish as publish

# Set up the MQTT broker connection parameters
hostname = "37d997fa2a7b4a6cbf23470c5d089a86.s2.eu.hivemq.cloud"
port = 8883
username = "vatsal"
password = "BtpVatsalPranshu1"

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
import paho.mqtt.client as paho

# Set up the MQTT broker connection parameters
hostname = "37d997fa2a7b4a6cbf23470c5d089a86.s2.eu.hivemq.cloud"
port = 1883  # Default non-TLS MQTT port
username = "vatsal"
password = "BtpVatsalPranshu1"

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