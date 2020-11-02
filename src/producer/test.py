import kafka
from json import dumps
from time import sleep


producer = kafka.KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda x: dumps(x).encode('utf-8'))


for e in range(1000):
    data = {'teste' : e}
    producer.send('teste', value=data)
    sleep(5)
