# Import necessary libraries
import ssl
import paho.mqtt.client as mqtt
import paho.mqtt.subscribe as subscribe

# Set up MQTT broker connection parameters
hostname = "37d997fa2a7b4a6cbf23470c5d089a86.s2.eu.hivemq.cloud"
port = 8883
username = "pranshu"
password = "BtpVatsalPranshu1"

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
