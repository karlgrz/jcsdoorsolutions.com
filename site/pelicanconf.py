#!/usr/bin/env python
# -*- coding: utf-8 -*- #
import os

AUTHOR = u'JCSDoorSolutions'

SITENAME = u'JCS Door Solutions'
SITESUBTITLE = u'Garage Door Rescue and Repair Carpentersville, IL Garage Doors and Openers'
SITEURL = '' # change in publishconf.py

# Times and dates
DEFAULT_DATE_FORMAT = '%b %d, %Y'
TIMEZONE = 'US/Central'
DEFAULT_LANG = u'en'

# Set the article URL
ARTICLE_URL = '{slug}/'
ARTICLE_SAVE_AS = '{slug}/index.html'

# Set the page URL
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'

# Title menu options
MENUITEMS = [('Archives', '/archives.html'), ('CHI Overhead Doors', 'http://chiohd.com'), ('Liftmaster', 'http://liftmaster.com'), ('Homes by OTTO', 'http://homesbyotto.com')]

#Github include settings
#GITHUB_USER = 'jcsdoorsolutions'
#GITHUB_REPO_COUNT = 5 
#GITHUB_SKIP_FORK = True
#GITHUB_SHOW_USER_LINK = True

# Blogroll
#LINKS =  (('Pelican', 'http://docs.notmyidea.org/alexis/pelican/'),
#          ('Python.org', 'http://python.org'),
#          ('Jinja2', 'http://jinja.pocoo.org'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
#SOCIAL = ('twitter: @jcsdoorsolutions', 'http://twitter.com/jcsdoorsolutions')

DEFAULT_PAGINATION = 5 

# STATIC_OUT_DIR requires https://github.com/jakevdp/pelican/tree/specify-static
#STATIC_OUT_DIR = ''
#STATIC_PATHS = ['images', 'figures', 'downloads']
#FILES_TO_COPY = [('favicon.png', 'favicon.png')]

# This requires Pelican 3.3+
STATIC_PATHS = ['images', 'favicon.ico']

CODE_DIR = 'downloads/code'
NOTEBOOK_DIR = 'downloads/notebooks'

# Theme and plugins
#  Theme requires http://github.com/duilio/pelican-octopress-theme/
#  Plugins require http://github.com/getpelican/pelican-plugins/
THEME = os.path.join('theme')
PLUGIN_PATH = os.path.join('plugins')
PLUGINS = ['summary']

SHOW_SUMMARY = False

# The theme file should be updated so that the base header contains the line:
#
#  {% if EXTRA_HEADER %}
#    {{ EXTRA_HEADER }}
#  {% endif %}
# 

# Sharing
#TWITTER_USER = 'jcsdoorsolutions'
#GOOGLE_PLUS_USER = '+JCSDoorSolutions'
#GOOGLE_PLUS_ONE = True 
#GOOGLE_PLUS_HIDDEN = False
#FACEBOOK_LIKE = True
#TWITTER_TWEET_BUTTON = True 
#TWITTER_LATEST_TWEETS = False 
#TWITTER_FOLLOW_BUTTON = True 
#TWITTER_TWEET_COUNT = 3
#TWITTER_SHOW_REPLIES = 'false'
#TWITTER_SHOW_FOLLOWER_COUNT = 'false'

# RSS/Atom feeds
FEED_DOMAIN = SITEURL
FEED_ATOM = 'atom.xml'


# Search
SEARCH_BOX = True
