import sys
import json
import operator
from operator import itemgetter

# read tweet_file
def readTweetFile (tweet_file):
    tweet_file = open(sys.argv[1])
    tweet_data = []
    for line in tweet_file:
        tweet_data.append(json.loads(line))
    return tweet_data

#Extract hash tags
def extract_htags(tweets):
	htags = []
	for tweet in tweets:
		#Ensure that there is an entities element to extract.
		if "entities" in tweet.keys() and "hashtags" in tweet["entities"]:
			for htag in tweet["entities"]["hashtags"]:
				unicode_tag = htag["text"].encode('utf-8')
				htags.append(unicode_tag)
	return htags

#Count top 10 hash tags
def top_ten(htags):
	freq = []
	for htag in htags:
		tup = [htag,htags.count(htag)]
		#print tup
		if tup not in freq :
		    freq.append(tup)
	freq_sorted = sorted(freq, key=itemgetter(1), reverse=True)
	
	for i in range(0,10):
		print freq_sorted[i][0] + " " + str(float(freq_sorted[i][1]))

def main():
    freq = []
    tweets = readTweetFile(sys.argv[1])
    htags = extract_htags(tweets)
    top_ten(htags)

if __name__ == '__main__':
	main()
