"""DefItem AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 298)

JSON Source: docs/json/packages/M2_MSR_Documentation_BlockElements_ListElements.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView.paginateable import (
    Paginateable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)

if TYPE_CHECKING:
    from armodel.models.M2.MSR.Documentation.BlockElements.documentation_block import (
        DocumentationBlock,
    )



class DefItem(Paginateable):
    """AUTOSAR DefItem."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def_: DocumentationBlock
    help_entry: Optional[String]
    def __init__(self) -> None:
        """Initialize DefItem."""
        super().__init__()
        self.def_: DocumentationBlock = None
        self.help_entry: Optional[String] = None

    def serialize(self) -> ET.Element:
        """Serialize DefItem to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DefItem, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize def_
        if self.def_ is not None:
            serialized = ARObject._serialize_item(self.def_, "DocumentationBlock")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DEF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize help_entry
        if self.help_entry is not None:
            serialized = ARObject._serialize_item(self.help_entry, "String")
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

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DefItem":
        """Deserialize XML element to DefItem object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DefItem object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DefItem, cls).deserialize(element)

        # Parse def_
        child = ARObject._find_child_element(element, "DEF")
        if child is not None:
            def__value = ARObject._deserialize_by_tag(child, "DocumentationBlock")
            obj.def_ = def__value

        # Parse help_entry
        child = ARObject._find_child_element(element, "HELP-ENTRY")
        if child is not None:
            help_entry_value = child.text
            obj.help_entry = help_entry_value

        return obj



class DefItemBuilder:
    """Builder for DefItem."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DefItem = DefItem()

    def build(self) -> DefItem:
        """Build and return DefItem object.

        Returns:
            DefItem instance
        """
        # TODO: Add validation
        return self._obj
