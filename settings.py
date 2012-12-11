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
STATIC_PATHS = ['images',]
TIMEZONE = 'America/Los_Angeles'
DEFAULT_LANG = u'en'
MAIL_USERNAME = 'matt'
MAIL_HOST = 'thebrandts.org'


# =============
# URL settings
# =============
PERMALINK_STRUCTURE = '{date:%Y}/{date:%m}/'
ARTICLE_URL = '%s{slug}.html' % PERMALINK_STRUCTURE
PAGE_URL = '%spages/{slug}.html' % PERMALINK_STRUCTURE
ARTICLE_SAVE_AS = '%s{slug}.html' % PERMALINK_STRUCTURE
ARTICLE_LANG_SAVE_AS = '%s{slug}-{lang}.html' % PERMALINK_STRUCTURE


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
THEME = 'secretmustache-theme'
#GOOGLE_ANALYTICS = 'UA-XXXX-3'
SECTIONS = [('Blog', 'index.html'),
        ('Archive', 'archives.html'),
        ('Tags', 'tags.html'),
        #('Projects', 'pages/projects.html'),
        #('Talks', 'pages/talks.html'),
        ('About', 'pages/about.html')
        ]


# =============
# Social widget
# =============
DISQUS_SITENAME = 'secretmustache'
FLATTR = True
GITHUB_URL = 'https://github.com/m8ttyB'
LINKEDIN_URL = 'http://www.linkedin.com/in/mlbrandt'
TWITTER_USERNAME = 'm8ttyb'
