"""LLongName AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 179)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 62)

JSON Source: docs/json/packages/M2_MSR_Documentation_TextModel_LanguageDataModel.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel.language_specific import (
    LanguageSpecific,
)
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class LLongName(LanguageSpecific):
    """AUTOSAR LLongName."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize LLongName."""
        super().__init__()

    def serialize(self) -> ET.Element:
        """Serialize LLongName to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes (L attribute and text)
        parent_elem = super(LLongName, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Copy text from parent element (the blueprint_value content)
        if parent_elem.text is not None:
            elem.text = parent_elem.text

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "LLongName":
        """Deserialize XML element to LLongName object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized LLongName object
        """
        # First, call parent's deserialize to handle inherited attributes (L attribute and text)
        return super(LLongName, cls).deserialize(element)


class LLongNameBuilder:
    """Builder for LLongName."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: LLongName = LLongName()

    def build(self) -> LLongName:
        """Build and return LLongName object.

        Returns:
            LLongName instance
        """
        # TODO: Add validation
        return self._obj