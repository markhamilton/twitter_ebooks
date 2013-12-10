# Get these from dev.twitter.com
api = {
	'consumer_key': '',
	'consumer_secret': '',
	'access_token_key': '',
	'access_token_secret': ''
}

# List of accounts that learn.py should grab tweets from
#example: ['usagipic_bot', 'bug_horse']
dump_accounts = ['']

#list of prexisting text files to check our tweets against to avoid copying verbatim
#the text file you used to prime the brain should be included here
#old log files should also be included here if you're upgrading from the old version that used text files to log everything
#example: ['tweetlog.txt', 'braintweets.txt']
brain_tweets = ['']

#how long should the bot avoid repeating a specific tweet it's made, in hours?
#by the way, this is tracked on a per tweet basis now COOL WOW NICE DUDE
log_time = 72

#What Levenshtein ratio should we use?
#Higher numbers allow tweets that are more similar to the originals
#Range is from 0 to 1
levenshtein_ratio = 0.80

# Reply to tweets?
replies = True

# list of screen names to ignore when replying, be sure to include your bot's screen name!
#example: ['thom_ebooks', 'clonepa_']
screen_name = ['']

# Filters
filter_url = False
filter_handle = False
filter_hashtag = False

#blacklist of words or phrases to reject tweets based on
#be sure to include spaces!! for example "is" will give a false positive and match "this", but " is " (note the spaces) won't.
#example: [' badword ', ' butt ']
blacklist = ['']
