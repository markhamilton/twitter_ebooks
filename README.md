This is an update to https://github.com/postcasio/twitter_ebooks

It prevents the bot from tweeting verbatim tweets from its source accounts.
It also prevents it from repeating itself. It will eventually run out of things to tweet so you should probably clear its log everyday.
(I do this by putting: 
0 0 * * * rm /path/to/tweetlog.txt > /dev/null 
in crontab. the file you need to delete is the one you listed for 'our_tweets' in config.py)

You set it up basically the same way as before. 
The only difference is that there's now a few more things in config.py to set up.

Also note that it doesn't do all the checks and junk for replies yet.