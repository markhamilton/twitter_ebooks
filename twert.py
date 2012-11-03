import twitter, argparse, sys, os
import config
import Levenshtein
import re
import db_manager
from cobe.brain import Brain

parser = argparse.ArgumentParser(description="Post ebooks tweets to twitter.")
parser.add_argument('-o', '--stdout', action='store_true', help="Output to stdout instead of posting to twitter.")
parser.add_argument('-t', '--tweet', help="Tweet arbitrary text instead of using the brain.")

args = parser.parse_args()

api = twitter.Api(**config.api)

if args.tweet:
	api.PostUpdate(args.tweet)
else:
	blacklist = config.blacklist
	#get all our tweets
	lines = db_manager.get_tweets()
	b = Brain(os.path.join(os.path.dirname(__file__), 'cobe.brain'))
	
	#truncate to 140 characters, do not cut off words
	def smart_truncate(content, length=140):
	    if len(content) <= length:
	        return content
	    else:
	        return content[:length].rsplit(' ', 1)[0]

	#check tweet vs text files and reject if >70% the same as a tweet up in there or if it contains a blacklisted word
	def check_tweet(content):
		for k in blacklist:
			if k in content:
				return False
		for line in lines:
			if Levenshtein.ratio(re.sub(r'\W+', '', content), re.sub(r'\W+', '', line)) >= 0.70:
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
		
	#put the tweet in the db
	db_manager.insert_tweet(tweet)
	if args.stdout:
		print tweet
	else:
		status = api.PostUpdate(tweet)