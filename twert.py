#!/usr/bin/python

import twitter, argparse, sys, os
import config
import twert_helper

reload(sys)
sys.setdefaultencoding('utf-8')

parser = argparse.ArgumentParser(description="Post ebooks tweets to twitter.")
parser.add_argument('-o', '--stdout', action='store_true', help="Output to stdout instead of posting to twitter.")
parser.add_argument('-t', '--tweet', help="Tweet arbitrary text instead of using the brain.")
args = parser.parse_args()

api = twitter.Api(**config.api)

if args.tweet:
	# tweet arbitrary text from console
	api.PostUpdate(args.tweet)
else:
	tweet = twert_helper.create_tweet('', not args.stdout)
	if tweet == unicode(''):
		# failure: probably couldn't generate a tweet within the alloted tries
		print "Could not generate a unique tweet this time"
	else:
		if(args.stdout):
			print "Dry run: " + tweet
		else:
			status = api.PostUpdate(tweet)
			print "Tweeted: " + tweet
