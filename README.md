In order to run this stack, docker has to be installed, as well as docker compose.
In every directory, run "docker-compose up -d". This starts up the docker containers
associated with the stack. Following prequisites have to be fullfilled in order to deploy the stack:

- For Apache Hop, copy the pipelines out of hop/volumes/hop-data/projects/project to your local Hop instance, and execute them via remote server
- For Kafka, SSL certificates have to be generated, for that, execute kafka/ssl/kafka-generate-ssl.sh, also it is beneficial to change the credentials in the config/kafka_server_jaas.conf
as it contains secrets
- The kafka_jira_webhook docker network is an external network, which is included in a docker-compose file that is not present in this repository. If using this with Jira, add this network
to the compose file. 
- For setup of the webhook flask service, as well as kafka, refer to the kafka/kafka_readme.md
- The ports in the compose files have to be open, if the plan is to reach them in a network. In this example, the ports were reachable inside a university VPN