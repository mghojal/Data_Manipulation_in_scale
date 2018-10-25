import sys
import json

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    # Read sentiment and create dic from it
    scores = {} 
    for line in sent_file:
      term, score  = line.split("\t")  
      scores[term] = int(score)  
    sent_file.close()

    # read tweet_file
    tweet_data = []
    for line in tweet_file:
        response = json.loads(line)
        if "text" in response.keys():
            tweet_data.append(response["text"])

    # encode the tweet, delete unneccessery characters, lower the case for each word and calculate the score
    for tweet in tweet_data:
        sum = 0
        encoded_tweet = tweet.encode('utf-8')
        words = encoded_tweet.split()

	for word in words:
            word = word.rstrip('?:!.,;"!@')
	    word = word.lower()
	    if word in scores:
                sum = sum + scores[word]

        print '%d' % sum

if __name__ == '__main__':
    main()
