# -*- coding: utf-8 -*-
#
# CRM & Sales Management documentation build configuration file, created by
# sphinx-quickstart on Mon Mar  9 11:55:03 2009.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# The contents of this file are pickled, so don't put values in the namespace
# that aren't pickleable (module imports are okay, they're removed automatically).
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys, os
from docutils import nodes
sys.path.append('../../common')
from conf import *

# General information about the project.
project = u'OpenERP for Manufacturing Management'

# Options for HTML output
# -----------------------

html_title = 'OpenERP for Manufacturing Management'

htmlhelp_basename = 'manufacturing_management_book'

# Options for LaTeX output
# ------------------------

latex_documents = [
   ('index', 'openerp-manufacturing-book.tex', ur'OpenERP for Manufacturing Management', ur'Els Van Vossel\\Fabien Pinckaers', 'manual'),
]

