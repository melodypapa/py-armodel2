"""MultiLanguageParagraph AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 290)

JSON Source: docs/json/packages/M2_MSR_Documentation_TextModel_MultilanguageData.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel2.serialization.decorators import lang_prefix

from armodel2.models.M2.MSR.Documentation.BlockElements.PaginationAndView.paginateable import (
    Paginateable,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel2.models.M2.MSR.Documentation.TextModel.LanguageDataModel.l_paragraph import (
    LParagraph,
)


class MultiLanguageParagraph(Paginateable):
    """AUTOSAR MultiLanguageParagraph."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    help_entry: Optional[String]
    _l1: list[LParagraph]
    def __init__(self) -> None:
        """Initialize MultiLanguageParagraph."""
        super().__init__()
        self.help_entry: Optional[String] = None
        self._l1: list[LParagraph] = []
    @property
    @lang_prefix("L-1")
    def l1(self) -> list[LParagraph]:
        """Get l1 with language-specific wrapper."""
        return self._l1

    @l1.setter
    def l1(self, value: list[LParagraph]) -> None:
        """Set l1 with language-specific wrapper."""
        self._l1 = value


    def serialize(self) -> ET.Element:
        """Serialize MultiLanguageParagraph to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(MultiLanguageParagraph, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize help_entry
        if self.help_entry is not None:
            serialized = SerializationHelper.serialize_item(self.help_entry, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("HELP-ENTRY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize l1 (list with l_prefix "L-1")
        for item in self.l1:
            serialized = SerializationHelper.serialize_item(item, "LParagraph")
            if serialized is not None:
                # For l_prefix lists, wrap each item in the l_prefix tag
                wrapped = ET.Element("L-1")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "MultiLanguageParagraph":
        """Deserialize XML element to MultiLanguageParagraph object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized MultiLanguageParagraph object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(MultiLanguageParagraph, cls).deserialize(element)

        # Parse help_entry
        child = SerializationHelper.find_child_element(element, "HELP-ENTRY")
        if child is not None:
            help_entry_value = child.text
            obj.help_entry = help_entry_value

        # Parse l1 (list with l_prefix "L-1")
        obj.l1 = []
        for child in SerializationHelper.find_all_child_elements(element, "L-1"):
            l1_value = SerializationHelper.deserialize_by_tag(child, "LParagraph")
            obj.l1.append(l1_value)

        return obj



class MultiLanguageParagraphBuilder:
    """Builder for MultiLanguageParagraph."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: MultiLanguageParagraph = MultiLanguageParagraph()

    def build(self) -> MultiLanguageParagraph:
        """Build and return MultiLanguageParagraph object.

        Returns:
            MultiLanguageParagraph instance
        """
        # TODO: Add validation
        return self._obj
