from kafka import KafkaProducer


TOPIC_NAME = 'Persons'
KAFKA_SERVER = 'localhost:9092'

producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)

Longitude= '77.25412587' 
Latitude= '14.2354125'

producer.send(TOPIC_NAME, 'Location of the person is +'Longitude' and +'Latitude' !!!')
producer.flush()
