# Copyright (c) 2010-2021 openpyxl

from openpyxl.descriptors import Sequence
from openpyxl.descriptors.excel import Relation
from openpyxl.descriptors.serialisable import Serialisable


class ExternalReference(Serialisable):

    tagname = "externalReference"

    id = Relation()

    def __init__(self, id):
        self.id = id
