"""Xdoc AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 319)

JSON Source: docs/json/packages/M2_MSR_Documentation_TextModel_InlineTextElements.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.single_language_referrable import (
    SingleLanguageReferrable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    DateTime,
    String,
)


class Xdoc(SingleLanguageReferrable):
    """AUTOSAR Xdoc."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    date: Optional[DateTime]
    number: Optional[String]
    position: Optional[String]
    publisher: Optional[String]
    state: Optional[String]
    url: Optional[Any]
    def __init__(self) -> None:
        """Initialize Xdoc."""
        super().__init__()
        self.date: Optional[DateTime] = None
        self.number: Optional[String] = None
        self.position: Optional[String] = None
        self.publisher: Optional[String] = None
        self.state: Optional[String] = None
        self.url: Optional[Any] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "Xdoc":
        """Deserialize XML element to Xdoc object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Xdoc object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse date
        child = ARObject._find_child_element(element, "DATE")
        if child is not None:
            date_value = child.text
            obj.date = date_value

        # Parse number
        child = ARObject._find_child_element(element, "NUMBER")
        if child is not None:
            number_value = child.text
            obj.number = number_value

        # Parse position
        child = ARObject._find_child_element(element, "POSITION")
        if child is not None:
            position_value = child.text
            obj.position = position_value

        # Parse publisher
        child = ARObject._find_child_element(element, "PUBLISHER")
        if child is not None:
            publisher_value = child.text
            obj.publisher = publisher_value

        # Parse state
        child = ARObject._find_child_element(element, "STATE")
        if child is not None:
            state_value = child.text
            obj.state = state_value

        # Parse url
        child = ARObject._find_child_element(element, "URL")
        if child is not None:
            url_value = child.text
            obj.url = url_value

        return obj



class XdocBuilder:
    """Builder for Xdoc."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Xdoc = Xdoc()

    def build(self) -> Xdoc:
        """Build and return Xdoc object.

        Returns:
            Xdoc instance
        """
        # TODO: Add validation
        return self._obj
