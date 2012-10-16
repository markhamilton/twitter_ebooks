This is an update to https://github.com/postcasio/twitter_ebooks

List of changes:

-You can define more than one account to ignore when replying, i.e. other bots

-Bot won't tweet verbatim from its source material (text file used to prime the brain and auto-learned tweets)

-Bot keeps track of what it's tweeted and won't repeat itself. It will eventually run out of things to tweet so you should probably clear its log everyday.
(I do this by putting: 
0 0 * * * rm /path/to/tweetlog.txt > /dev/null 
in crontab. the file you need to delete is the one you listed for 'our_tweets' in config.py)


You set it up basically the same way as before. 
The only difference is that there's now a few more things in config.py to set up.

Also note that it doesn't do all the new checks and junk for replies yet.