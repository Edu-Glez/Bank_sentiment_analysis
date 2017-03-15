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

tweet1='Estoy muy triste'
prob1=classifier.prob_classify(extract_features(tweet1.split()))
tweet2=':('
prob2=classifier.prob_classify(extract_features(tweet2.split()))
dist1=prob1.samples()
dist2=prob2.samples()
print(dist1)
print(dist2)

print(prob1.prob("positive"))


