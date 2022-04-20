# Copyright (c) 2010-2021 openpyxl


import openpyxl._constants as constants
from openpyxl.compat.numbers import NUMPY
from openpyxl.reader.excel import load_workbook
from openpyxl.reader.excel import load_workbook as open
from openpyxl.workbook import Workbook
from openpyxl.xml import DEFUSEDXML, LXML

# Expose constants especially the version number

__author__ = constants.__author__
__author_email__ = constants.__author_email__
__license__ = constants.__license__
__maintainer_email__ = constants.__maintainer_email__
__url__ = constants.__url__
__version__ = constants.__version__
