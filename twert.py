import twitter, argparse, sys, os
import config
import twert_helper

parser = argparse.ArgumentParser(description="Post ebooks tweets to twitter.")
parser.add_argument('-o', '--stdout', action='store_true', help="Output to stdout instead of posting to twitter.")
parser.add_argument('-t', '--tweet', help="Tweet arbitrary text instead of using the brain.")

args = parser.parse_args()

api = twitter.Api(**config.api)

if args.tweet:
	api.PostUpdate(args.tweet)
else:
	tweet = twert_helper.create_tweet()
	if args.stdout:
		print tweet
	else:
		status = api.PostUpdate(tweet)
