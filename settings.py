#!/usr/bin/env python
# -*- coding: utf-8 -*- #

# ===============
# Basic settings
# ===============
AUTHOR = 'Matt Brandt'
DEFAULT_CATEGORY = 'Blog'
SITENAME = 'Secret Mustache'
SITEURL = 'http://www.secretmustache.com'
SITE_URL = SITEURL
STATIC_PATHS = ['images', ]
TIMEZONE = 'Asia/Singapore'
DEFAULT_LANG = u'en'


# =============
# URL settings
# =============
PERMALINK_STRUCTURE = '{date:%Y}/{date:%m}/'
ARTICLE_URL = '%s{slug}.html' % PERMALINK_STRUCTURE
ARTICLE_LANG_URL = '%s{slug}-{lang}.html' % PERMALINK_STRUCTURE
PAGE_URL = '%spages/{slug}.html' % PERMALINK_STRUCTURE
PAGE_LANG_URL = '%spages/{slug}-{lang}.html' % PERMALINK_STRUCTURE
ARTICLE_SAVE_AS = '%s{slug}.html' % PERMALINK_STRUCTURE
ARTICLE_LANG_SAVE_AS = '%s{slug}-{lang}.html' % PERMALINK_STRUCTURE
PAGE_SAVE_AS = '%spages/{slug}.html' % PERMALINK_STRUCTURE
PAGE_LANG_SAVE_AS = '%spages/{slug}-{lang}.html' % PERMALINK_STRUCTURE


# =============
# Blogroll
# =============
LINKS =  (('mbeb.org', 'http://mbeb.org'),
            ('jcerise', 'http://readmythings.com'),
        )

# =================
# Ordering content
# =================
REVERSE_ARCHIVE_ORDER = True
DEFAULT_PAGINATION = 5


# =================
# Theming
# =================
THEME = 'notmyidea'
#GOOGLE_ANALYTICS = 'UA-XXXX-3'
MENUITEMS = (
    ('Archives', '{0}/archives.html'.format(SITEURL)),
)


# =============
# Social widget
# =============
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),
          )
DISQUS_SITENAME = 'secretmustache'
FLATTR = True
GITHUB_URL = 'https://github.com/m8ttyB/secretmustache'
TWITTER_USERNAME = 'm8ttyb'