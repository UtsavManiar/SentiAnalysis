import pickle
import nltk.classify
from feature_extractor import *

# Train the classifier
NBClassifier = nltk.NaiveBayesClassifier.train(training_set)
save_classifier = open("naivebayes.pickle","wb")
pickle.dump(NBClassifier, save_classifier)
save_classifier.close()

# Test the classifier
testTweet = 'Congrats @ravikiranj, i heard you wrote a new tech post on sentiment analysis'
processedTestTweet = processTweet(testTweet)
print (NBClassifier.classify(extract_features(getFeatureVector(processedTestTweet, stopWords))))