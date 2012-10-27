import twitter, os
import config
import db_manager
import Levenshtein
import re
from simplejson import loads, dumps
from cobe.brain import Brain

def smart_truncate(content, length=140):
	    if len(content) <= length:
	        return content
	    else:
	        return content[:length].rsplit(' ', 1)[0]

b = Brain(os.path.join(os.path.dirname(__file__), 'cobe.brain'))


try:
	state = loads(open(os.path.join(os.path.dirname(__file__), '.state'), 'r').read())
except:
	state = {}

if 'last_reply' not in state:
	state['last_reply'] = 0

api = twitter.Api(**config.api)

def check_names(rp):
	for name in config.screen_name:		
		if rp.user.screen_name.lower() == name.lower():
			return True
	return False

if config.replies:
	print "Performing replies"
	
	lines = db_manager.get_tweets()
	last_tweet = long(state['last_reply'])

	def check_tweet(content):
		for line in lines:
			if Levenshtein.ratio(re.sub(r'\W+', '', content), re.sub(r'\W+', '', line)) >= 0.70:
				return False
		return True
	
	replies = api.GetReplies(since_id=last_tweet)
	
	for reply in replies:
		if check_names(reply):
			continue
		try:
			i = 0
			while True:
				reply_tweet = smart_truncate(b.reply(reply.text.encode('utf-8', 'replace')).encode('utf-8', 'replace'))
				if check_tweet(reply_tweet) or i >= 100:
					break
				i += 1
			db_manager.insert_tweet(reply_tweet)
			reply_tweet = smart_truncate('@%s %s' % (reply.user.screen_name.encode('utf-8', 'replace'), reply_tweet))
			api.PostUpdate(reply_tweet, in_reply_to_status_id=reply.id)
		except:
			print 'Error posting reply.'
		last_tweet = max(reply.id, last_tweet)

	state['last_reply'] = str(last_tweet)

print "Saving state"

open(os.path.join(os.path.dirname(__file__), '.state'), 'w').write(dumps(state))
