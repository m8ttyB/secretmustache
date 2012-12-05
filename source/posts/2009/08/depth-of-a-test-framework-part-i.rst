A test framework
################
:date: 2009-08-22 11:05
:category: Blog
:tags: testing

If we think of a working system as layers of abstractions, at what depth
within that system should a test engineer consider exposing when
targeting functional testing? Or more concisely are the trade-offs of
*touching*\ a system at the *lower*\ places within the architecture
valid arguments for lowering risk to an acceptable level? Is this
creating too much overhead? Would an existing framework such as
WebDriver be a sufficient wrapper for driving functional testing?

Exposing your services:
~~~~~~~~~~~~~~~~~~~~~~~

I'm working with a small group of people to automate what has been a
very manual process of regression & integration testing. Ultimately
testing has (and is) historically meant a tester (developers too) drives
the application via our web gui and checks for state changes in the gui.
They may also dip into the back-end from time to time via ssh to look at
file creation/change/deletion along with the database for additional
expected changes. The entire application is browser driven.

.. raw:: html

   </p>

One solution involves the extension of the current system. Plopping a
xml-rpc server into our existing application architecture and exposing
existing services within that application. This of course could have
some interesting and not too unpleasant implications outside of our
little test group.

.. figure:: http://freecog.com/wp-content/uploads/2009/08/RPCDiagram.jpg
   :align: center
   :alt: RPC Diagram

   RPC Diagram
By way of driving the application from this layer we can quickly assess
whether core components are working correctly or if recently integrated
code changes have changed or broken underlying contracts. From the
standpoint of someone who enjoys writing code to accomplish and overcome
challenges this is a fun project. However I can't help but feel a small
twinge of fear because we're completely ignoring the gui. The gui is the
one and only path that the user/customer will ever interact with.

There is a defined split in philosophies; a vocal group believing that
stability beneath the viewable presentation layer is the most vital and
a second and quieter group mumbling... "what about the presentation
layer?"

WebDriver or Selenium (or Watir or ... x):
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

... a future section.

.. raw:: html

   </p>

Definitions:

-  Regression - "... any type of `software testing`_ which seeks to
   uncover `software regressions`_. Such regressions occur whenever
   software functionality that was previously working correctly, stops
   working as intended. Typically regressions occur as an `unintended
   consequence`_ of program changes. *Common methods* of regression
   testing include re-running previously run tests and checking whether
   previously fixed faults have re-emerged." (`more`_)
-  Integration - "... is the activity\ :sup:``[1]`_` of `software
   testing`_ in which individual software modules are combined and
   tested as a group. It occurs after `unit testing`_ and before `system
   testing`_." (`more`_)

.. raw:: html

   </p>

.. _software testing: http://en.wikipedia.org/wiki/Software_testing
.. _software regressions: http://en.wikipedia.org/wiki/Software_regression
.. _unintended consequence: http://en.wikipedia.org/wiki/Unintended_consequence
.. _more: http://en.wikipedia.org/wiki/Regression_test
.. _[1]: http://en.wikipedia.org/wiki/Integration_test#cite_note-0
.. _unit testing: http://en.wikipedia.org/wiki/Unit_testing
.. _system testing: http://en.wikipedia.org/wiki/System_testing
.. _more: http://en.wikipedia.org/wiki/Integration_test
