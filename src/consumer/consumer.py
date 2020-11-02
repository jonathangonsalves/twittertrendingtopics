import kafka
from json import loads
from  psycopg2 import connect



class Consumer():
    def __init__(self):
        self.conn = connect(
                    host="localhost",
                    database="suppliers",
                    user="postgres",
                    password="Ja15082020*")

        self.cur = conn.cursor()



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

