===========
House Rules
===========

This is the recorded list of operating policy of the TSC for things
not documented elsewhere.

Specs Approval
==============

Spec approval requires a simple majority of the current TSC membership.
If after two days of reaching majority if no negative votes are cast
the review may be merged.

Governance Changes
==================

The Technical Steering Committe Charter requires a super-majority approval
(2/3) of the current membership to change the governance charter or operating
policy.  These are specific exceptions to that rule to simplify the
maintenance of the ``stx-governance`` repository.

Typo Fixes
----------

When the change fixes content that is obviously wrong (updates an email
address, fixes a typo...) they may be approved after receiving a positive
vote from any TSC member.

Code Changes
------------

The ``stx-governance`` repository contains code used in the generation of
the published documentation.  We will apply our normal review rules.  Due to
the differences in Gerrit configuration for this repository we will consider
RollCall +1 votes as the +2 to let Code Review +1 continue to have its usual
meaning.

Change Correction
-----------------

If any TSC member disagrees with a change merged under these rules they can
propose a revert of that change.  The revert can be approved under the same
rules used in the original change.  The topic then should be discussed
during a TSC meeting, on the mailing list or in a new review proposed with
the change.
