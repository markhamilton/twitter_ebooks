#!/usr/bin/env python3

import os, sys
from loop import do_main_loop

if sys.version_info.major != 3:
	print("----\033[91m fatal error: twitter_ebooks [v2] requires python3 to run\033[0m")
	print("----\033[91m for compatibility info: https://github.com/markhamilton/twitter_ebooks\033[0m")
	sys.exit()

def create_daemon():
	try:
		pid = os.fork()
		if pid > 0:
			print("---- starting twitter_ebooks daemon as pid %d" % pid)
			os._exit(0)
	except OSError as error:
		print("----\033[91m unable to fork. error: %d (%s)" % (error.errno, error.strerror))
		os._exit(1)
	do_main_loop()

if __name__ == '__main__':
	create_daemon()
