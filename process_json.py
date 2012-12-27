import os, glob, json, codecs

tweets = []
ignored = 0

# move to the json directory
os.chdir('tweets')

# for each csv file
for filename in glob.glob('*.js'):

    # open the file and parse it as json
    with codecs.open(filename, 'r', encoding='utf-8') as jsonfile:
        tweetbuffer = jsonfile.readlines()[1:]
        tweetlist = json.loads(''.join(tweetbuffer))

        for tweet in tweetlist:
            text = tweet['text']

            # add it to the tweetlist if it isn't a reply or retweet
            if not text.startswith('@') and not text.startswith('RT'):
                tweets.append(text)
            else:
                ignored += 1

# we have all the tweets now! throw em in a file, one per line
codecs.open('../tweets.txt', 'w', encoding='utf-8').write('\n'.join(tweets))
print "Processed %d tweets (ignored %d)" % (len(tweets), ignored)
