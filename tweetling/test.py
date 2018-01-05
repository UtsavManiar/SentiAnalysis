import pickle
import os
import re
import csv
import pprint
#from preprocess_tweets import processTweet
import nltk.classify

#start process_tweet
def processTweet(tweet):
    # process the tweets
    #Convert to lower case
    tweet = tweet.lower()
    #Convert www.* or https?://* to URL
    tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))','URL',tweet)
    #Convert @username to AT_USER
    tweet = re.sub('@[^\s]+','AT_USER',tweet)    
    #Remove additional white spaces
    tweet = re.sub('[\s]+', ' ', tweet)
    #Replace #word with word
    tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
    #trim
    tweet = tweet.strip('\'"')
    return tweet
#end 

#initialize stopWords
stopWords = []

#start replaceTwoOrMore
def replaceTwoOrMore(s):
    #look for 2 or more repetitions of character and replace with the character itself
    pattern = re.compile(r"(.)\1{1,}", re.DOTALL)
    return pattern.sub(r"\1\1", s)
#end

#start getStopWordList
def getStopWordList(stopWordListFileName):
    #read the stopwords file and build a list
    stopWords = []
    stopWords.append('AT_USER')
    stopWords.append('URL')

    fp = open(stopWordListFileName, 'r')
    line = fp.readline()
    while line:
        word = line.strip()
        stopWords.append(word)
        line = fp.readline()
    fp.close()
    return stopWords
#end

#start getfeatureVector
def getFeatureVector(tweet, stopWords):
    featureVector = []  
    words = tweet.split()
    for w in words:
        #replace two or more with two occurrences 
        w = replaceTwoOrMore(w) 
        #strip punctuation
        w = w.strip('\'"?,.')
        #check if it consists of only words
        val = re.search(r"^[a-zA-Z][a-zA-Z0-9]*[a-zA-Z]+[a-zA-Z0-9]*$", w)
        #ignore if it is a stopWord
        if(w in stopWords or val is None):
            continue
        else:
            featureVector.append(w.lower())
    return featureVector    
#end

#start extract_features
def extract_features(tweet):
    tweet_words = set(tweet)
    features = {}
    for word in featureList:
        features['contains(%s)' % word] = (word in tweet_words)
    return features
#end

module_dir1 = os.path.dirname(__file__)  # get current directory
file_path1 = os.path.join(module_dir1, 'full_training_dataset.csv')

module_dir = os.path.dirname(__file__)  # get current directory
file_path = os.path.join(module_dir, 'stopwords.txt')
#Read the tweets one by one and process it
inpTweets = csv.reader(open(file_path1, encoding="Latin-1"), delimiter=',', quotechar='"', escapechar='\\')
stopWords = getStopWordList(file_path)
count = 0;
featureList = []
tweets = []
for row in inpTweets:
    sentiment = row[0]
    tweet = row[1]
    processedTweet = processTweet(tweet)
    featureVector = getFeatureVector(processedTweet, stopWords)
    featureList.extend(featureVector)
    tweets.append((featureVector, sentiment));
#end loop

# Remove featureList duplicates
featureList = list(set(featureList))

# Extract feature vector for all tweets in one shote
training_set = nltk.classify.util.apply_features(extract_features, tweets)
module_dir = os.path.dirname(__file__)  # get current directory
file_path = os.path.join(module_dir, file_path)
module_dir3 = os.path.dirname(__file__)  # get current directory
file_path3 = os.path.join(module_dir3, "naivebayes.pickle")
loaded_model = pickle.load(open(file_path3, 'rb'))

"""
test = '"PJ_King","Loves twitter"'
    #test2 = "Morning everyone! In serious need of some decent coffee.. why isn't the catering open yet at 08.30?"
print ("------------Positive------------")
print (loaded_model.classify(extract_features(getFeatureVector(test,file_path))))
	
"""