import json
import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
import pandas as pd
import pickle
import sys

arg=sys.argv
print(sys.argv)


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
datos_tweets.setdefault('id',{})
datos_tweets['id'].setdefault('date',[])
datos_tweets['id'].setdefault('texts',[])
datos_tweets['id'].setdefault('user_id',[])
datos_tweets['id'].setdefault('retweet_count',[])


#print(place_id) 
for tweet in tweepy.Cursor(api.search, q=arg[1], lang="es", since=arg[2], until=arg[3]).items():
	if not hasattr(tweet,'retweeted_status'):	
		datos_tweets['id']['date'].append(tweet.created_at.isoformat())
		datos_tweets['id']['texts'].append(tweet.text)
		datos_tweets['id']['user_id'].append(tweet.user.id)
		datos_tweets['id']['retweet_count'].append(tweet.retweet_count)


with open(arg[1]+'_'+arg[2]+'.json', 'w') as fp:
    json.dump(datos_tweets, fp)

print(pd.DataFrame(datos_tweets))
