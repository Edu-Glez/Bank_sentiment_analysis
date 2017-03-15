import pickle
import pandas as pd
import numpy as np
import nltk

a=pd.read_table('tweets_pos_clean.txt')
b=pd.read_table('tweets_neg_clean.txt')


aux1=[]
aux2=[]
auxiliar1=[]
auxiliar2=[]
for element in a['Text']:
        for w in element.split():
                if (w==':)' or len(w)>3):
                        auxiliar1.append(w)
        aux1.append((auxiliar1,'positive'))
        auxiliar1=[]

for element in b['text']:
        for w in element.split():
                if (w==':(' or len(w)>3):
                        auxiliar2.append(w)
        aux2.append((auxiliar2,'negative'))
        auxiliar2=[]

aux1=aux1[11000:11100]
aux2=aux2[21000:21100]

table_set=aux1+aux2

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


with open('objs.pickle', "rb") as f:
	classifier, word_features=pickle.load(f)

def extract_features(document):
	document_words = set(document)
	features = {}
	for word in word_features:
		features['contains(%s)' % word] = (word in document_words)
	return features

tweet1=':)'
print(classifier.classify(extract_features(tweet1.split())))
tweet2=':('
print(classifier.classify(extract_features(tweet2.split())))

test_set = nltk.classify.apply_features(extract_features, table_set)

print(nltk.classify.accuracy(classifier,test_set))
