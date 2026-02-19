"""TopicContent AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 478)

JSON Source: docs/json/packages/M2_MSR_Documentation_Chapters.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.MSR.Documentation.BlockElements.documentation_block import (
    DocumentationBlock,
)
from armodel.models.M2.MSR.Documentation.BlockElements.OasisExchangeTable.table import (
    Table,
)


class TopicContent(ARObject):
    """AUTOSAR TopicContent."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    block_level: DocumentationBlock
    table: Optional[Table]
    traceable_table: Any
    def __init__(self) -> None:
        """Initialize TopicContent."""
        super().__init__()
        self.block_level: DocumentationBlock = None
        self.table: Optional[Table] = None
        self.traceable_table: Any = None

    def serialize(self) -> ET.Element:
        """Serialize TopicContent to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize block_level
        if self.block_level is not None:
            serialized = ARObject._serialize_item(self.block_level, "DocumentationBlock")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BLOCK-LEVEL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize table
        if self.table is not None:
            serialized = ARObject._serialize_item(self.table, "Table")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TABLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize traceable_table
        if self.traceable_table is not None:
            serialized = ARObject._serialize_item(self.traceable_table, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TRACEABLE-TABLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TopicContent":
        """Deserialize XML element to TopicContent object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TopicContent object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse block_level
        child = ARObject._find_child_element(element, "BLOCK-LEVEL")
        if child is not None:
            block_level_value = ARObject._deserialize_by_tag(child, "DocumentationBlock")
            obj.block_level = block_level_value

        # Parse table
        child = ARObject._find_child_element(element, "TABLE")
        if child is not None:
            table_value = ARObject._deserialize_by_tag(child, "Table")
            obj.table = table_value

        # Parse traceable_table
        child = ARObject._find_child_element(element, "TRACEABLE-TABLE")
        if child is not None:
            traceable_table_value = child.text
            obj.traceable_table = traceable_table_value

        return obj



class TopicContentBuilder:
    """Builder for TopicContent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TopicContent = TopicContent()

    def build(self) -> TopicContent:
        """Build and return TopicContent object.

        Returns:
            TopicContent instance
        """
        # TODO: Add validation
        return self._obj
