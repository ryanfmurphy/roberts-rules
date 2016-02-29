'''
Robert's Rules
generic interface

when at a certain node
    can that node be discussed? voted on?
    can a motion be proposed?

are some motions proposed regarding branches under a committee instead of the whole group?
    each branch has a voter group of users
'''

import datetime
import git

class OutOfOrderError(Exception):
    pass


class User():
    def __init__(self, backend):
        self.backend = backend
    def propose_motion(self, title):
        motion = Motion(title)
        #return backend.create_motion(motion)
    def vote_on_motion(self, motion, vote):
        return motion.vote_on(motion, vote,  self)
        # return Motion()


class Motion():

    def __init__(self, title, members, quorum=.5, majority=.5):
        self.title = title
        self.members = members
        self.quorum = quorum
        self.majority = majority
        self.votes = {}

    def vote_on(self, vote, voter):
        #todo record timestamp
        if voter in self.members:
            self.votes[voter] = {
                'vote': vote,
                'time': datetime.datetime.now(),
                'voter': voter,
            }
        else:
            raise OutOfOrderError('This voter cannot vote on this motion')

    def get_discussion(self):
        pass

    def is_passing(self):
        #todo the motion could still be In Discussion, in which it can't be voted on yet
            # or there could be an Amendment that hasn't yet been voted on
        n_members = len(self.members)
        n_votes = len(self.votes)
        pct_present = float(n_voters) / n_members
        quorum = (pct_present >= self.quorum)
        if quorum:
            # votes are either 1 yea or 0 nay
            vote_values = (vote['vote'] for vote in votes.values())
            pct_yea = float(sum(vote_values)) / n_votes
            return pct_yea >= self.majority
        else:
            return None

    def enact(self, backend):
        'update the content/bylaws to reflect the motion'
        return backend.enact_motion(self)


class Backend():
    def __init__(self, users=None):
        self.users = users or {}
    def create_motion(self, motion):
        pass
    def enact_motion(self, motion):
        pass


class GitBackend(Backend):

    def create_motion(self, motion):
        # we assume we're at the right directory
        # and the right branch
        # and all file changes are already made
        git_checkout('-b', motion.title)
        git_add('-A')
        git_commit('-am', 'Motion: ' + motion.title)

    def enact_motion(self, motion):
        pass

