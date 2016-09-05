# -*- coding: utf-8 -*-

import twitter, argparse, sys, os
import config
import twert_helper

parser = argparse.ArgumentParser(description="post ebooks tweets to twitter")
parser.add_argument('-o', '--stdout', action='store_true', help="output to stdout instead of posting to twitter.")
parser.add_argument('-t', '--tweet', help="tweet arbitrary text instead of using the brain.")
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

