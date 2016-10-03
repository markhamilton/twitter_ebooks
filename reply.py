#!/usr/bin/python

import twitter, argparse, os
import twert_helper
import config
from simplejson import loads, dumps
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

parser = argparse.ArgumentParser(description="Checks for recent unanswered @mentions and replies to them individually")
parser.add_argument('-o', '--stdout', action='store_true', help="Shows replies without actually sending to twitter")
args = parser.parse_args()

try:
	state = loads(open(os.path.join(os.path.dirname(__file__), '.state'), 'r').read())
except:
	state = {}

if 'last_reply' not in state:
	state['last_reply'] = 0

api = twitter.Api(**config.api)

# make sure we're not replying to ourselves
def check_names(rp):
	for name in config.screen_name:		
		if rp.user.screen_name.lower() == name.lower():
			return True
	return False

if config.replies:
	if not args.stdout:
		print "Performing replies"
	else:
		print "Printing test replies (dry-run)"
	
	last_tweet = long(state['last_reply'])
	replies = api.GetMentions(since_id=last_tweet)
	
	for reply in replies:
		if check_names(reply):
			continue

		reply_tweet = twert_helper.create_tweet(reply.text)
		if len(reply_tweet) == 0:
			# sometimes it can't be done with the catalyst given
			# so create something novel, instead
			reply_tweet = twert_helper.create_tweet()

		# make sure that we don't have a blank tweet
		# otherwise we'll send a blank reply
		if len(reply_tweet) > 0:
			reply_tweet = twert_helper.smart_truncate('@%s %s' % (reply.user.screen_name, reply_tweet))
			if not args.stdout:
				api.PostUpdate(reply_tweet, in_reply_to_status_id=reply.id)
			else: 
				print(reply_tweet)

		# mark it as last tweet either way
		# (in rare circumstances the bot won't reply)
		last_tweet = max(reply.id, last_tweet)

	if not args.stdout:
		state['last_reply'] = str(last_tweet)
		print "Saving state"

open(os.path.join(os.path.dirname(__file__), '.state'), 'w').write(dumps(state))
