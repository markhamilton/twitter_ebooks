#import config
import twit_log
import time

def do_main_loop():
	while True:
		twit_log.writeline("Checking jobs...")
		time.sleep(60)

