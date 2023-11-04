# Import necessary libraries
import ssl
import paho.mqtt.client as mqtt
import paho.mqtt.subscribe as subscribe

# Set up MQTT broker connection parameters
from creds.vatsal import hostname, username, password  # Import credentials from credentials.py
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
