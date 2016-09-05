#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, sys, argparse
import twit_log
from loop import do_main_loop

twit_log.writeline("twitter_ebooks.v2 launched")

parser = argparse.ArgumentParser(description="runs the teb.v2 daemon")
parser.add_argument('-s', '--no-daemon', action='store_true', help="output to stdout instead of running daemon")
args = parser.parse_args()

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
	if args.no_daemon:
		try:
			twit_log.writeline("running in stdout mode", debug=True)
			do_main_loop()
		except(KeyboardInterrupt, SystemExit):
			twit_log.writeline("keyboard interrupt; exiting")
			sys.exit(0)
		except:
			twit_log.writeline("unexpected error", error=True)
			sys.exit(1)
	else:
		#TODO: Flag daemon mode in the config, prevent it from writing to stdout with the log
		create_daemon()
