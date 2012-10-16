# Get these from dev.twitter.com
api = {
	'consumer_key': '',
	'consumer_secret': '',
	'access_token_key': '',
	'access_token_secret': ''
}

# List of accounts that learn.py should grab tweets from
dump_accounts = ['']

#text file to save tweets we've made in
our_tweets = 'file.txt'
#text file to save tweets found via learn.py in
learned_tweets = 'another_file.txt'
#big text file of tweets you used to prime the brain with
brain_tweets = 'yet_another_file.txt'

# Skip replies when learning?
skip_replies = True

# Skip retweets when learning?
skip_retweets = True

# Reply to tweets?
replies = True

# list of screen names to ignore when replying, be sure to include your bot's own screen name!
screen_name = ['bots_screen_name', 'other_account_to_ignore']
