secretmustach.com
===================

This is the repository for my blog [secretmustache.com]. It uses [Pelican], a static blog generator written in [Python].

If you find errors or would like to submit amendments to my blog (or even submit an article), I would be more than happy to merge your pull request. Simply submit patches to the .md and .rst files. Don't worry about generating the .html output with [Pelican].

The following [contributors] have submitted pull requests to [secretmustache.com].

### Setting up a Python env
If you want to play with the code locally you'll need to do a bit of setup. You will need to have [Python] 2.6 installed (or a newer, stable version).

Run

    easy_install pip

followed by

    sudo pip install -r requirement.txt

If you're new to [Python] you may want to explore [virtualenv] to isolate your [Python] applications (their libraries) from one another. If you think [virtualenv] is nifty consider using [virtualenvwrapper] in conjunction with it. [virtualenvwrapper] provides a bunch of very handy tools imho.

__note__

If you are running on Ubuntu/Debian you will need to do the following first to install the required [Python] libraries.

    sudo apt-get install python-setuptools

Setting up a dev environment in Windows is a bit more complex; there are several good articles you can find using a search engine like [Google]. This is beyond the scope of this readme (I don't have a Windows environment). Patches welcome if you want help with this readme :-)

License
-------
This software is licensed under the [MPL] 2.0:

    This Source Code Form is subject to the terms of the Mozilla Public
    License, v. 2.0. If a copy of the MPL was not distributed with this
    file, You can obtain one at http://mozilla.org/MPL/2.0/.

[secretmustache.com]: http:www.secretmustache.com/
[Pelican]: https://github.com/getpelican/pelican
[Python]: http://www.python.org/
[contributors]: https://github.com/m8ttyb/secretmustache/contributors
[virtualenv]: http://www.virtualenv.org/
[virtualenvwrapper]: http://www.doughellmann.com/projects/virtualenvwrapper/
[Google]: http://lmgtfy.com/?q=how+to+install+windows+python+easy_install
[MPL]: http://www.mozilla.org/MPL/2.0/