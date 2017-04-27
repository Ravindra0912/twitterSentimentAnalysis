import password
import json
from tweepy import OAuthHandler
import tweepy
from tweepy import StreamListener
from tweepy import Stream
auth = OAuthHandler(password.consumer_key , password.consumer_secret)
auth.set_access_token(password.access_token,password.access_token_secret)
#a2 = tweepy.API()


class Listener(StreamListener):
    def __init__(self,number_of_tweets):
        self.count = number_of_tweets
        self.counter =0
    def on_data(self, raw_data):
        while self.counter<self.count:
        #search_data = tweepy.Cursor(a1.search, q = 'Liverpool')
            trends = a1.trends_place(1)
            j = json.loads(raw_data)
            print(j["text"])
            print(str(j["retweeted"]))
            print("retweet count = "+ str(j["retweet_count"]))
            self.counter += 1
            print("not found")
            return True
       # j1 = a1.trends_place(1)
       # for data in search_data:
           # print(data.text)


twitterStream = Stream(auth,Listener(5))
a1 = tweepy.API(auth)
twitterStream.filter(track=["car"])