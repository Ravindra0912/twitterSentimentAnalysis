import requests
from bs4 import BeautifulSoup
from queue import *
import tweepy
import password
import json
from tweepy.streaming import StreamListener
from tweepy import streaming
from tweepy.streaming import Stream
from tweepy import OAuthHandler
from textblob import TextBlob


consumer_key = 'B1CbvEZAbktdui4BerzGlSH0h'
consumer_secret = 'vhZci8ZHwdefrxLWoiaruIXQ2mP0CLfaqjGpcTH9pF4oVea9EY'
access_token = '771565398458179586-eMxFCEA9o1ZAyb5FxaO5StShdhSPUkS'
access_token_secret = 'ccyHiv8WCP5RQqs9ywvjDOdqlkofbjvZmZbAg1sSeib5U'


auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_token_secret)
a2 = tweepy.API(auth)

print("GLOBAL TRENDS OR MOVIES")
query = input()

if(query == "GLOBAL TRENDS"):
    trends = a2.trends_place(1)
    for trend in trends[0]["trends"]:
        print(trend["name"])


langs = {'ar': 'Arabic', 'bg': 'Bulgarian', 'ca': 'Catalan', 'cs': 'Czech', 'da': 'Danish', 'de': 'German', 'el': 'Greek', 'en': 'English', 'es': 'Spanish', 'et': 'Estonian',
         'fa': 'Persian', 'fi': 'Finnish', 'fr': 'French', 'hi': 'Hindi', 'hr': 'Croatian', 'hu': 'Hungarian', 'id': 'Indonesian', 'is': 'Icelandic', 'it': 'Italian', 'iw': 'Hebrew',
         'ja': 'Japanese', 'ko': 'Korean', 'lt': 'Lithuanian', 'lv': 'Latvian', 'ms': 'Malay', 'nl': 'Dutch', 'no': 'Norwegian', 'pl': 'Polish', 'pt': 'Portuguese', 'ro': 'Romanian',
         'ru': 'Russian', 'sk': 'Slovak', 'sl': 'Slovenian', 'sr': 'Serbian', 'sv': 'Swedish', 'th': 'Thai', 'tl': 'Filipino', 'tr': 'Turkish', 'uk': 'Ukrainian', 'ur': 'Urdu',
         'vi': 'Vietnamese', 'zh_CN': 'Chinese (simplified)', 'zh_TW': 'Chinese (traditional)'}



q = Queue()


class Spider:
    def c_spider(self):
        url = 'http://www.imdb.com/movies-in-theaters/?ref_=nv_mv_inth_1'
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text,"lxml")
        none = 0
        movies = []
        for link in soup.findAll('h4',{'itemprop':'name'}):
            title= link.get('title')
            none += 1
            title=link.string
            if(none > 8 and none < 15):
                if(title != "None"):
                    print(title)
                    q.put(title)

    # print(none)
        return q.get(0)
s = Spider()

if query == "MOVIES":
    s.c_spider()

print("enter Search term")
search_term = input()

fn = open("negative.txt", "w+")
fp = open("positive.txt", "w+")


class Listener(StreamListener):

    def __init__(self, num):

        self.number = num
        self.counter = 0
        self.n = 0
        self.p = 0

    def on_data(self, raw_data):

        while self.counter < self.number:
            j = json.loads(raw_data)
            tweet = j["text"]
            var1 = TextBlob(tweet)

            #if var1.sentiment.polarity != 0 or var1.subjectivity != 0:
            print(tweet)
            var = TextBlob(tweet)

            if var.sentiment.polarity > 0:
                self.p = self.p+1
                fp.write(tweet)

            else:
                self.n = self.n+1
                fn.write(tweet)

            print("Polarity = " + str(var.sentiment.polarity))
            print("subjectivity = "+str(var.subjectivity))
            self.counter +=1
            return True

        else:
            return False


l1 = Listener(20)
twitterStream = Stream(auth,Listener(20))
twitterStream.filter(track=[search_term], languages=["en"])


class Search(Listener):

    def __init__(self,num):
        self.num = num

    def search_tweets(self):

        search_results = tweepy.Cursor(a2.search, q=search_term).items(self.num)

        for result in search_results:
            var = TextBlob(result.text)
            print(result.text)
            a = var.sentiment.polarity
            b = var.subjectivity

            if var.sentiment.polarity < 0:
                l1.n = l1.n+1
                fn.write(result.text)

            else:
                l1.p = l1.p + 1
                fp.write(result.text)

            print("subjectivity = " + str(b))
            print("polarity = " + str(a))
            print("retweets = " + str(result.retweet_count))


num_of_tweets = 20
src = Search(num_of_tweets)
src.search_tweets()
ppercent = (l1.p/20)*100
npercent =(l1.n/20)*100
print("like percent = " + str(ppercent))
print("dislike percent = " + str(npercent))

print("POSITIVE TWEETS :")
print(fp.read())

print("NEGATIVE TWEETS")
print(fn.read())



