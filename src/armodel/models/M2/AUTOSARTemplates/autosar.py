"""AUTOSAR root element - singleton pattern."""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from lxml import etree


class AUTOSAR(ARObject):
    """AUTOSAR root element representing the entire ARXML document.

    This class implements the singleton pattern - there is only one
    AUTOSAR instance per document.
    """

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        """Initialize AUTOSAR singleton."""
        if hasattr(self, "_initialized"):
            return
        super().__init__()
        self._initialized = True
        # Splitable elements (top-level children)
        self.ar_packages: list = []
        self.administrative_data: list = []

    def get_splitable_elements(self) -> list:
        """Get all splitable child elements.

        Returns:
            List of splitable elements
        """
        splitable = []
        for elem in self.ar_packages:
            if getattr(elem, "is_splitable", False):
                splitable.append(elem)
        return splitable

    def serialize(self) -> etree.Element:
        """Convert AUTOSAR to XML element.

        Returns:
            XML element representing this document
        """
        from lxml import etree
        element = etree.Element("AUTOSAR")
        element.set("xmlns", "http://autosar.org/schema/r4.0")

        # TODO: Serialize child elements

        return element
