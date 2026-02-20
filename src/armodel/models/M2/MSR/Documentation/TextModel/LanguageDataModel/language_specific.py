"""LanguageSpecific AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 350)

JSON Source: docs/json/packages/M2_MSR_Documentation_TextModel_LanguageDataModel.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel import (
    LEnum,
)
from abc import ABC, abstractmethod


class LanguageSpecific(ARObject, ABC):
    """AUTOSAR LanguageSpecific."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    l: LEnum
    _text: Optional[str]
    def __init__(self) -> None:
        """Initialize LanguageSpecific."""
        super().__init__()
        self.l: LEnum = None
        self._text: Optional[str] = None
    def serialize(self) -> ET.Element:
        """Serialize LanguageSpecific to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize l as XML attribute (not child element)
        if self.l is not None:
            elem.set("L", str(self.l))

        # Serialize text content directly to element text
        if self._text is not None:
            elem.text = self._text

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "LanguageSpecific":
        """Deserialize XML element to LanguageSpecific object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized LanguageSpecific object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse l from XML attribute (not child element)
        l_value = element.get("L")
        if l_value is not None:
            obj.l = l_value

        # Parse text content from element
        if element.text is not None and element.text.strip():
            obj._text = element.text

        return obj



class LanguageSpecificBuilder:
    """Builder for LanguageSpecific."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: LanguageSpecific = LanguageSpecific()

    def build(self) -> LanguageSpecific:
        """Build and return LanguageSpecific object.

        Returns:
            LanguageSpecific instance
        """
        # TODO: Add validation
        return self._obj
