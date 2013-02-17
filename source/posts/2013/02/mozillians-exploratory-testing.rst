Mozillians Testplan
###################
:date: 2013-02-15
:category: Blog
:tags: Mozilla

Manual Testing
--------------
Welcome to the `Mozillians project`_ - A `community phonebook`_ to share, identify
and communicate with other Mozillians in our community. If this is your first
time working on a project at Mozilla or you're a seasoned veteran this is a great
project to get involved on.

.. image:: /static/images/2013/02/mozillians.png
   :width: 75%
   :align: center
   :alt: Mozillians.org homepage
   :target: https://mozillians.org

Exploratory Testing
-------------------
Exploratory testing is a great way to contribute to the Mozillians project. Many
of our integration and functional tests have been `automated`_, but automated
tests are best at catching the bugs we can anticipate. Exploratory testing
catches the truly interesting bugs -- the ones we haven’t imagined yet -- and
gives testers an opportunity to learn about the Mozillians project and platform.

  “The main advantage of exploratory testing is that less preparation is needed,
  important bugs are found quickly, and at execution time, the approach tends to
  be more intellectually stimulating than execution of scripted tests.”
  `Wikipedia`_

There are several schools of thought on what `exploratory testing`_ is. For
our purpose we’ll treat it as a testing approach where a tester through
creativity and curiosity seeks to find out how the software works. An
exploratory tester simply looks at and uses the software as a normal user might,
and asks questions on behalf of the users. This approach reveals places where
the software does not behave as expected -- in other words, bugs!

Audience
--------
The Mozillians project targets several different types of users:

- Community members who want to connect with others in the community in order to learn more about them and/or form groups around interests and skills
- Community organizers who want to reach out to groups of people that identify with particular interests
- Developers who want to use the API to power their own applications

Testing
-------

.. image:: /static/images/2013/01/speak_your_mind.jpg
   :align: center
   :alt: Explore!

Your mission if you choose to accept is to creatively explore the Mozillians
`website`_, keeping in mind the users it is intended for. As you work through the
different areas of the application, apply a critical eye to the design, layout,
workflows, and different functionality of the site. If it helps you, keep notes
about what you find, questions you may have, and thoughts about additional
areas you’d like to test.

Here are few places to start:

- Is the site behaving as you expect it to?
- Does the site and user flow behave the same on different devices and web browsers?
- What happens when you pass in unexpected values to the `API`_?

To get started you’ll need:

- Access to `IRC`_ so you can ask questions in `#mozwebqa`_ and `#commtools`_. Stop in and say hello! We’re a friendly group.
- Access to the `staging server`_.
- A vouched Mozillians account: ask in `#mozwebqa`_ or `#commtools`_ to have your account vouched.
- Disposable email addresses so you can create test accounts. I recommend free services like `Mailinator`_ or `10minutemail`_.

Filing Bugs
-----------
On the Mozillians project all defects and feature requests are tracked in
`Bugzilla as bugs`_. Yes! We treat everything as a bug. Not all bugs describe
problems in software; some bugs describe feature requests, and some ask for help.
We simply use Bugzilla as a ticketing system that helps facilitate discussion.

.. image:: /static/images/2013/02/bugzilla.png
   :width: 75%
   :align: center
   :alt: Bugzilla
   :target: https://bugzilla.mozilla.org

As you are testing, the types of bugs that you’ll discover will likely fall into
three categories:

1. Functional regressions in the application
2. Usability problems,
3. New feature suggestions.

Sometimes the issues are `known or even deliberate`_.
If a feature request has been turned down in the past and you feel it should be
incorporated into the application, please file a bug (or ask that a closed one be
reopened) and advocate for that feature.

A few tips for filing bugs:

- Provide as much information as possible so the team (devs & other QA’s) understands the problem or suggested enhancement that you are making.
- Do your best to find and provide clear steps to reproduce to problem, including what browser you used, what URL you were visiting, where you clicked, what you saw, etc. Sometimes a screenshot is a great help.
- Try searching `Bugzilla for the defects`_
- Use `this form`_ to file new bugs

You can always ask us questions if you aren’t sure if what you found should be
entered as a bug.

Please let me know how your testing went. I’d love to hear from you!

mbrandt@mozilla.com

.. _Mozillians project: https://mozillians.org
.. _community phonebook: https://wiki.mozilla.org/Mozillians
.. _automated: https://github.com/mozilla/mozillians-tests
.. _Wikipedia: https://en.wikipedia.org/wiki/Exploratory_testing#Benefits_and_drawbacks
.. _exploratory testing: https://en.wikipedia.org/wiki/Exploratory_testing
.. _website: https://mozillians.org
.. _API: https://wiki.mozilla.org/Mozillians/API-Specification
.. _IRC: https://wiki.mozilla.org/IRC
.. _#mozwebqa: https://widget00.mibbit.com/?settings=1b10107157e79b08f2bf99a11f521973&server=irc.mozilla.org&channel=%23mozwebqa
.. _#commtools: https://widget.mibbit.com/?settings=1b10107157e79b08f2bf99a11f521973&server=irc.mozilla.org&channel=%23commtools
.. _staging server: http://mozillians.allizom.org/
.. _Mailinator: http://mailinator.com/
.. _10minutemail: http://10minutemail.com
.. _Bugzilla as bugs: https://bugzilla.mozilla.org/buglist.cgi?component=Phonebook;product=Community%20Tools;list_id=5698738
.. _known or even deliberate: https://bugzilla.mozilla.org/buglist.cgi?list_id=5698760;resolution=WONTFIX;resolution=WORKSFORME;classification=Other;query_format=advanced;bug_status=RESOLVED;bug_status=VERIFIED;component=Phonebook;product=Community%20Tools
.. _Bugzilla for the defects: https://bugzilla.mozilla.org/query.cgi?classification=Other;query_format=advanced;component=Phonebook;product=Community%20Tools
.. _this form: https://bugzilla.mozilla.org/enter_bug.cgi?product=Community%20Tools&component=Phonebook