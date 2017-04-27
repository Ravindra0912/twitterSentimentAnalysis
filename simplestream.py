import password
import json
import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream


class Listener(StreamListener):
    def __init__(self,number_of_tweets):
        self.number = number_of_tweets
        self.counter=0
    def on_data(self, raw_data):
        j = json.load(raw_data)
        while self.counter < self.number:
            print(j["text"])
            self.counter= self.counter + 1
            return True
        else:
            return False

auth = OAuthHandler(password.consumer_key , password.consumer_secret)
auth.set_access_token(password.access_token,password.access_token_secret)
twitterStream = Stream(auth,Listener(5))
twitterStream.filter(track=["liverpool"])