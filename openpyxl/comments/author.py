# Copyright (c) 2010-2021 openpyxl


from openpyxl.descriptors import Alias, Sequence
from openpyxl.descriptors.serialisable import Serialisable


class AuthorList(Serialisable):

    tagname = "authors"

    author = Sequence(expected_type=str)
    authors = Alias("author")

    def __init__(
        self,
        author=(),
    ):
        self.author = author
