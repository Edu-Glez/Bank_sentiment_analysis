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
dates=[{}]
texts=[{}]
user_id=[{}]
#print(place_id) 
for tweet in tweepy.Cursor(api.search, q="#Bancomer", lang="es", since="2017-03-07", until="2017-03-09").items():
	dates.append({'dates':tweet.created_at})
	texts.append({'texts':tweet.text})
	user_id.append({'user_id':tweet.user.id})
dates_df=pd.DataFrame(dates)
texts_df=pd.DataFrame(texts)
user_id_df=pd.DataFrame(user_id)

table=[dates_df, texts_df, user_id_df]
#print(table)
final_result=pd.concat(table, axis=1)
final_result=pd.DataFrame.dropna(final_result)

print(final_result)

final_json=final_result.to_json("test.JSON")
#	if tweet.in_reply_to_user_id is not None:
#		with open('python.json', 'a') as f:
#			f.write(json.dumps(tweet.in_reply_to_user_id))
