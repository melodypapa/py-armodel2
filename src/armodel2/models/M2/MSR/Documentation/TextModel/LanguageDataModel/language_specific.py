"""LanguageSpecific AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 350)

JSON Source: docs/json/packages/M2_MSR_Documentation_TextModel_LanguageDataModel.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.models.M2.MSR.Documentation.TextModel.LanguageDataModel import (
    LEnum,
)
from armodel2.serialization import SerializationHelper
from abc import ABC, abstractmethod


class LanguageSpecific(ARObject, ABC):
    """AUTOSAR LanguageSpecific."""

    _XML_TAG = "LANGUAGE-SPECIFIC"

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
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes (checksum, timestamp)
        parent_elem = super(LanguageSpecific, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

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
        obj = cls.__new__(cls)  # type: ignore
        obj.__init__()

        # Call parent deserialize for common fields
        super(LanguageSpecific, cls).deserialize(element)

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