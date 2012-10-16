import twitter, argparse, sys, os
import config
import Levenshtein
import re
from cobe.brain import Brain

parser = argparse.ArgumentParser(description="Post ebooks tweets to twitter.")
parser.add_argument('-o', '--stdout', action='store_true', help="Output to stdout instead of posting to twitter.")
parser.add_argument('-t', '--tweet', help="Tweet arbitrary text instead of using the brain.")

args = parser.parse_args()

api = twitter.Api(**config.api)

if args.tweet:
	api.PostUpdate(args.tweet)
else:
	#note: i don't actually know if you have to close + reopen a file to change the mode soooo
	#create a tweet log if we don't have one already
	if os.path.exists(config.our_tweets) == False:
		tweetlog = open(config.our_tweets, "w")
		tweetlog.close
	#open for read and write
	tweetlog = open(config.our_tweets, "r+")
	#put our tweetlog into a list
	twets = [twet.strip() for twet in tweetlog]	
	
	#text file with tweets used to prime the brain (should already exist but let's make sure anyway I guess)
	if os.path.exists(config.brain_tweets) == False:
		primedtxt = open(config.brain_tweets, "w")
		primedtxt.close
	#we only need to read from it so mode is "r"
	primedtxt = open(config.brain_tweets, "r")
	#shove those pieces of shit into a list
	brains = [line.strip() for line in primedtxt]

	#learned tweets
	if os.path.exists(config.learned_tweets) == False:
		learnedtxt = open(config.learned_tweets, "w")
		learnedtxt.close
	#we only need to read from it so mode is "r"
	learnedtxt = open(config.learned_tweets, "r")
	#shove these other pieces of shit into a list
	learned = [line.strip() for line in learnedtxt]	

	#combine the lists
	lines = brains + twets + learned
	
	b = Brain(os.path.join(os.path.dirname(__file__), 'cobe.brain'))
	
	

	#truncate to 140 characters, do not cut off words
	def smart_truncate(content, length=140):
	    if len(content) <= length:
	        return content
	    else:
	        return content[:length].rsplit(' ', 1)[0]

	#check tweet vs text files and reject if >60% the same as a tweet up in there
	def check_tweet(content):
		for line in lines:
			if Levenshtein.ratio(re.sub(r'\W+', '', content), re.sub(r'\W+', '', line)) >= 0.60:
				return False
		return True

	# get a reply from brain, encode as UTF-8
	i = 0
	while True:
		tweet = smart_truncate(b.reply("").encode('utf-8', 'replace'))
		#make sure we're not tweeting something close to something else in the txt files
		#or we can just give up after 100 tries
		if check_tweet(tweet) or i >= 100:
			break
		i += 1
		
	#put the tweet in the log
	tweetlog.write(tweet + '\n')
	
	#close all those files lol
	tweetlog.close()
	learnedtxt.close()
	primedtxt.close()
	if args.stdout:
		print tweet
	else:
		status = api.PostUpdate(tweet)