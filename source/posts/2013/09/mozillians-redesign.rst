Mozillians Redesign
###################
:date: 2013-09-18
:category: Blog
:tags: mozilla

Help test the new site redesign.  Welcome to the `Mozillians project`_ - a
`community phonebook`_ to find, share and communicate with like minded
Mozillians throughout the world. I'm thrilled to announce the latest
evolution of the website.

The team has been feverishly redesigning the user experience. We're at a point
of stability; design ideas have been expressed, debated, agreed upon, and those
ideas codified. 

.. image:: /static/images/2013/06/new_mozillians.png
   :width: 75%
   :align: center
   :alt: The new Mozillians.org
   :target: https://mozillians.allizom.org

A test environment is live on our staging server - `mozillians.allizom.org`_ 
- for your critical eye. We welcome you to explore the new site and offer
your open and unabashed feedback.

Test Plan
---------
We are doing `exploratory testing`_.  Here are a few things you could check for:

- Functionality – a feature does what it is supposed to do.
- Layout issues - does the site look correct in different environments and screen resolutions?
- Usability - does something not make sense? seem hard to use?
- Security – XSS, encoding/escaping issues, etc.
- Error handling – system fails gracefully and displays useful and appropriate error messages
- localization (l10n)

Out of scope for this test cycle (don't test):

- the profile pages - work is still being completed on their design. For example here is my `profile page`_
- search functionality - we know that search and results it returns work sub-optimally and will improve it in the future

Environments to test against:

- Linux, OSX, Windows
- Android, iOS
- Firefox (RC, Beta, Nightly), Chrome, IE 9+, Safari

Setup
-----

To get started you’ll need:

- Get a vouched Mozillians account on our `staging server`_. Ask in `#commtools`_ to have your account vouched.
- Disposable email addresses so you can create test accounts on stage. I recommend free services like `Mailinator`_ or `10minutemail`_.

Filing Bugs
-----------

Important tips for filing bugs:

- `Search Bugzilla`_ to see if the defect has already been filed. Try not to file duplicates if a bug already exists.
- Write good bugs that provide clear steps to reproduce the problem. Read `this document`_ for tips.
- Use `this form`_ to file new bugs.
- `Bugzilla etiquette`_ - be polite and treat people with respect, we are a friendly community.
- `IRC etiquette`_ - same as Bugzilla; relax and have fun.

We plan on keeping this test cycle open from 2013-09-18 to 2013-09-25.

We really appreciate your enthusiasm and help with making the community
phonebook better. This is fully a community initiative and wouldn't exist
without you. If you have questions or simply want to say hello reach out in IRC
- `#mozwebqa`_ or `#commtools`_ - and introduce yourself. Myself or another
community member will help you. My online name is mbrandt.

I look forward to seeing you online!

Matt Brandt

https://mozillians.org/u/mbrandt


.. _Mozillians project: https://mozillians.org
.. _community phonebook: https://wiki.mozilla.org/Mozillians
.. _mozillians.allizom.org: https://mozillians.allizom.org
.. _exploratory testing: http://en.wikipedia.org/wiki/Exploratory_testing
.. _IRC: https://wiki.mozilla.org/IRC
.. _#mozwebqa: https://widget00.mibbit.com/?settings=1b10107157e79b08f2bf99a11f521973&server=irc.mozilla.org&channel=%23mozwebqa
.. _#commtools: https://widget.mibbit.com/?settings=1b10107157e79b08f2bf99a11f521973&server=irc.mozilla.org&channel=%23commtools
.. _staging server: https://mozillians.allizom.org
.. _Mailinator: http://mailinator.com/
.. _10minutemail: http://10minutemail.com
.. _Search Bugzilla: https://bugzilla.mozilla.org/buglist.cgi?cmdtype=runnamed&namedcmd=phonebook%20%3A%3A%20unknown&list_id=6730411
.. _this document: https://developer.mozilla.org/en-US/docs/Mozilla/QA/Bug_writing_guidelines?redirectlocale=en-US&redirectslug=Bug_writing_guidelines
.. _this form: https://bugzilla.mozilla.org/enter_bug.cgi?product=Community%20Tools&component=Phonebook
.. _Bugzilla etiquette: https://bugzilla.mozilla.org/page.cgi?id=etiquette.html
.. _IRC etiquette: https://quality.mozilla.org/docs/misc/getting-started-with-irc/
.. _profile page: https://mozillians.allizom.org/u/mbrandt/
