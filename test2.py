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
dates_bancomer=[{}]
texts_bancomer=[{}]
user_id_bancomer=[{}]
#print(place_id) 
for tweet in tweepy.Cursor(api.search, q="#Bancomer", lang="es", since="2017-03-07", until="2017-03-09").items():
	dates_bancomer.append({'dates':tweet.created_at})
	texts_bancomer.append({'texts':tweet.text})
	user_id_bancomer.append({'user_id':tweet.user.id})
dates_bancomer_df=pd.DataFrame(dates_bancomer)
texts_bancomer_df=pd.DataFrame(texts_bancomer)
user_id_bancomer_df=pd.DataFrame(user_id_bancomer)

table_bancomer=[dates_bancomer_df, texts_bancomer_df, user_id_bancomer_df]
#print(table)
final_result_bancomer=pd.concat(table_bancomer, axis=1)
final_result_bancomer=pd.DataFrame.dropna(final_result_bancomer)

print(final_result)

final_json=final_result.to_json("test.JSON")
#	if tweet.in_reply_to_user_id is not None:
#		with open('python.json', 'a') as f:
#			f.write(json.dumps(tweet.in_reply_to_user_id))
