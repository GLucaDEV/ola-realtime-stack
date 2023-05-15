from kafka import KafkaProducer
import json
'''
Parses a string to json format.
'''
# source: https://betterdatascience.com/apache-kafka-in-python-how-to-stream-data-with-producers-and-consumers/
def parseToJSON(message):
    return json.dumps(message).encode('utf-8')
# establishes a connection to the kafka broker
producer = KafkaProducer(
    bootstrap_servers=['kafka:9092'],
    value_serializer=parseToJSON,
    sasl_mechanism='PLAIN'
)
'''
Sends a message with a given topic into the kafka broker.
'''
def sendToQueue(Topic, message):
    producer.send(Topic, message)
    producer.flush()
