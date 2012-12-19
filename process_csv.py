import re, os, glob, csv

tweets = []

# move to the csv directory
os.chdir('csv')

# for each csv file
for filename in glob.glob('*.csv'):

    # open the file and parse it as csv
    with open(filename, 'rb') as csvfile:
        tweetreader = csv.reader(csvfile)
        for tweet in tweetreader:
            # the actual text is in the 8th position of the csv
            text = tweet[7]

            # add it to the tweetlist if it isn't a reply or retweet
            if not text.startswith('@') and not text.startswith('RT'):
                tweets.append(text)

# we have all the tweets now! throw em in a file, one per line
open('../tweets.txt', 'w').write('\n'.join(tweets))
print "Processed %d tweets" % len(tweets)
