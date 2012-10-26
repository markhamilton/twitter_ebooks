This is an update to https://github.com/postcasio/twitter_ebooks

List of changes:

-You can define more than one account to ignore when replying, i.e. other bots

-Bot won't tweet verbatim from its source material (text file used to prime the brain and auto-learned tweets)

-Bot keeps track of what it's tweeted and won't repeat itself. It will eventually run out of things to tweet so you should probably clear its log every few day depending on how much material
the bot has to work with, for example thom ebooks could probably go for like a dang year without needing to repeat.

Anyay to clear the log you can use crontab i.e.:

0 0 */2 * * rm /path/to/tweetlog.txt > /dev/null 

will clear the log every other day. The file you need to clear is the one you put for 'our_tweets' in config.py. How often you'll actually need to clear the log is very specific to your individual bot so just play it by ear~!

You set it up basically the same way as before. 
The only difference is that there's now a few more things in config.py to set up.