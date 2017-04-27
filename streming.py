import password
import json
import tweepy
#import project
from tweepy import Stream
from tweepy import OAuthHandler
from  tweepy.streaming import StreamListener
from textblob import TextBlob

langs = {'ar': 'Arabic', 'bg': 'Bulgarian', 'ca': 'Catalan', 'cs': 'Czech', 'da': 'Danish', 'de': 'German', 'el': 'Greek', 'en': 'English', 'es': 'Spanish', 'et': 'Estonian',
         'fa': 'Persian', 'fi': 'Finnish', 'fr': 'French', 'hi': 'Hindi', 'hr': 'Croatian', 'hu': 'Hungarian', 'id': 'Indonesian', 'is': 'Icelandic', 'it': 'Italian', 'iw': 'Hebrew',
         'ja': 'Japanese', 'ko': 'Korean', 'lt': 'Lithuanian', 'lv': 'Latvian', 'ms': 'Malay', 'nl': 'Dutch', 'no': 'Norwegian', 'pl': 'Polish', 'pt': 'Portuguese', 'ro': 'Romanian',
         'ru': 'Russian', 'sk': 'Slovak', 'sl': 'Slovenian', 'sr': 'Serbian', 'sv': 'Swedish', 'th': 'Thai', 'tl': 'Filipino', 'tr': 'Turkish', 'uk': 'Ukrainian', 'ur': 'Urdu',
         'vi': 'Vietnamese', 'zh_CN': 'Chinese (simplified)', 'zh_TW': 'Chinese (traditional)'}

class Listener(StreamListener):
    def __init__(self,number_of_tweets_to_fetch,retweet_count = 1000):
        self.counter = 0
        self.numberOfTweets = number_of_tweets_to_fetch
        self.languages =  []
        self.i = 0
        self.retweet_count = retweet_count
    def on_data(self, raw_data):
      #  print(raw_data)
      #  retweet = j["retweeted_status"]["retweet_count"]
       # if()
        while self.counter != self.numberOfTweets and self.i < self.numberOfTweets:
            j = json.loads(raw_data)
            self.languages.append(langs[j["lang"]])
            #print(self.languages)

          #  retweet_status = j["retweeted"]
            rc = j["retweet_count"]
            tweet  = (j["text"])
            var = TextBlob(tweet)
            print(tweet)
            print("language of tweet is "+ self.languages[self.i])
            print("retweets = "+ str(rc))
            print("polarity = "+ str(var.sentiment.polarity))
            self.i = self.i+1
            self.counter = self.counter+1
            return True
        else:
            return False
    def on_error(self, status_code):
        print(status_code)


auth = OAuthHandler(password.consumer_key , password.consumer_secret)
auth.set_access_token(password.access_token,password.access_token_secret)
twitterStream = Stream(auth,Listener(1000))
twitterStream.filter(track=["The boss baby"])

a2 = tweepy.API(auth)