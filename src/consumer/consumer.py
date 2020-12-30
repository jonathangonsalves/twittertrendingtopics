import kafka
from json import loads


class Consumer():
    def __init__(self):
        print("Initializating!")


    def insert_into_postgres(self):
        consumer = kafka.KafkaConsumer(
            'teste',
            bootstrap_servers='localhost:9092',
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            group_id='test_group',
            value_deserializer=lambda x: loads(x.decode('utf-8'))
        )

        for message in consumer:
            print(message)

