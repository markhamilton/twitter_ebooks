#import config
import twit_log
import time
import sys
import string
import random

def do_main_loop():
	while True:
		twit_log.writeline("Checking jobs...")

		# adding example job!
		# TODO: only write like this to stdout when not in daemon mode
		for y in range(30):
			for x in range(10):
				sys.stdout.write(random.choice(string.ascii_letters))
				sys.stdout.write('\b')
				sys.stdout.flush()
				time.sleep(0.01)
			sys.stdout.write('\033[1C') # advance 1c
			sys.stdout.flush()
			time.sleep(0.2)
		print("") # advance 1r

		time.sleep(2)

