import tweepy
from tweepy import OAuthHandler

consumer_key = '****'
consumer_secret = '****'
access_token = '****' 
access_secret = '****' 

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

#reading my timeline
for status in tweepy.Cursor(api.home_timeline).items(10):
    print (status.text)

#Want details of all these tweets?
def process_or_store(tweet):
    print(json.dumps(tweet))
    
for status in tweepy.Cursor(api.home_timeline).items(10):
    process_or_store(status._json)

#list of your followers
for friend in tweepy.Cursor(api.friends).items():
    process_or_store(friend._json)


#apple
from tweepy import Stream
from tweepy.streaming import StreamListener
 
class MyListener(StreamListener):
 
    def on_data(self, data):
        try:
            with open('python.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
 
    def on_error(self, status):
        print(status)
        return True
 
twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['#apple'])


