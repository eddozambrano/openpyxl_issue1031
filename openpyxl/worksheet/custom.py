# Autogenerated schema
from openpyxl.descriptors import Sequence, String
from openpyxl.descriptors.serialisable import Serialisable

# can be done with a nested sequence


class CustomProperty(Serialisable):

    tagname = "customProperty"

    name = String()

    def __init__(
        self,
        name=None,
    ):
        self.name = name


class CustomProperties(Serialisable):

    tagname = "customProperties"

    customPr = Sequence(expected_type=CustomProperty)

    __elements__ = ("customPr",)

    def __init__(
        self,
        customPr=(),
    ):
        self.customPr = customPr
