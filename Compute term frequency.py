import sys
import json

# read tweet_file
def readTweetFile (tweet_file):
    tweet_data = []
    for line in tweet_file:
        response = json.loads(line)
        if "text" in response.keys():
            tweet_data.append(response["text"])
    return tweet_data

def main():
    tweet_file = open(sys.argv[1])
    tweets = readTweetFile(tweet_file)
    term_list = []
    total_list = {}#dict of term and corresponding the number of occurance that term/ number of total terms
    for tweet in tweets:
	words = tweet.encode('utf-8').split()
	for word in words:
	    word = word.rstrip('?:!.,;"!@')
	    word = word.lower()
	    term_list.append(word)

    for word in term_list:
	if word in total_list:
		total_list[word] = total_list[word] + 1	
	else:
		total_list[word] = 1		   
    total_number = len(total_list)

    for word in total_list:
        total_list[word] = "%.3f" %(float(total_list[word])/total_number)
        print word + " " + total_list[word]

if __name__ == '__main__':
    main()
