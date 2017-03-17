import json
import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
import pandas as pd
import pickle
import sys

#arg=sys.argv
#print(sys.argv)


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
datos_tweets.setdefault('date',{})
datos_tweets.setdefault('texts',{})
datos_tweets.setdefault('user_id',{})
datos_tweets.setdefault('retweet_count',{})
i=1
#print(place_id) 
for tweet in tweepy.Cursor(api.search, q='IXE', lang="es", since='2017-03-09', until='2017-03-10').items():
	if not hasattr(tweet,'retweeted_status'):
		datos_tweets['date'].update({i:tweet.created_at.isoformat()})
		datos_tweets['texts'].update({i:tweet.text})
		datos_tweets['user_id'].update({i:tweet.user.id})
		datos_tweets['retweet_count'].update({i:tweet.retweet_count})
		i=i+1

df_datos_tweets=pd.DataFrame(datos_tweets)



#with open(arg[1]+'_'+arg[2]+'.json', 'w') as fp:
#    json.dump(datos_tweets, fp)

print(df_datos_tweets.to_json)
