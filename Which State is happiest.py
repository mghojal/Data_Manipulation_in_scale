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
        tweet_data.append(json.loads(line))
    return tweet_data

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = dictFromSentFile(sent_file)
    tweets = readTweetFile(tweet_file)
    state_dict = {"Alabama":"AL","Alaska":"AK","Arizona":"AZ","Arkansas":"AR","California":"CA","Colorado":"CO","Connecticut":"CT","Delaware":"DE","Florida":"FL","Georgia":"GA","Hawaii":"HI","Idaho":"ID","Illinois":"IL","Indiana":"IN","Iowa":"IA","Kansas":"KS","Kentucky":"KY","Louisiana":"LA","Maine":"ME","Maryland":"MD","Massachusetts":"MA","Michigan":"MI","Minnesota":"MN","Mississippi":"MS","Missouri":"MO","Montana":"MT","Nebraska":"NE","Nevada":"NV","NewHampshire":"NH","NewJersey":"NJ","NewMexico":"NM","NewYork":"NY","NorthCarolina":"NC","NorthDakota":"ND","Ohio":"OH","Oklahoma":"OK","Oregon":"OR","Pennsylvania":"PA","RhodeIsland":"RI","SouthCarolina":"SC","SouthDakota":"SD","Tennessee":"TN","Texas":"TX","Utah":"UT","Vermont":"VT","Virginia":"VA","Washington":"WA","WestVirginia":"WV","Wisconsin":"WI","Wyoming":"WY"}                       
    state_list = {}
    max_score = 0
    happiest_state = ""

    for tweet in range(len(tweets)):
        if 'place' in tweets[tweet].keys() and tweets[tweet]["place"] is not None and tweets[tweet]["place"]["country_code"]=='US' and tweets[tweet]["place"]["full_name"] is not None:
                    tweet_word = tweets[tweet]["text"].encode('utf-8').lower().split()
                    tweet_country = tweets[tweet]["place"]["country_code"]

		    if tweets[tweet]["place"]["full_name"].split(", ")[1] == "USA":
			tweet_state_full_name = tweets[tweet]["place"]["full_name"].split(", ")[0]
			tweet_state = state_dict[tweet_state_full_name]
		    else:
		    	tweet_state = tweets[tweet]["place"]["full_name"].split(", ")[1]  
		    #print tweet_word

		    if len(tweet_state) == 2 and tweet_country == 'US':    
		    	#print tweet_state
                        sent_score = 0
		        for word in tweet_word:
	                    if word in scores.keys():
	                        sent_score = sent_score + float(scores[word])
	                    else:
	                        sent_score = sent_score
			
	                if tweet_state in state_list.keys():
	                    state_list[tweet_state].append(sent_score)
	                else:
	                    state_list[tweet_state] = []
	                    state_list[tweet_state].append(sent_score)
			#print state_list[tweet_state]

    for state in state_list.keys():
	state_score = 0
	state_list_score = state_list[state]
  
	for score in state_list_score:
	    state_score = state_score + float(score)
		
	state_score = state_score/len(state_list[state])
		                      
	if happiest_state == "" or state_score > max_score:
	    max_score = state_score
	    happiest_state = state    

    print happiest_state, max_score

if __name__ == '__main__':
    main()
