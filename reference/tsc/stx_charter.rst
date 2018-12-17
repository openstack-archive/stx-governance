=====================================
Draft - StarlingX Initial Governance
=====================================

The initial draft of this document with feedback from the reviewers
`is on this Etherpad <https://etherpad.openstack.org/p/stx-governance>`_.

-------------
Introduction
-------------

The StarlingX project is governed according to the OpenStack Foundation's
`four opens <https://governance.openstack.org/tc/reference/opens.html>`_,
which are open source, open design, open development and open community.
Technical decisions are made by technical contributors, technical leaders
and by a representative Technical Steering Committee.  Our community is
committed to diversity, openness, and encouraging new contributors and
leaders to rise up.

StarlingX is both a development project and an integration project.  It
includes new services that provide important features and combines them
with components from many other Open Source projects into a complete
Edge Cloud solution.  To help manage the complexity of the project, we
have divided the project up into several sub-projects, each with project
and technical leadership, to help distribute the overall work and to
acknowledge in the community that there are multiple ways to
contribute to the project.  The sub-project lifecycle is managed by
the project's Technical Steering Committee who approve the creation of
new sub-projects and the retirement of sub-projects that are no longer active.

StarlingX is a brand new project and is in an initial "bootstrapping"
phase in which the leadership positions will be volunteers.  All
leadership positions will transition to be elected by the project's
Contributors within one year.

--------------
Project Roles
--------------

StarlingX defines the following roles for the project.

^^^^^^^^^^^^
Contributors
^^^^^^^^^^^^

A Contributor to StarlingX is someone who has made a Contribution to the
project within the last 12 months.  Contributions can include merged code,
test or document submissions, or serving in a leadership role as defined
below.  All Contributions are welcome and will be accepted based on their
technical merit.  The project's Technical Steering Committee can grant
Contributor status for other contributions at its discretion.

Contributors are eligible to vote in the elections for Technical
Steering Committee positions and for the leadership roles described in this
document.  Contributors are also eligible to become members of the
Technical Steering Committee and/or serve in a leadership role.

^^^^^^^^^^^^^^
Core Reviewer
^^^^^^^^^^^^^^

Core Reviewers are active Contributors and participants in a sub-project
that have the additional responsibility to review the changes proposed
to the sub-project, to ensure that approved changes are aligned with the
project's design & architecture, and meet the project's quality
requirements.  Core Reviewers have the ability to approve code and
documenation to be
merged into the StarlingX repositories.  Core Reviewers for a sub-project
are appointed by the sub-project Technical Lead with input from other
StarlingX Core Reviewers.  Contributors can become Core Reviewers for
multiple sub-projects.

^^^^^^^^^^^^^^^
Technical Lead
^^^^^^^^^^^^^^^

A Technical Lead in StarlingX is a Core Reviewer who has additional
responsibility for guiding the overall technical direction of one or
more of the sub-projects, under the overall technical guidance of the
Technical Steering Committee.  Technical Leads are responsible for
resolving disagreements between the sub-project's Contributors and
Core Reviewers.  A sub-project's Technical Lead should be included as a
reviewer and approver for any
`Feature Specification
<https://wiki.openstack.org/wiki/StarlingX/Feature_Development_Process>`_
that impacts their sub-project.  The initial Technical Leads are appointed
to one year terms at launch by the Technical Steering Committee but
will be fully elected by the sub-project's Contributors on an annual basis.
Technical Lead elections will be held in September of every year starting in
2019 and will be administered by the TSC or their delegates.  Contributors
can be Technical Leads for multiple sub-projects.

^^^^^^^^^^^^^
Project Lead
^^^^^^^^^^^^^

A Project Lead in StarlingX is an outside facing role for a StarlingX
sub-project that is responsible for requirements gathering, tracking
progress, reporting results, handling outside communication, serving as a
project ambassador and facilitating the four opens within the sub-project.
The Project Lead works with the Technical Lead and the sub-project team to
break down large work items for the team into Stories and Tasks.  The
Project Lead can help guide Contributors to the work items most needed
by the sub-project, as defined by the Project Priorities established by the
Technical Steering Committee.  The initial Project Leads are appointed to
one year terms at launch by the Technical Steering Committee but will be
fully elected by the sub-project's Contributors on an annual basis with
the first election to be held in April 2019.  Contributors can be
Project Leads for multiple sub-projects.

The same person can become a Technical Lead and Project Lead for a
StarlingX sub-project.  That person's role would then be similar to an
`OpenStack PTL <https://docs.openstack.org/project-team-guide/ptl.html>`_
The StarlingX project has split these roles to enable Technical Leaders
to focus more of their attention on technical issues and to leverage
the skills and strengths of Project Leaders in the initial community.

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Technical Steering Committee
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Technical Steering Committee is responsible for overall project
architectural decisions, managing the sub-project life-cycle including
approving new sub-projects and making final decisions if sub-project
Core Reviewers, Technical Leads or Project Leads disagree.  It defines
the overall project architecture and sets the overall Project
Priorities in collaboration with the community.  It will be comprised of
7 members who will be initially appointed but fully elected by the
Contributors after the first year.

NOTE: There will be additional updates to this document to clarify the
timeline and process for electing TSC members.

The initial Technical Steering Committee members will be: Brent
Rowsell (Wind River), Ian Jolliffe (Wind River), Dean Troyer (Intel)
and Saul Wold (Intel).  The remaining members are yet to be determined.

NOTE: The paragraph below will be changed in a future version of
this document.

In September 2019, 3 of the 7 seats are up for election by the project's
Contributors. Anyone who is a Contributor to the project will be
eligible to run, and anyone who is a Contributor is eligible to vote.
In that election the TSC positions held by one each of the members from
Wind River and Intel will be opened for election, as well as one of the
other initially-appointed seats, to be determined randomly (unless one
of the members voluntarily steps down).

In April 2020, the remaining 4 seats are up for election.  At
that time all initially appointed TSC positions will no longer be
appointed but will be elected by the Contributors.    TSC Elections
will continue on a staggered six month cycle (3 seats and 4 seats) in
order to ensure consistency across terms while allowing new leaders to
begin to serve. There are no limits on the number of terms an individual
may serve, but no single organization may be represented by more than
two seats at any given time.  In the event that 3 people from the same
organization are elected to the TSC in one election, the person with the
lowest vote count among the 3 is skipped and the next candidate is elected.
Any other case of more than 2 people per company on the TSC shall be
addressed at the latest at the next scheduled election.

The Technical Steering Committee will meet regularly in an open forum
with times and locations published in community channels.  The
Technical Steering Committee can elect a Chair at its discretion.

A quorum for the TSC requires more than half of the members.  When
the TSC membership is an even number, a quorum is half + 1.  The
TSC should seek consensus on issues and decisions however a simple
majority vote shall be sufficient for most resolutions. Certain
resolutions, specifically changing the project formal governance
(including this document) and changes to project structure
(adding or removing a sub-project) require a two-thirds majority vote.

The exact size and model for the Technical Steering Committee will
evolve over time based on the needs and growth of the project, but the
governing body will always be committed to openness, diversity and the
principle that technical decisions are made by technical contributors.

----------
Elections
----------

All elections for leadership positions in StarlingX shall follow standard
OpenStack procedures and methods.  Ballots will be distributed to each
Contributor's primary email address.  Elections will be held using
CIVS and a Condorcet algorithm (Schulze/Beatpath/CSSD variant). Any
tie will be broken using
`Governance TieBreaking
<https://wiki.openstack.org/wiki/Governance/TieBreaking>`_.
In the event that a candidate runs unopposed for a position, the
TSC can waive a formal vote. Membership in the Foundation itself is
not a requirement for holding an elected position though it is preferred.
Elections are appointing an individual to a position in the project, not
a company or organization.  Individuals are expected to continue to
support the project in the event of career changes unless they
notify the project that they are resigning their position.

-------------------
Governance Changes
-------------------

The project's formal governance document is maintained in the
stx-governance git repository.  Changes to the document can be proposed
by any project Contributor but would need to be ratified by the TSC
with a super-majority (2/3rds) vote.  The TSC should strive for
consensus for any change to the project's formal governance.
