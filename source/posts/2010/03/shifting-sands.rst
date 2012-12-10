Shifting sands
##############
:date: 2010-03-20 17:03
:category: Blog
:tags: life, testing, work

Yesterday (Friday) I received an email from a project manger announcing
the dissolution of the team that I'm on and that we are to
be assimilated by the b0rg or the developer teams in our department. You
see the teams need help meeting their customer deliverables and our
little 3 person test automation team decidedly knows how to and enjoys
coding.

Many of you at this point I suspect will laugh at me, the little (or
big) voice in your head will say "oh but the places I've been, this
young whipper-snapper will see many more of these in his lifetime." I am
aware this phenomena, it is industry non-discriminate. I come from a
psychology background and have worked in homeless shelters, youth
detention centers, health clinics in 3rd world countries, etc; I
understand the importance of teams that are dynamic and able to handle
the immediate need.

A little history, 2-years ago I jumped on the test-automation horse as
an intern. At first the prospect of working as a tester scared me, would
I forever be labeling myself as a tester and axe any future career moves
to work as developer on teams? One of my loves is developing and writing
code and I didn't want to inadvertently limit the scope of future
employment opportunities.  A few old-timers in the department even went
so far as to warn me that their 25+ year careers had been shoe horned
into the testing category because of early decisions they had made when
they were fresh from the ranks of college.

A couple of items I've learned in the last 2-years:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. I'm a stickler for quality - I love driving innovation through
   quality practices.  Agile, XP, pair programming, TDD,
   continuous integration, etc.  The quicker a problem is discovered the
   cheaper it is to fix. Siloing of knowledge is just plain bad for a
   team and a product.
#. Breadth of knowledge - I have had broad access to the systems we test
   and understand nuances and aspects of our products that evade some of
   the developers because of their macro-expertise.
#. Creativity - Writing automation harnesses & frameworks is a
   challenging and *ubber::fun* process. Answering the question of how
   do we test X without re-implementing the functionality of X leads to
   very diverse and important conversations with teammates. This leads
   to understanding how the product works (or should) from multiple
   points of view: customer proxies, architects, developers, manual
   testers, mangers, pms, spouses, etc (I know I'm leaving a few people
   out). The point being that to automate the testing of X extension or
   product you need to be able to integrate all of these perspectives
   and then decidedly take your own road towards how to automate a
   testing solution targeting the highest areas of risk.
#. Give me a Volkswagen not a Cadillac - Ultimately give me the right
   amount of bang for the buck. A team member who I love to argue with
   always pushes for the simplest solution to solve the problem. Distill
   the essence of the problem and don't gold plate the solution, you
   don't know what you don't know so don't plan for it.
#. Sometimes you want more than a VW Bug - In conversations with
   teammates I changed the previous analogy to taking a single-speed
   bike and turning it into a 21-speed. Usually after riding a single
   speed bike you quickly start to see a pattern for the type of terrain
   that your attempting to negotiate, at that point it might be time to
   refactor your approach and your code. I recently spent some time
   automating testing on a few database centric extensions and I started
   to notice a pattern in the approach I was taking at testing these
   scenarios. After 2-weeks of fiddling with a new approach in-between
   deliverables my *dbtester* framework was born. Instead of it taking
   me several hours to churn out a database related test it now takes me
   a quick 15-minutes to script a new test.
#. Bolt on a motor to your 21-speed bike - The team liked the testing
   approach I took with the database scenarios and we're now taking what
   we learned from my experiment and are refactoring our other
   frameworks to more closely follow this paradigm shift.

.. raw:: html

   </p>

