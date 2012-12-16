Modifying DNS for testing/dev
#############################
:date: 2011-06-13 11:21
:category: Blog
:tags: testing, dev

Recently I needed to find the equivalent of /etc/hosts for Win7. I'll be
honest, my first attempt at poking around Windows was a complete flop. I
haven't worked in a Windows environment in years and I can't claim that
I was a power user at that time (even remotely).

Let me quickly get to the point of this post, on Win7 there exists a
hosts file. I was pleasantly surprised that it functions the same as
/etc/hosts on Linux.

::

    C:WINDOWS\system32\driverset\hosts

Simply update the with the *hosts* file with the paths that your need:

::

    ##
    # Host Database
    #
    # localhost is used to configure the loopback interface
    ### added for testing purposes
    63.245.217.71   thisisnotmarkup.mozilla.org
    127.0.0.1       expectpants.com# don't touch
    127.0.0.1   localhost
    255.255.255.255 broadcasthost

And test/dev away!

References: - `Krzysztof Kowalczyk`_

.. _Krzysztof Kowalczyk: http://blog.kowalczyk.info/article/Local-DNS-modifications-on-Windows-etchosts-equi.html
