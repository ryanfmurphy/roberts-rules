# recommended to use python 3
from cmd import cmd
import re

def git_init(*args):     return cmd('git', 'init', *args)
def git_add(*args):      return cmd('git', 'add', *args)
def git_log(*args):      return cmd('git', 'log', *args)
def git_status(*args):   return cmd('git', 'status', *args)
def git_push(*args):     return cmd('git', 'push', *args)
def git_pull(*args):     return cmd('git', 'pull', *args)
def git_diff(*args):     return cmd('git', 'diff', *args)
def git_branch(*args):   return cmd('git', 'branch', *args)
def git_checkout(*args): return cmd('git', 'checkout', *args)
def git_merge(*args):    return cmd('git', 'merge', *args)
def git_reset(*args):    return cmd('git', 'reset', *args)

def git_commit(*args):
	if '-m' not in args:
		print 'Specify a commit message with -m'
		# (otherwise we hang when we try to open $EDITOR)
		return False
	return cmd('git', 'commit', *args)

def git_parent_branch(branch=None):
	if branch is None:
		branch = git_current_branch()
	# main functionality - get parent branch
	logtxt = git_log(branch, '--decorate', '--oneline')
	loglines = logtxt.split('\n')
	parent_match = re.search(r'\((.*)\)', loglines[1])
	if parent_match:
		parent = parent_match.group(1)
	elif branch == 'master':
		parent = None
	else:
		parent = 'master'
	return parent

def git_current_branch():
	branch_txt = git_branch()
	branches =  branch_txt.split('\n')
	for branch in branches:
		if len(branch) and branch[0] == '*':
			return branch[2:]
	return None

#todo get current HEAD

