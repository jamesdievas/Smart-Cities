# -*- coding: utf-8 -*-

import tweepy
import time
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

class StreamListener(tweepy.StreamListener):
  """tweepy.StreamListener is a class provided by tweepy used to access
  the Twitter Streaming API to collect tweets in real-time.
  """

  def on_connect(self):
    """Called when the connection is made"""
    
    print("You're connected to the streaming server!!")

  def on_error(self, status_code):
    """This is called when an error occurs"""
    
    print('!Error!: ' + repr(status_code))
    return False

  def on_data(self, data):

    #print(data)
    try:
      ##print(data)
      texto =data.split('{"id":')[1].split(',"')[0]+'     '+data.split(',"text":"')[1].split('"')[0]+'\n'
      print(texto)
      saveFile = open('extdData.txt', 'a')
      #saveFile.write(complet)
      saveFile.write(texto)
      saveFile.write('\n')
      saveFile.close()
      time.sleep(3)
      return True
    except BaseException:
      print ('failed ondata,')
      #time.sleep(5)

    return True


if __name__ == "__main__":

  # authorization tokens
  consumer_key = "*******************"
  consumer_secret = "7y********************"
  access_token = "1***************************"
  access_token_secret = "**************************"

  # complete authorization and initialize API endpoint
  auth1 = tweepy.OAuthHandler(consumer_key, consumer_secret)
  auth1.set_access_token(access_token, access_token_secret)

  #https://boundingbox.klokantech.com/ (format -> CSV)
  #location = [-47.736915,-23.227718,-46.738258,-22.640884] #Mais que a Região Metropolitana de Campinas
  
  #location = [-160.161542, 18.776344, -154.641396, 22.878623] #Hawaii
  
  stream_listener = StreamListener(api=tweepy.API(wait_on_rate_limit=True))
  stream = tweepy.Stream(auth=auth1, listener=stream_listener)
  tweets = stream.filter(locations=[-47.736915,-23.227718,-46.738258,-22.640884])
