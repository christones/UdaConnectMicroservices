from kafka import KafkaConsumer


TOPIC_NAME = 'Persons'

consumer = KafkaConsumer(TOPIC_NAME)
for message in consumer:
    print (message)
