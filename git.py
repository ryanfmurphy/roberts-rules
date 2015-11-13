# recommended to use python 3
from cmd import cmd

def git_add(*args):      return cmd('git', 'add', *args)
def git_commit(*args):   return cmd('git', 'commit', *args)
def git_status(*args):   return cmd('git', 'status', *args)
def git_push(*args):     return cmd('git', 'push', *args)
def git_pull(*args):     return cmd('git', 'pull', *args)
def git_diff(*args):     return cmd('git', 'diff', *args)
def git_branch(*args):   return cmd('git', 'branch', *args)
def git_checkout(*args): return cmd('git', 'checkout', *args)
def git_merge(*args):    return cmd('git', 'merge', *args)
def git_reset(*args):    return cmd('git', 'reset', *args)

