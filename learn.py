import twitter, os
import config
from simplejson import loads, dumps
from cobe.brain import Brain
import db_manager

b = Brain(os.path.join(os.path.dirname(__file__), 'cobe.brain'))

try:
	state = loads(open(os.path.join(os.path.dirname(__file__), '.state'), 'r').read())
except:
	state = {}

if 'accounts' not in state:
	state['accounts'] = {}


api = twitter.Api(**config.api)

b.start_batch_learning()

tweets = 0


def smart_truncate(content, length=140):
	    if len(content) <= length:
	        return content
	    else:
		return content[:length].rsplit(' ', 1)[0]

for account in config.dump_accounts:
	print "Grabbing tweets for %s" % account
	
	if account in state['accounts']:
		last_tweet = long(state['accounts'][account])
	else:
		last_tweet = 0

	try:
		timeline = api.GetUserTimeline(
			screen_name=account, count=200, since_id=last_tweet,
			include_rts=config.skip_retweets,
			exclude_replies=config.skip_replies,
			trim_user=True
		)
	except:
		continue

	for tweet in timeline:
		b.learn(tweet.text)
		#add it to the db
		db_manager.insert_tweet(tweet.text.encode('utf-8', 'replace'), False)
		last_tweet = max(tweet.id, last_tweet)
		tweets += 1

	print "%d found..." % tweets
	state['accounts'][account] = str(last_tweet)

print "Learning %d tweets" % tweets
b.stop_batch_learning()
#close the learned txt
open(os.path.join(os.path.dirname(__file__), '.state'), 'w').write(dumps(state))
