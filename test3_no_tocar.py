import pickle
import pandas as pd
import numpy as np
import nltk

a=pd.read_table('Dict.txt')

def get_words_in_tweets(tweets):
	all_words = []
	for (words, sentiment) in tweets:
		all_words.extend(words)
	return all_words

def get_word_features(wordlist):
	wordlist = nltk.FreqDist(wordlist)
	word_features = wordlist.keys()
	return word_features

def extract_features(document):
	document_words = set(document)
	features = {}
	for word in word_features:
		features['contains(%s)' % word] = (word in document_words)
	return features

classifier = nltk.NaiveBayesClassifier.train(a)



#with open('objs.pickle','wb') as f:
#	pickle.dump([classifier, word_features],f)


