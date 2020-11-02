import twitter
import requests
import numpy
import tweepy
from kafka import KafkaProducer
from datetime import datetime
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener


consumer_key="Lwp5cwDioiJ1bDqnYi1uxXPD2"
consumer_secret="fJ2zT2wFPgEhAclTIcN7cnDBkc7qpB1lcN2wDlgumNJ07qwkGQ"
access_token_key="1312165577633525760-LmWZsZ0fjkFImlMUbi9UXHo7Gy4g6T"
access_token_secret="JPLH8IZu1j2Df9O394cnKHbUSI4HZGgOxsglueDkBPmO5"




class TwitterAuth():

    @classmethod
    def authenticateTwitter(self):
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token_key, access_token_secret)

        return auth


class TwitterStream():
    def __init__(self):
        self.twitterAuth = TwitterAuth.authenticateTwitter()
        self.producer = KafkaProducer(
            bootstrap_servers='localhost:9092',
            value_serializer = lambda x: dumps(x).encode('utf-8')
        )

    def stream_tweets(self):
        while True:
            listener = Listener()
            stream = Stream(self.twitterAuth, listener)
            stream.filter(follow=['1312165577633525760'])
            #stream.filter(follow=['959791427143299072'])


    def teste(self):
        api = tweepy.API(self.twitterAuth)
        print( api.trends_place(1))



class Listener(StreamListener):
    def  on_data(self, raw_data):

        print(raw_data)
        if (raw_data.find("I have identified") != -1):
            number_of_tweets = text[text.rfind("identified") + 11 : text.find("tweets") - 1]
            mentioning = text[text.rfind("mentioning") + 11 : text.find("that") - 1]
            current_date = datetime.now()

            data = {
                message:  mentioning,
                tweet_number: number_of_tweets,
                cur_date: current_date
            }
            producer.send(topic_name,data)



t = TwitterStream()
t.stream_tweets()
#t.
