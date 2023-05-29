## What is the purpose of this stack?

This stack is to receive Jira worklog events as a webhook
and dispatch them to the outside world in a Kafka node, which acts as a
outside world.

## What is included?

The following things are included in this repository:

- "webhook" folder.
Contains the Dockerfile, the requirements and the Python scripts for the functionality of the endpoint.

- docker-compose.yml
    - Zookeeper: Takes over the consensus for Kafka.
    - Kafka: mediator for the endpoint to the outside world.
    - Endpoint: Receives webhooks from Jira worklog events and passes them to Kafka

## How to start

in root dir run 'docker-compose up -d'.
Then build the endpoint and start the other services.
After start use the command 'docker ps' to make sure that all three 
three services are started.

## Configure Webhook

In Jira, click on webhook in the settings, configure new webhook.
The address of the endpoint is: "webhook_receiver:5000/webhook" (inside Docker network).

## What else needs to be customized?

- Since Kafka should be reachable in the VPN, the left port at 9102:9102
  has to be changed to the port that is available.

- So that Kafka can also be addressed within the VPN, must:
    - The address localhost:9093 in the docker-compose.yml under the Environment Variables of Kafka, more precisely.
      "KAFKA_CFG_ADVERTISED_LISTENERS=PLAINTEXT://kafka:9092,SASL_PLAINTEXT://<localhost:9102>"
      must be replaced by the address that makes Kafka accessible to the outside world and the port.

## How to authenticate with a client?

- Via Python Kafka Lib:
  - In the producer/consumer add the following parameters:
    - bootstrap_servers=['kafka:9102'] # has to be changed to an actual server address
    - security_protocol='SASL_PLAINTEXT'
    - sasl_plain_username=<is in config/kafka_server_jaas.conf under username>
    - sasl_plain_password=<is in config/kafka_server_jaas.conf under password>
    - sasl_mechanism='PLAIN'

- About Hop
  - Go to the options at the consumer/producer and add the following parameters
    - sasl.jaas.config = <content of config/kafka_server_jaas.conf>, important to take only the content between the curly braces
    - security.protocol = SASL_PLAINTEXT
    - sasl.mechanism = PLAIN