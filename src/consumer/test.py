import kafka
from json import loads
from  psycopg2 import connect



class Consumer():
    def __init__(self):
        self.conn = connect(
                    host="localhost",
                    database="postgres",
                    user="postgres",
                    password="Ja15082020*")

        self.cur = self.conn.cursor()


    def teste(self):
        values = ('teste', 10, '2020-10-27')
        self.cur.execute(sql, values)
        self.conn.commit()
        count = self.cur.rowcount
        self.cur.close()


    def insert_into_postgres(self):
        sql = """INSERT INTO TWEETS(TOPIC_MESSAGE, NUMBER_OF_TWEETS, DATE) VALUES (%s, %s, %s)"""

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


teste = Consumer()

teste.insert_into_postgres()
