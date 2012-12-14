import argparse
import re

parser = argparse.ArgumentParser(description="Prep a file directly from greptweet.com (but doesn't import it into the brain). This will replace the contents of the existing file.")
parser.add_argument('file', metavar='file', type=str, help='A file filled with raw tweet data')
args = parser.parse_args()

contents = open(args.file, "r").read()

# remove timestamps
contents = re.sub(r'^.*\|.*\|', '', contents, flags=re.MULTILINE)

# remove retweets
contents = re.sub(r'^RT.\@.*', '', contents, flags=re.MULTILINE)

# remove direct replies
contents = re.sub(r'^@.*$', '', contents, flags=re.MULTILINE)

# remove blank lines (do this twice)
contents = re.sub(r'^\s', '', contents, flags=re.MULTILINE)
contents = re.sub(r'^\s', '', contents, flags=re.MULTILINE)

# replace html entities (twitter is sloppy)
contents = contents.replace('&gt;', '>')
contents = contents.replace('&lt;', '<')
contents = contents.replace('&amp;', '&')

# write it all back to the same file.
open(args.file, "w").write(contents)
print( 'Processed {} ({} chars)'.format(args.file, len(contents) ) )