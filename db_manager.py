import config
import sys, os
import datetime
import sqlite3

db = sqlite3.connect('twets.db', detect_types=sqlite3.PARSE_DECLTYPES)

def get_tweets():
	with db:
		tweets_from_db = []	
		cur = db.cursor()
		#create the table if it doesn't exist
		cur.execute("CREATE TABLE IF NOT EXISTS tweets(content TEXT, date TIMESTAMP, ours BOOLEAN)")
		#get all the tweets!
		for t in cur.execute('SELECT * FROM tweets'):
			if t.ours == False or datetime.datetime.now() - t.date > datetime.timedelta(hours = config.log_time):
				tweets_from_db.append(str(t.content))
		#list to hold tweets from txt files
		txt_tweets = []
		#open the file used to prime the brain
		for f in config.brain_tweets:
			#shove those pieces of shit into a list
			txt_tweets += [line.strip() for line in openfile(f)]
		#return both lists combined
		return tweets_from_db + txt_tweets

def insert_tweet(content, ours=True):
	with db:
		cur = db.cursor()
		#create the table if it doesn't exist
		cur.execute("CREATE TABLE IF NOT EXISTS tweets(content TEXT, date TIMESTAMP, ours BOOLEAN)")
		#prepare and insert the tweet
		t = [str(content).encode('utf-8', 'replace'), datetime.datetime.now(), ours]
		cur.execute("INSERT INTO tweets VALUES (?,?, ?)", t)

		

def openfile(path):
	#note: i don't actually know if you have to close + reopen a file to change the mode soooo
	if os.path.exists(os.path.join(os.path.dirname(__file__), path)) == False:
		txtfile = open(os.path.join(os.path.dirname(__file__), path), "w")
		txtfile.close
	#open for read and write
	txtfile = open(os.path.join(os.path.dirname(__file__), path), "r+")
	return txtfile
