#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

# Para producción los URLs son absolutos
SITEURL = 'https://www.pjecz.gob.mx'
SITELOGO = 'https://www.pjecz.gob.mx/theme/images/pjecz.png'
RELATIVE_URLS = False

# Para producción se activa la generacion de feeds
FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'
CATEGORY_FEED_RSS = 'feeds/{slug}.rss.xml'
TAG_FEED_ATOM = None
TAG_FEED_RSS = None
TRANSLATION_FEED_ATOM = None
TRANSLATION_FEED_RSS = None
FEED_MAX_ITEMS = 24
RSS_FEED_SUMMARY_ONLY = True

# Pelican plugins
PLUGIN_PATHS = ['plugins']
PLUGINS = ['pelican_javascript', 'sitemap']
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 1,
        'indexes': 0.5,
        'pages': 1,
    },
    'changefreqs': {
        'articles': 'weekly',
        'indexes': 'daily',
        'pages': 'monthly',
    },
    'exclude': [
        'archives.html',
        'tags.html',
        'categories.html',
        'author/',
    ],
}

# Para producción NO BORRAR todo el directorio de salida
DELETE_OUTPUT_DIRECTORY = False

# Para producción activar el caché
LOAD_CONTENT_CACHE = True

# Para producción SI hay cargas desde Internet
USE_REMOTE_SERVICES = True
