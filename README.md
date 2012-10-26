This is an update to https://github.com/postcasio/twitter_ebooks (Setup instructions are essentially the same as detailed in that project's readme)

A single dependency has been added: http://pypi.python.org/pypi/python-Levenshtein/

I believe everything else come standard with python

The functionality of the bot has been extensively upgraded at this point, some highlights:

* bot keeps track of what it's tweeted and doesn't repeat a specific tweet until a user defined amount of time have passed
* bot won't copy tweets verbatim from a list of definable text files, such as the file you used to prime it or old log files from previous versions
* bot won't copy tweets verbatim that it learns on the fly via learn.py
* it now uses an SQLite database to keep track of tweets its made and learned along with timestamps
* you can now define a list of users to ignore when replying such as other bots
* you don't have to fool with crontab to delete logs anymore, tweets are tracked on an individual basis and expire automatically
* probably some other stuff i forgot aaaa
