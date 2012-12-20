#twitter_ebooks

This is an update to https://github.com/clonepa/twitter_ebooks, which is an update to postcasio's version, which is an update to thom's version.

3 non-standard twitter dependencies:
- Levenshtein - http://pypi.python.org/pypi/python-Levenshtein/
- Cobe - https://github.com/pteichman/cobe
- Python-Twitter - https://github.com/postcasio/python-twitter/tarball/master

(There are two common twitter api modules, make sure you grab the right one if you're using a package manager.)

This update comes with some new features:
- Centralized Tweeting Code
- Now matches identical tweets (happens often if you have small amounts of initial tweet data.)
- Option in the configuration file to filter URLs
- Feed greptweet.com text files directly to process.py and it removes all the junk for you automatically for easier setup

Here's how to set it up (instructions modified from Thom, et. al):

###REQUIREMENTS

- Any decent linux distro.
- A new twitter account 
- The files from this package. Just unzip them into a folder in your user folder (here on out referred to as the ebooks folder)

###PREPARING TWEETS

- Go to greptweet.com and fetch the tweets of your desired user(s)
- Save as .txt file in your ebooks folder
- ch to the ebooks folder and run:
  - `python process.py tweetfile.txt`
- This removes the timestamps, direct replies, retweets, blank lines, and fixes some HTML entities that greptweets leaves in.

###CREATE APP

- Log into dev.twitter.com with your bot account. Then clicky: https://dev.twitter.com/apps
- Click create new application and fill out everything but callback url.
- Click on your new application and go into settings. Here, change the application type to Read and Write. Update settings and return the details tab. Here, scroll to the bottom and click 'create my access token'.
- Copy these four values: 
  - consumer key 
  - consumer secret 
  - access token 
  - access token secret 
- Verify that access level is 'read and write'.

###INSTALL PYTHON DEPENDENCIES

(This will assume that you have installed python-distribute through your package manager.)
- Execute these commands (with superuser privileges): 
  - `easy_install cobe`
  - `easy_install python-Levenshtein`
  - `easy_install https://github.com/postcasio/python-twitter/tarball/master`
- (If you're on ubuntu, use apt-get install for these packages. If easy_install gives you trouble use pip install.)
- Now download twitter_ebooks https://github.com/markhamilton/twitter_ebooks/tarball/master 
- Untar this into your ebooks folder

###CREATE YOUR ROBOT 

- Rename the `config-example.py` to `config.py` and edit it.
- Put the values you saved from your application earlier in the 'api' bit.
- Follow the instructions for the remainder of the config file. It's well commented 

###DO THIS IN ORDER

`cobe init` (this creates an empty cobe brain in the current directory) 

`python learn.py` (This is only necessary if you enabled auto-learning. This sets the initial "last tweet learned" so you do not feed the bot a tweet twice. on arch this must be python2 learn.py) 

`rm cobe.brain cobe.brain-journal` (this deletes the brain. we're going to create a new one using the file you prepared earlier) 

`cobe learn tweetfile.txt` (this creates a new brain, using the file you prepared earlier as training) 

Your bot is now ready! test it locally (this won't tweet anything) with:

`python twert.py -o`

When this is to your liking, you can do a final 'live' test by doing:

`python twert.py`

###AUTOMATE YOUR ROBOT

Chuck this into your crontab:

`0 * * * * python ~/twitter_ebooks/twert.py > /dev/null tag_br`
`0,30 * * * * python ~/twitter_ebooks/twitter_ebooks/reply.py > /dev/null`
`0 0 * * * python ~/twitter_ebooks/learn.py > /dev/null`

**REMEMBER THAT THE DIRECTORIES GIVEN ARE EXAMPLES AND THAT YOU NEED TO CHANGE THEM TO REFLECT WHERE THE SCRIPT AND BRAIN ACTUALLY ARE**

If you use Arch Linux, use python2 instead of python.

These directives will make the bot tweet once an hour, reply to tweets twice an hour, and learn new tweets once a day at midnight. Look up how cron works if you want to change this.

(I removed the instructions on how to replace crontab intentionally so you don't end up deleting your existing cron jobs. Look this up if you're not sure how to do it please.)

> "Your bot is ready! Go retweet it or something, NERD"
