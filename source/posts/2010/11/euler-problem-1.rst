Euler problem #1
################
:date: 2010-11-23 21:35
:category: Blog
:tags: Euler, Python

Inspired by a conversation with a few people on twitter I came up with a
mind-map laying out a personal syllabus of learning goals. I've been out
of school for a few months and I have a sinking feeling that I'd better
keep my gears turning or the proverbial *"use it or lose it..."* bit
will completely grab me with its forgetfulness.

One of the branches or areas that I want to keep fresh is algorithm
evaluation. Its also an area of weakness for me. Its been at least two
years since I had a class that focused on BigO notation or on speed,
I've never taken a formal algorithms class, and lastly on a professional
note I've never seen anyone do an analysis on a performance problem
using anything other than capturing run times in a log. From my
experience developers sprinkle log captures throughout their code in
areas they *think* are bottlenecks.

Professionally I haven't seen a discussion/analysis on why certain bits
of code are faster or slower other than watching developers do it by
trial and error. This next bit is taken from `Project Euler`_. I've
done two implementations. Can you see why one might run faster than the
other?

**Example**: If we list all the natural numbers below 10 that are
multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is
23. (`Problem #1`_)

**Question:** Find the sum of all the multiples of 3 or 5 below 1000.

*Assumption if we input 16 the multiples are: 3, 5, 6, 9, 10, 12, 15,
15*

::

    def multiple1(limit):
        count = 0
        for i in range(1, limit):
            if (i % 3) is 0:
                count += i
            if (i % 5) is 0:
                count += i
        return count

Let's run the first algorithm with a value of 10,000,000.

::

    ordo-grande:Desktop matt$ time ./play.py 1000000
    the answer is: 266666333333
    real    0m0.423s
    user    0m0.373s
    sys 0m0.047s

And now the second algorithm.

::

    def multiple2(limit):
        count = 0
        for i in range(3, limit, 3):
            count += i
        for i in range(5, limit, 5):
            count += i
        return count

::

    ordo-grande:Desktop matt$ time ./play.py 1000000
    the answer is: 266666333333
    real    0m0.104s
    user    0m0.083s
    sys 0m0.018s

I drew up these two methods on the whiteboard in my team room yesterday
along with the problem declaration. Note, I didn't include the run
times.  I asked my team which method was more efficient and over half
the team guessed wrong. I won't spell out the discussion or the
evaluation of the two examples, but can you see why one is
faster/more efficientthan the other?

.. _Project Euler: http://projecteuler.net
.. _Problem #1: http://projecteuler.net/index.php?section=problems&id=1
