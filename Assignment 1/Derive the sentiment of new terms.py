import sys
import json

#Read sentiment and create dic from it
def dictFromSentFile(sent_file):
    scores = {}
    for line in sent_file:
      term, score  = line.split("\t")
      scores[term] = int(score)
    sent_file.close()
    return scores

# read tweet_file
def readTweetFile (tweet_file):
    tweet_data = []
    for line in tweet_file:
        response = json.loads(line)
        if "text" in response.keys():
	   tweet_data.append(response["text"])
	    
    return tweet_data

# Derive sentiment from each tweet by summing up sentiments of individual words
def tweetSentiment (tweet_data, scores):
    sentiments = []
    for tweet in tweet_data:
        sum = 0.0
        encoded_tweet = tweet.encode('utf-8')
        words = encoded_tweet.split()
	for word in words:
            word = word.rstrip('?:!.,;"!@')
	    word = word.lower()
	    if word in scores:
                sum = sum + scores[word]
	sentiments.append(sum)
    return sentiments

# derive terms of sentiments
def termSentiment (tweet_data, scores, sentiments):
	index = 0
	repeatance = {}
	for tweet in tweet_data:
		words = tweet.encode('utf-8').split()
		for word in words:
		    repeatance [word] = 0
		for word in words:
			repeatance[word] = repeatance[word] + 1
			if word not in scores:
				scores[word] = sentiments[index]
			else:
				scores[word] = (scores[word] + sentiments[index]) / repeatance[word]  # average
			print word + " %.3f" %scores[word]
		index = index + 1
	return scores

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = dictFromSentFile(sent_file)
    tweet_data = readTweetFile(tweet_file)
    tweet_sentiments = tweetSentiment(tweet_data, scores)
    termSentiment(tweet_data, scores, tweet_sentiments)

if __name__ == '__main__':
    main()
