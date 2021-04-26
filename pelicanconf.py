#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import datetime
from collections import namedtuple

import os

AUTHOR = 'Descomplicando a Docência'
SITENAME = 'Descomplicando a Docência'
SITEURL = '{}'.format(os.getenv('SITEURL', 'http://localhost:{}'.format(os.getenv('PORT', '8000'))))
DEFAULT_DATE_FORMAT = ('%d-%m-%Y')
DEFAULT_BG = 'images/Logomarca.png'
SINCE = datetime.now().year
NOW = datetime.now().date()
SUMMARY_MAX_LENGTH = 100

NEST_HEADER_LOGO = '/images/logotipo.png'

#Menu
MENUITEMS = (
    ('Sobre', '/sobre'),
    ('Equipe', '/equipe'),
    ('Blog', '/archives.html'),
    ('Contato', '/contato')
)

# pagination.html
NEST_PAGINATION_PREVIOUS = u'Anterior'
NEST_PAGINATION_NEXT = u'Próximo'

# index.html
NEST_INDEX_HEAD_TITLE = u'Início'
NEST_INDEX_HEADER_TITLE = u'Impulsionando a Inovação Pedagógica'
NEST_INDEX_HEADER_SUBTITLE = u'E promovendo as transformações educacionais!'
NEST_INDEX_CONTENT_TITLE = u'Publicações Recentes'

# archives.html
NEST_ARCHIVES_HEAD_TITLE = u'Arquivos'
NEST_ARCHIVES_HEAD_DESCRIPTION = u'Arquivos'
NEST_ARCHIVES_HEADER_TITLE = u'Arquivos'
NEST_ARCHIVES_HEADER_SUBTITLE = u'Arquivos de todas as publicações'
NEST_ARCHIVES_CONTENT_TITLE = u'Arquivos'

# article.html
NEST_ARTICLE_HEADER_BY = u'de'
NEST_ARTICLE_HEADER_MODIFIED = u'modificado'
NEST_ARTICLE_HEADER_IN = u'na categoria'

# author.html
NEST_AUTHOR_HEAD_TITLE = u'Publicado por'
NEST_AUTHOR_HEAD_DESCRIPTION = u'Publicado por'
NEST_AUTHOR_HEADER_SUBTITLE = u'suas publicações'
NEST_AUTHOR_CONTENT_TITLE = u'Publicações'

# authors.html 
NEST_AUTHORS_HEAD_TITLE  =  u'Lista de Autores' 
NEST_AUTHORS_HEAD_DESCRIPTION  =  u'Lista de Autores' 
NEST_AUTHORS_HEADER_TITLE  =  u'Lista de Autores' 
NEST_AUTHORS_HEADER_SUBTITLE  =  u'Arquivos listados por autor'

# categorias.html 
NEST_CATEGORIES_HEAD_TITLE  = u'Categorias' 
NEST_CATEGORIES_HEAD_DESCRIPTION  =  u'Arquivos listados por categoria ' 
NEST_CATEGORIES_HEADER_TITLE  =  u'Categorias' 
NEST_CATEGORIES_HEADER_SUBTITLE  =  u'Arquivos listados por categoria' 

# category.html 
NEST_CATEGORY_HEAD_TITLE  =  u'Arquivo da categoria ' 
NEST_CATEGORY_HEAD_DESCRIPTION  =  u'Arquivo da categoria' 
NEST_CATEGORY_HEADER_TITLE  =  u' Categoria ' 
NEST_CATEGORY_HEADER_SUBTITLE  =  u'Arquivo da categoria' 

# tag.html 
NEST_TAG_HEAD_TITLE  =  u'Tag arquivos '
NEST_TAG_HEAD_DESCRIPTION  =  u'Tag arquivos ' 
NEST_TAG_HEADER_TITLE  =  u'Tag' 
NEST_TAG_HEADER_SUBTITLE  =  u'Tag arquivos ' 

# tags.html 
NEST_TAGS_HEAD_TITLE =  u'Tags' 
NEST_TAGS_HEAD_DESCRIPTION  =  u'Lista de Tags ' 
NEST_TAGS_HEADER_TITLE  =  u'Tags' 
NEST_TAGS_HEADER_SUBTITLE  = u'Lista de Tags' 
NEST_TAGS_CONTENT_TITLE  =  u'Lista de Tags ' 
NEST_TAGS_CONTENT_LIST  =  u'tagged'

#Footer
NEST_SITEMAP_COLUMN_TITLE = u'Mapa do site'
NEST_SITEMAP_MENU = [('Arquivo', '/archives.html'),('Tags','/tags.html'), ('Categorias', '/categories.html'), ('Autores','/authors.html')]
NEST_SITEMAP_ATOM_LINK = u'Atom Feed'
NEST_SITEMAP_RSS_LINK = u'RSS Feed'
NEST_SOCIAL_COLUMN_TITLE = u'Social'
NEST_LINKS_COLUMN_TITLE = u'Areas' 
NEST_COPYRIGHT = u'Exceto onde indicado de outra forma, todos os conteúdos neste site essão licenciados sob licença Creative Commons Atribuição Compartilhe Igual 4.0'


ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{}index.html'.format(ARTICLE_URL)

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
TAGS_URL = 'tag/{slug}.html'
CATEGORY_URL = 'category/{slug}.html'

# Sitemap
'''DIRECT_TEMPLATES = ('index', 'tags', 'categories', 'archives', 'sitemap')
SITEMAP_SAVE_AS = 'sitemap.xml'
'''

PATH = 'content'

TIMEZONE = 'America/Campo_Grande'

DEFAULT_LANG = 'en'
THEME = 'themes/nest'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True
DELETE_OUTPUT_DIRECTORY = True

# Blogroll
LINKS = (('Ciências Humanas', '/category/ciencias_humanas.html'), ('Ciências Naturais', '/category/ciencias_naturais.html'), ('Linguagem', '/category/linguagem.html'), ('Matemática', '/category/matematica.html'), ('Educação Inclusiva', '/category/educacao_inclusiva.html'), ('Gestão Escolar', '/category/gestao_escolar.html'), ('Coodernação Pedagógica', '/category/coodernacao_pedagogica.html'))

# Social widget
SOCIAL = (('Linkedin', 'https://www.linkedin.com/company/descomplicandoadocencia/'),
          ('Facebook', 'https://www.facebook.com/descomplicandoadocencia'),
          ('Github', 'https://github.com/descomplicandoadocencia'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = ['images', 'extra/robots.txt', 'extra/favicon.ico']
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    }

DEFAULT_METADATA = {
    'status': 'draft',
}    

DISQUS_SITENAME = 'descomplicandoadocencia'