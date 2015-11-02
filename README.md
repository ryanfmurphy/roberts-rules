Robert's Rules of Order
=======================

# Goal

Help people (e.g. the Open Source movement) have more structure
and participation in their community decision making processes
by implementing Robert's Rules of Order as an API / in an online
discussion context.


# Motions

Motions could take the physical form of (e.g.):

* Running a Command in a computing environment

* Accepting a Pull Request on a Git project
    The project wouldn't have to have anything to do with coding.
    The repo could just consist of documents about decisions, agreements
    and plans you are making together.
    (could be considered a Command)

* Admission of a new Member into the Community
  (could be considered a Command)

* Granting a Member limited/temporary Administrator Rights
  on the environment


## Motions with and without Discussion

Some motions by their nature have Discussion prior to Voting, while
some do not.  See Robert's Rules of Order.


## Motions with and without Amendability

Some motions by their nature have the possibility of Amendment prior to Voting,
while some do not.  See Robert's Rules of Order.


## Conflicts between Motions

2 or more Members during the same Submission Window may submit 2 or more
conflicting Motions.  If these motions are detected or flagged as conflicting,
this will automatically create a Motion to resolve the Conflict.

In a motion to resolve a Conflict, there would be a window for members to
submit a Motion (a diff) that synthesizes the Motions without conflicts.
The synthesizing Motion with the most Yay votes would pass in place of the
Motions under conflict.


# Example of Flow

* Suppose there's a Project.
* Someone might make a Motion,
    e.g. to create or modify some document
    (i.e. submits a Pull Request to the democratically-controlled repo)

* In the democratic process of deciding whether to accept the pull request:
    * Someone else might Second the Motion
    * At that point the Motion is in Discussion
        * Someone could move to amend the Motion / pull request
            (this amendment would need to be seconded and voted on)
    * If no one needs to discuss / after needed discussion, it goes to a vote


# Discussion

In a round of discussion, everyone could be given a time period,
x, to submit their thoughts (y words or chars), and they would all be
posted automatically at once.  There would be z rounds of discussion.

Default values of x, y and z would be agreed upon and subject to change
via the usual Process.


# Voting

The members would vote Yay, Nay or Abstain regarding whether to pass the
(possibly amended) Motion.  p percent of Yays would be required
for the Motion to pass.

A Quorum of at least q Acknowledgments would be required for a Vote on a
Motion to be considered valid.

An Acknowledgment could consist of e.g. casting a Yay, Nay or Abstain vote,
or e.g. of just reading the Motion in the first place.


# Membership & Quorum

The value of q could go up as new Members are admitted.  But if this were
the case then the group would need to be careful about admitting too many
Members who were not very involved, lest it stagnate the Project by making
it too difficult to pass Motions.

Members could move to raise the value of q for a specific Motion if e.g.
it seems very impactful and needs more discussion, or they could move to
lower the value of q if e.g. some people feel it is very important but not
everybody needs to be involved.


# Committees

A Motion could create a Committee, a sublist of Members who could move and
discuss motions without flooding the rest of the Community.  Motions decided
by the Committee would still need to go to the whole Community to be passed /
incorporated into the documents.


# Other Applications

Without using a git repository, processes could use this as a Committee Strategy
for arbitration of Shared Resources, e.g. reading/writing a filesystem,
relational db, or document store.

Another possibility would be to have a customized IRC Chatroom running using
this process to moderate / channel discussion.  A regular IRC Bot wouldn't have
enough power to enforce the process (i.e. limits of debate) for all members of
the chatroom, but perhaps a modification on the server would allow it.


# Deliverables / Implementation

* Specification / Protocol
* Initial pilot in Python

## API Layers

* Python function-level API
* Process stdin-stdout-level API (between Members and Chair)
* HTTP Endpoints
    * Member's Servers would hit the Chair's Endpoints
    * Members could request from the Chair the list of Motions and Metadata
    * (or Chair could broadcast back to Members the results?)

