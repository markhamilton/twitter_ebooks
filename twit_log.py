from time import strftime

class c_colors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'

prev_date = None
date_format = '%Y-%m-%d'

def writeline(text, debug=False, error=False ):
	global prev_date
	cur_date = strftime(date_format)

	if prev_date is None:
		prev_date = cur_date
		writeline("logging starting " + cur_date)
	if cur_date != prev_date:
		prev_date = cur_date
		writeline("day changed to " + cur_date)

	time_color = c_colors.OKGREEN
	if debug is True: time_color = c_colors.OKBLUE
	elif error is True: time_color = c_colors.FAIL

	print( time_color + "[" + strftime('%H:%M:%S') + "] " + ("DEBUG: " if debug is True else "") + c_colors.ENDC + text)


def quitmsg():
	writeline("signing off " + strftime(date_format))
