# recommended to be run with python3

import subprocess

def cmd(*args):
	return subprocess.check_output(args)

