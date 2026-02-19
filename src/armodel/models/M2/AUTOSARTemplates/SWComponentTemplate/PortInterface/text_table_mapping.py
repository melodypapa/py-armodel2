"""TextTableMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 145)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 230)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_PortInterface.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import (
    MappingDirectionEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.text_table_value_pair import (
    TextTableValuePair,
)


class TextTableMapping(ARObject):
    """AUTOSAR TextTableMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    bitfield_text_table: Optional[PositiveInteger]
    identical: Optional[Boolean]
    mapping_ref: Optional[MappingDirectionEnum]
    value_pairs: list[TextTableValuePair]
    def __init__(self) -> None:
        """Initialize TextTableMapping."""
        super().__init__()
        self.bitfield_text_table: Optional[PositiveInteger] = None
        self.identical: Optional[Boolean] = None
        self.mapping_ref: Optional[MappingDirectionEnum] = None
        self.value_pairs: list[TextTableValuePair] = []
    def serialize(self) -> ET.Element:
        """Serialize TextTableMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize bitfield_text_table
        if self.bitfield_text_table is not None:
            serialized = ARObject._serialize_item(self.bitfield_text_table, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BITFIELD-TEXT-TABLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize identical
        if self.identical is not None:
            serialized = ARObject._serialize_item(self.identical, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IDENTICAL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize mapping_ref
        if self.mapping_ref is not None:
            serialized = ARObject._serialize_item(self.mapping_ref, "MappingDirectionEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAPPING")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize value_pairs (list to container "VALUE-PAIRS")
        if self.value_pairs:
            wrapper = ET.Element("VALUE-PAIRS")
            for item in self.value_pairs:
                serialized = ARObject._serialize_item(item, "TextTableValuePair")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TextTableMapping":
        """Deserialize XML element to TextTableMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TextTableMapping object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse bitfield_text_table
        child = ARObject._find_child_element(element, "BITFIELD-TEXT-TABLE")
        if child is not None:
            bitfield_text_table_value = child.text
            obj.bitfield_text_table = bitfield_text_table_value

        # Parse identical
        child = ARObject._find_child_element(element, "IDENTICAL")
        if child is not None:
            identical_value = child.text
            obj.identical = identical_value

        # Parse mapping_ref
        child = ARObject._find_child_element(element, "MAPPING")
        if child is not None:
            mapping_ref_value = ARRef.deserialize(child)
            obj.mapping_ref = mapping_ref_value

        # Parse value_pairs (list from container "VALUE-PAIRS")
        obj.value_pairs = []
        container = ARObject._find_child_element(element, "VALUE-PAIRS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.value_pairs.append(child_value)

        return obj



class TextTableMappingBuilder:
    """Builder for TextTableMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TextTableMapping = TextTableMapping()

    def build(self) -> TextTableMapping:
        """Build and return TextTableMapping object.

        Returns:
            TextTableMapping instance
        """
        # TODO: Add validation
        return self._obj
