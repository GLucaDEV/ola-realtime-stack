# ola-realtime-stack

Preface: The shown configuration was only deployed inside a VPN in a university. Therefore, this
stack may be not secure enough for deploying it into the real web. Furthermore, the specific
configuration is dependend on Jira, which is not included in this stack. If aimed to use it
with Jira, the docker networks have to be included in the Jira configuration, if it is deployed
via Docker. If not, at least the webhook receiver is required to be reachable in the web.

## Kafka
This section further explains how to configure the Kafka part of the stack, including the webhook receiver.
It is also helpful to overlook the explanation in kafka/kafka_readme.md as it states some parts a bit deeper.

	* create two docker networks
		* docker network create kafka_jira_webhook
		* docker network create etl-webhook-network
	* navigate in kafka dir
	* generate ssl config
		* change line 15-20 in ssl/kafka-generate-ssl.sh to actual values
		* bash ssl/kafka-generate-ssl.sh
	* change values in config/kafka_server_jaas.conf  to actual values (see: https://docs.confluent.io/platform/current/kafka/authentication_sasl/index.html)
	* change environment variable KAFKA_ADVERTISED_LISTENERS, more specifically, everything after SASL_PLAINTEXT:// to an actual server address, if it is not supposed to run local only
	* docker-compose up -d in kafka dir

## Apache Hop

    * navigate in hop dir
	* change environment variables, more specifically, usernames and password to actual secure values
	* start the stack with docker-compose up -d
	* change the pipelines as desired, with opening them up in the hop client. The pipelines can be found in hop/volumes/hop-data/projects/project
	* It is necessary to configure hop beforehand, e.g. add necessary database connections. For executing the pipelines on the remote server, see: https://hop.apache.org/manual/1.0.0/pipeline/pipeline-run-configurations/native-remote-pipeline-engine.html

## Metabase

	* navigate to metabase dir
	* change environment variables, more specifically, usernames and password to actual secure values
	* start up metabase and its database with docker-compose up -d
	* visit the metabase web frontend and start with the first steps
