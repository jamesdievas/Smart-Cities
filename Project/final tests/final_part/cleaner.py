#Nome: Jemis Dievas José Manhiça

    #---------------Code Description--------------------
    #Downloads the tweets by location and keywords, and get only the tweet 'text" and "id".
    #---------------------------------------------------

#import thongs from a tweepy libary
#this is for live tweets based on location & hastags
import tweepy
import time
from tweepy.streaming import StreamListener
#this is for autentications based on twitter Keys that we saved, associeted to twitter app created on twitter API
from tweepy import OAuthHandler
from tweepy import Stream 
#import the credentials that we saved,(has to be in the same folder as this file 
import credentials

class TwitterStreamer():
    
    """
    class  for streaming & processing live tweets.
    """
    def stream_tweets(self,fetched_tweets_filename, hash_tag_list):
        #this handles twitter authentications & connection to thw twitter streaming API.
        
        listener = StdOutListener(fetched_tweets_filename)

        #autenticate using the keys we saved in other file
        auth =OAuthHandler(credentials.CONSUMER_KEY, credentials.CONSUMER_SECRET)
        auth.set_access_token(credentials.ACCESS_TOKEN,credentials.ACCESS_TOKEN_SECRET)

    
class StdOutListener(StreamListener):
    """ A listener handles tweets are the received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    
    def on_data(self, data):
        try:
            ##print(data)
            texto =data.split('{"id":')[1].split(',"')[0]+'     '+data.split(',"text":"')[1].split('"')[0]+'\n'
            print(texto)
            saveFile = open('extdData.txt', 'a')
            #saveFile.write(complet)
            saveFile.write(texto)
            saveFile.write('\n')
            saveFile.close()
            time.sleep(5)
            return True
        except BaseException:
            print ('failed ondata,')
            time.sleep(5)

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(credentials.CONSUMER_KEY,credentials.CONSUMER_SECRET)
    auth.set_access_token(credentials.ACCESS_TOKEN, credentials.ACCESS_TOKEN_SECRET)
    #ASK FOR KEYWORD TO COLLECT DATA
    #user_keyword=input("What keyword do you want to mine?")
    stream = Stream(auth, l)
    # usando coordenadas de uma região maior de São Paulo, incluindo a região de  CAMPINAS/BRASIL!
    tweets = stream.filter(locations=[-47.736915,-23.227718,-46.738258,-22.640884], track=["CPI", "covid-19", "educação"])
  
