# -*- coding: utf-8 -*-
DESCRIPTION = (
    'A pyexcel plugin to render data as handsontable in html pages' +
    ''
)
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
]
intersphinx_mapping = {
    'pyexcel': ('http://pyexcel.readthedocs.io/en/latest/', None),
}
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'

project = u'pyexcel-handsontable'
copyright = u'2015-2017 Onni Software Ltd.'
version = '0.0.1'
release = '0.0.2'
exclude_patterns = []
pygments_style = 'sphinx'
html_theme = 'default'
html_static_path = ['_static']
htmlhelp_basename = 'pyexcel-handsontabledoc'
latex_elements = {}
latex_documents = [
    ('index', 'pyexcel-handsontable.tex',
     'pyexcel-handsontable Documentation',
     'Onni Software Ltd.', 'manual'),
]
man_pages = [
    ('index', 'pyexcel-handsontable',
     'pyexcel-handsontable Documentation',
     [u'Onni Software Ltd.'], 1)
]
texinfo_documents = [
    ('index', 'pyexcel-handsontable',
     'pyexcel-handsontable Documentation',
     'Onni Software Ltd.', 'pyexcel-handsontable',
     DESCRIPTION,
     'Miscellaneous'),
]
