import sys
import daemon

if sys.version_info[0] != 3:
	print("twitter_ebooks [v2] requires python3 to run")
	print("for compatibility see v1 at https://github.com/markhamilton/twitter_ebooks")


with daemon.DaemonContext():
	
