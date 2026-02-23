"""MultilanguageLongName AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 179)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 163)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 62)

JSON Source: docs/json/packages/M2_MSR_Documentation_TextModel_MultilanguageData.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization.decorators import lang_prefix

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel.l_long_name import (
    LLongName,
)


class MultilanguageLongName(ARObject):
    """AUTOSAR MultilanguageLongName."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _l4: list[LLongName]
    def __init__(self) -> None:
        """Initialize MultilanguageLongName."""
        super().__init__()
        self._l4: list[LLongName] = []
    @property
    @lang_prefix("L-4")
    def l4(self) -> list[LLongName]:
        """Get l4 with language-specific wrapper."""
        return self._l4

    @l4.setter
    def l4(self, value: list[LLongName]) -> None:
        """Set l4 with language-specific wrapper."""
        self._l4 = value

    def serialize(self) -> ET.Element:
        """Serialize MultilanguageLongName to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # First, call parent's serialize to handle inherited attributes (timestamp and checksum)
        parent_elem = super(MultilanguageLongName, self).serialize()

        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize l4 (list to container "L-4")
        if self._l4:
            for item in self._l4:
                # Create L-4 element with L attribute from LLongName
                wrapper = ET.Element("L-4")
                if item.l is not None:
                    wrapper.set("L", str(item.l))
                # Copy text content from LLongName
                if item._text is not None:
                    wrapper.text = item._text
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "MultilanguageLongName":
        """Deserialize XML element to MultilanguageLongName object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized MultilanguageLongName object
        """
        # First, call parent's deserialize to handle inherited attributes (timestamp and checksum)
        obj = super(MultilanguageLongName, cls).deserialize(element)

        # Deserialize l4 list from L-4 elements
        obj._l4 = []
        for child in element:
            if SerializationHelper.strip_namespace(child.tag) == "L-4":
                # Create LLongName item from L-4 element
                l4_item = LLongName()
                # Extract L attribute
                l_value = child.get("L")
                if l_value is not None:
                    l4_item.l = l_value
                # Extract text content
                if child.text is not None and child.text.strip():
                    l4_item._text = child.text
                obj._l4.append(l4_item)

        return obj



class MultilanguageLongNameBuilder:
    """Builder for MultilanguageLongName."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: MultilanguageLongName = MultilanguageLongName()

    def build(self) -> MultilanguageLongName:
        """Build and return MultilanguageLongName object.

        Returns:
            MultilanguageLongName instance
        """
        # TODO: Add validation
        return self._obj
