V2 - a little WebDriver toss in some CraigsList
###############################################
:date: 2010-08-03
:category: Blog
:tags: java, jython, webdriver

So I revisited the code that I originally wrote and did quite a bit of
refactoring along with adding a stats counter that keeps track of pages
visited and results found. The greatest inspiration came when my wife
took interest and wanted to use it to do some job searches of her own,
her only caveat was that she wanted the results to look a *little*
prettier.

My next mini goal is to add the ability to parse arguments from the
command-line so that it becomes a more general purpose tool. I think
that I'll write a Jython wrapper to do this, I really like the
simplicity of Python's `optparse`_ library.

I have this running on a daily cron. Each morning over breakfast I can no
surf a customized set of job results. Yay!

`Git repository`_

.. _optparse: http://docs.python.org/library/optparse.html
.. _Git repository: http://github.com/m8ttyB/JobSearch
