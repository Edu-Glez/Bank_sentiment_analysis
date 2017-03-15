import json
import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
import pandas as pd

consumer_key = 'w87sF4cjjFylzzyCd4mmTVfW3'
consumer_secret = 'QSomS57CVwOZWHoK9Bl2yt2PdBImgxftulZeGSraq4n9vJzGFh'
access_token = '293210492-tjb5kNx8Iupi4Yq4vTlk3vuXCTM3XWqxALnoyIak'
access_secret = 'g6IjmWVWljTp9OjrFBZddiIyzjFC9251S7brov3RHT3hU'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)
#places = api.geo_search(query="MEXICO", granularity="country")
#place_id = places[0].id

datos_tweets={}
datos_tweets.setdefault('date',[])
datos_tweets.setdefault('texts',[])
datos_tweets.setdefault('user_id',[])

#print(place_id) 
for tweet in tweepy.Cursor(api.search, q="#Bancomer", lang="es", since="2017-03-09", until="2017-03-11").items():
	datos_tweets['date'].append(tweet.created_at)
	datos_tweets['texts'].append(tweet.text)
	datos_tweets['user_id'].append(tweet.user.id)


#print(table)
