---
morea_id: reading-code-reviews
morea_type: reading
title: "Code Reviews"
published: True
morea_summary: "What kind of reviews are we using in ICS 211?"
morea_sort_order: 4
morea_labels: 
---

## What are Reviews?

Code reviews are a software engineering technique designed to improve
the quality and productivity of the software development process. In
reviews you or a team of reviewers study a software development
product to understand it, fix the defects, logic, structure and
clarity.

## What can you Review?

Any software development product:

 * Plans,
 * Requirements,
 * Design documents,
 * Code,
 * Test plans and results,
 * Documentation,
 * etc.


## Three Review Methods

### Inspections

Inspections are a formal structured process for a team review of a
software product to find defects. Inspections were introduced in 1976 by Fagan.

Fagan Inspections assign roles to the participants and generally have
three phases. The roles are:

 * *Author*: the person who created the artifact
   under review.
 * *Reader*: the person who presents / paraphrases the document under
   review during the review meeting.
 * *Reviewers*: the people who review the document for defects.
 * *Moderator*: the person responsible for the inspection and keeping
   the process focused.

The three phases are:

 1. *Preparation*: The reviewers review the document on their own
    looking for defects. Often, they use checklists to focus their
    efforts.
 2. *Review Meeting*: The reviewers, author, reader, and moderator
    meet face to face to review the document. The reader starts at the
    beginning and reads/paraphrases the document. Reviewers raise the
    issues they found with each line of the document. The moderator
    keeps the meeting focused on finding defects not fixing them. The
    issues are recorded for the author to fix in the next step.
 3. *Repair and Report*: The author fixes the defects found during the
    review meeting and reports to the moderator.

Many software development teams have used Inspections to reduce the
number of defects earlier in the development process thus reducing the
overall software development effort.

### Walk-throughs

Walk-throughs are a less formal process than inspections. Usually the
author presents their code / work product to the reviewers in a
meeting.  The reviewers examine the document under review and raise
any issues they find. There typically isn't any preparation phase for
walk-throughs. After the meeting, the author fixes the defects found
during the walk-through.

### Personal/Peer Reviews

In personal reviews, you review your own document, looking for
defects, logic problems, poor structure and unclear sections.  In peer
reviews, you review your peer's document looking for the same
problems. When you find a problem note it so the author can fix the
problem later.

In peer reviews, it is good to note any positive features you find in
the document.

### ICS 211 Peer Reviews

In ICS 211 we will be using peer reviews. When given another
developer's or teams code. You should read through the code looking
for defects. Defects include not following the Java Coding Style, bad
variables, incorrect code, confusing code, etc. Mark the issues on the
code before returning it to the developer.  We also include one
positive about the code under review.
