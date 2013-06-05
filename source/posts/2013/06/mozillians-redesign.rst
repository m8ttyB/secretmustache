Mozillians Redesign
###################
:date: 2013-06-03
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

A preview of the new site is live on our staging server - `mozillians.allizom.org`_ 
- and is ready for your critical eye. We welcome you to explore the new site and offer
your feedback and suggestions.

Test Plan
---------
We are doing `exploratory testing`_.  Here are a few things you could check for:

- Functionality – a feature does what it is supposed to do.
- Layout issues - does the site look correct in environments and screen resolutions?
- Usability - does something not make sense? seem hard to use?
- Security – XSS, encoding/escaping issues, etc.
- Error handling – system fails gracefully and displays useful and appropriate error messages

Environments to test against:

- Linux, OSX, Windows
- Android, iOS
- Firefox (RC, Beta, Nightly), Chrome, IE 8+, Safari

Out of scope of this test cycle (don't test):

- localization (l10n)
- the profile pages - work is still being completed on their design. For example here is my `profile page`_

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

We plan on keep this test cycle open from XXX to XXX.

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
.. _profile page: https://mozillians.allizom.org/u/mbrandt/
