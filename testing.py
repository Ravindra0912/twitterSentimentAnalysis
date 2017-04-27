import password
import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import StreamListener
import json

class Listener(StreamListener):

    def on_data(self, raw_data):
        j = json.loads(raw_data)

        print(j["text"])
        print("retweets = "+ str(j["retweet_count"]))
        print("retweeted status = " + str(j["retweeted"]))

auth = OAuthHandler(password.consumer_key , password.consumer_secret)
auth.set_access_token(password.access_token,password.access_token_secret)
twitterStream = Stream(auth,Listener())
a2 = tweepy.API
twitterStream.filter(track=["Liverpool"])