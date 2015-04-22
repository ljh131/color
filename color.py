#!/usr/bin/python
from __future__ import print_function

import re
import sys
import fileinput
import getopt

RED		 = "\033[1;31m"
GREEN	 = "\033[1;32m"
YELLOW	 = "\033[1;33m"
BLUE	 = "\033[1;34m"
MAGENTA	 = "\033[1;35m"
CYAN	 = "\033[1;36m"
WHITE	 = "\033[1;37m"

COLORS = [RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE]
RESET	 = "\033[0m"

def usage():
	print('usage: %s <options> <patterns>', sys.argv[0])
	print('')
	print('options:')
	print('    -i: ignore case')
	print('patterns:')
	print('    <string>:<color>')
	print('colors:')
	print('    %sr[ed]%s, %sg[reen]%s, %sy[ellow]%s, %sb[lue]%s, %sm[agenta]%s, %sc[yan]%s, %sw[hite]%s' % ( 
			RED, RESET, 
			GREEN, RESET,
			YELLOW, RESET,
			BLUE, RESET,
			MAGENTA, RESET,
			CYAN, RESET,
			WHITE, RESET,
	))
	print('')
	print('eg)')
	print('    echo "hello color" | %s "hello:r" "o:b" "c:y"' % sys.argv[0])

def main():
	try:
		opts, args = getopt.getopt(sys.argv[1:], "i", ["help"])
	except Exception as err:
		usage()
		sys.exit(2)

	if len(args) == 0:
		usage()
		sys.exit(2)

	ignorecase = False

	for o, a in opts:
		if o in ("-h", "--help"):
			print('no help')
			sys.exit(2)
		elif o in ('-i'):
			ignorecase = True

	patterns = []	# array of dict(pattern=pat, color=cr)
	cridx = 0
	for a in args:
		ar = a.split(':')
		if len(ar) == 1:
			# pattern only
			pat = ar[0]
			cr = COLORS[cridx % len(COLORS)]
			cridx += 1
		else:
			# pattern:color (could be abbr.)
			pat = ar[0]
			color = ar[1]
			if color.startswith('r'):
				cr = RED
			elif color.startswith('g'):
				cr = GREEN
			elif color.startswith('y'):
				cr = YELLOW 
			elif color.startswith('b'):
				cr = BLUE
			elif color.startswith('m'):
				cr = MAGENTA
			elif color.startswith('c'):
				cr = CYAN
			elif color.startswith('w'):
				cr = WHITE
			else:
				cr = WHITE

		patterns.append(dict(pat='(%s)' % pat, sub='%s\g<1>%s' % (cr, RESET)))

	if ignorecase:
		reflags = re.IGNORECASE
	else:
		reflags = 0

	try:
		while True:
			line = sys.stdin.readline()
			if not line: break

			for d in patterns:
				line = re.sub(d['pat'], d['sub'], line, flags=reflags)
			print(line, end='')
			sys.stdout.flush()
	except KeyboardInterrupt:
		pass

main()

