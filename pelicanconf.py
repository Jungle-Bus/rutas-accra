#!/usr/bin/env python
# -*- coding: utf-8 -*- #

from __future__ import unicode_literals

AUTHOR = u'Jungle Bus'
SITENAME = u'Jungle Bus in Accra'
SITESUBTITLE = 'Find your trotro'
SITEDESCRIPTION = 'A very good map made from OSM'
SITEKEYWORDS = 'Bus, Buses, Rutas, Ruta, IRTRAMMA, TUC, Transporte, Transporte Urbano Colectivo, Nicaragua, Managua, CpenStreetMap, Transporte público, Datos Abuertos, Open Data'

USE_LESS = True
SITEURL = '//junglebus.io/accra'
SITELOGO = '/accra/images/jungle_bus_logo.png'
THEME = 'themes/mombacho'

FAVICON = '/accra/images/favicon.ico'
ROBOTS = 'index, follow'

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

AUTHOR_SAVE_AS = False
CATEGORY_SAVE_AS = False
TAG_SAVE_AS = False
ARCHIVES_SAVE_AS = False
DIRECT_TEMPLATES = ('index', 'embed')

CC_LICENSE = { 'name': 'Creative Commons Attribution-ShareAlike', 'version':'4.0', 'slug': 'by-sa' }

PATH = 'content'
STATIC_PATHS = ['images','php']

TIMEZONE = 'Africa/Accra'

DEFAULT_LANG = u'en'
OG_LOCALE = u'es_NI'
DEFAULT_DATE_FORMAT = ('%d %B %Y')

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
FEED_ALL_RSS = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social widget
SOCIAL = (('email', 'mailto:contact@junglebus.io'),
          ('twitter', 'http://www.twitter.com/BusJungle'),
          )

MENUITEMS = ()

DEFAULT_PAGINATION = False
