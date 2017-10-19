
import json
from tweepy import OAuthHandler, Stream, API
from tweepy.streaming import StreamListener

consumer_key = 'FMjMEgCw94Hw01ECgKvE2U5Ez'
consumer_secret= '3eW9rMq1ihDE5WSWaD76YlKWl1v1X8BeAEnYbcs7Ewk4j3QpGb'
access_token = '921061893145530369-ol1FRmXnxNasviUeiMjnePCAHpJ2K4F'
access_token_secret = 'Hr9f67ZWpHbHHOp3oDaCVlN9QxGIJxSaHAP2VbZ80BMES'

auth = OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_token_secret)

class PrintListener(StreamListener):
    def on_status(self, status):
        if not status.text[:3] == 'RT ':
            print(status.text)
            print(status.author.screen_name,
                  status.created_at,
                  status.source,
                  '\n')

        def on_error(self, status_code):
            print("Error code: {}".format(status_code))
            return True # keep stream alive

        def on_timeout(self):
            print('Listener timed out!')
            return True # keep stream alive

def print_to_terminal():
    listener = PrintListener()
    stream = Stream(auth, listener)
    languages = ('en',)
    stream.sample(languages=languages)

def pull_down_tweets(screen_name):
    api = API(auth)
    print(api)
    print(screen_name)
    tweets = api.user_timeline(screen_name=screen_name, count=200)
    
    print("Hallo")
    for tweet in tweets:
        print(json.dumps(tweet._json, indent=4))
if __name__ == '__main__':
    # print_to_terminal()
    print(auth)
    pull_down_tweets(auth.username)
