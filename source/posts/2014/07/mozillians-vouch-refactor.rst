Mozillians Vouch Refactor - Testday
###########################################
:date: 2014-07-24
:category: Blog
:tags: mozilla

Welcome to the Mozillians project. We love working with old and new
contributors!

.. image:: /images/2014/07/mozillians-home-page.png
   :width: 85%
   :align: center
   :alt: The new Mozillians.org
   :target: https://mozillians.allizom.org

The latest `feature set`_ of the community phonebook `has landed`_
and is ready for testing. The phonebook is a place to find, share, and
communicate with open web advocates throughout the world.

The community has worked to find creative ways to make the phonebook a
place where `active and trusted memebers`_ of the community can connect. The
latest set of features seeks to push new contributors and returning contributors to be
more active in shaping our community.

The new trust model:

- Anyone can create a Mozillians account.
- 1 vouch allows users to search for and view Mozillian profiles
- 3 vouches are needed to vouch for new Mozillians

A test environment is live on our dev server - `mozillians-dev.allizom.org`_
- and ready for your critical eye. We welcome you to explore the features and offer
your `open, honest, and unabashed feedback`_.


Test Plan
====================

There are two areas that you can get involved with helping test; feature
verification using exploratory testing techniques and test automation coverage.

Setup for manual testing
----------------------------

Here are the `unverified features`_ that needs to still need to be tested. Find
a bug that needs verification and begin testing.If you have questions reach
out in IRC - `#mozwebqa`_ or `#commtools`_ - and introduce yourself.
Myself or another community member will help you.

To get started you’ll need:

- Disposable email addresses so you can create test accounts on `dev`_ I recommend free services like `Mailinator`_ or `10minutemail`_.
- `personatestuser.org`_ is one of my preferred tools if you don't need to verify receipt of email but it forces you to parse a json file.
- Create an account on our `dev server`_.
- Some of the test scenarios will require a vouched account. You can automatically vouch yourself by appending ``/vouch`` to the url.
- For example ``mozillians.allizom.org/u/your_account_name/vouch``.
- Alternatively you can unvouch yourself by appending ``/unvouch`` to the url.

Filing Bugs
^^^^^^^^^^^^

- Write good bugs that provide clear steps to reproduce the problem. Read `this document`_ for tips.
- Use `this form`_ to file new bugs.
- `Bugzilla etiquette`_ - be polite and treat people with respect, we are a friendly community.
- `IRC etiquette`_ - same as Bugzilla; relax and have fun.

Setup for test automation
----------------------------

Creating test automation assumes that you have a bit of experience writing code and working with version control.

.. image:: /images/2014/07/mozillians-tests-readme.png
   :width: 75%
   :align: center
   :alt: The new Mozillians.org
   :target: https://github.com/mozilla/mozillians-tests/blob/master/README.md

Getting started:

- Work through the `mozillians-tests project ReadMe`_
- Review the `open git issues`_ for the project and assign one to yourself
- Talk to us in the `#mozwebqa`_ irc channel. We have a popping fun community that is energetic and would be thrilled to work with you.

We really appreciate your enthusiasm and help with making the community
phonebook better. This is fully a community initiative and wouldn't exist
without you.

I look forward to seeing you online!

Matt Brandt

https://mozillians.org/u/mbrandt


.. _Mozillians project: https://mozillians-dev.allizom.org
.. _dev: https://mozillians-dev.allizom.org
.. _feature set: https://bugzilla.mozilla.org/buglist.cgi?o13=substring&o9=substring&f13=cf_crash_signature&o2=substring&status_whiteboard_type=regexp&f12=status_whiteboard&status_whiteboard=vouching%20rel.%201&o12=substring&f14=CP&f10=alias&f1=OP&o3=substring&f0=OP&f8=product&o11=substring&f15=CP&f9=component&j7=OR&f4=CP&query_format=advanced&o10=substring&j1=OR&f3=status_whiteboard&f2=short_desc&f11=short_desc&component=Phonebook&f6=OP&product=Community%20Tools&f7=OP&o8=substring&list_id=10741869
.. _has landed:  https://mozillians-dev.allizom.org
.. _active and trusted memebers: http://hoosteeno.com/2013/12/17/a-new-mozillians-org-signup-process/
.. _community phonebook: https://wiki.mozilla.org/Mozillians
.. _mozillians-dev.allizom.org: https://mozillians-dev.allizom.org
.. _exploratory testing: http://en.wikipedia.org/wiki/Exploratory_testing
.. _bugzilla query: https://bugzilla.mozilla.org/buglist.cgi?o13=substring&o9=substring&f13=cf_crash_signature&o2=substring&status_whiteboard_type=regexp&f12=status_whiteboard&status_whiteboard=vouching%20rel.%201&o12=substring&f14=CP&f10=alias&f1=OP&o3=substring&f0=OP&f8=product&o11=substring&f15=CP&f9=component&j7=OR&f4=CP&query_format=advanced&o10=substring&j1=OR&f3=status_whiteboard&f2=short_desc&f11=short_desc&component=Phonebook&f6=OP&product=Community%20Tools&f7=OP&o8=substring&list_id=10741869
.. _mozillians-tests project ReadMe: https://github.com/mozilla/mozillians-tests/blob/master/README.md
.. _mozillians-tests: https://github.com/mozilla/mozillians-tests
.. _open git issues: https://github.com/mozilla/mozillians-tests/issues?labels=Community&page=1&state=open
.. _IRC: https://wiki.mozilla.org/IRC
.. _#mozwebqa: https://widget00.mibbit.com/?settings=1b10107157e79b08f2bf99a11f521973&server=irc.mozilla.org&channel=%23mozwebqa
.. _#commtools: https://widget.mibbit.com/?settings=1b10107157e79b08f2bf99a11f521973&server=irc.mozilla.org&channel=%23commtools
.. _dev server: https://mozillians-dev.allizom.org
.. _open, honest, and unabashed feedback: https://bugzilla.mozilla.org/enter_bug.cgi?product=Community%20Tools&component=Phonebook&status_whiteboard=[vouching%20rel.%201]
.. _unverified features: https://bugzilla.mozilla.org/buglist.cgi?list_id=10807942&resolution=FIXED&classification=Other&status_whiteboard_type=allwordssubstr&query_format=advanced&status_whiteboard=[vouching%20rel.%201]&bug_status=RESOLVED&component=Phonebook&product=Community%20Tools
.. _Mailinator: http://mailinator.com/
.. _10minutemail: http://10minutemail.com
.. _personatestuser.org: http://personatestuser.org/
.. _this document: https://developer.mozilla.org/en-US/docs/Mozilla/QA/Bug_writing_guidelines?redirectlocale=en-US&redirectslug=Bug_writing_guidelines
.. _this form: https://bugzilla.mozilla.org/enter_bug.cgi?product=Community%20Tools&component=Phonebook&status_whiteboard=[vouching%20rel.%201]
.. _Bugzilla etiquette: https://bugzilla.mozilla.org/page.cgi?id=etiquette.html
.. _IRC etiquette: https://quality.mozilla.org/docs/misc/getting-started-with-irc/
.. _profile page: https://mozillians.allizom.org/u/mbrandt/

