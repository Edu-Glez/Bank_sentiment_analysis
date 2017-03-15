import pickle
import pandas as pd
import numpy as np
import nltk
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
