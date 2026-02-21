"""SenderRecRecordTypeMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 235)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_DataMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping.sender_rec_composite_type_mapping import (
    SenderRecCompositeTypeMapping,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


class SenderRecRecordTypeMapping(SenderRecCompositeTypeMapping):
    """AUTOSAR SenderRecRecordTypeMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    record_elements: list[Any]
    def __init__(self) -> None:
        """Initialize SenderRecRecordTypeMapping."""
        super().__init__()
        self.record_elements: list[Any] = []

    def serialize(self) -> ET.Element:
        """Serialize SenderRecRecordTypeMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SenderRecRecordTypeMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize record_elements (list to container "RECORD-ELEMENTS")
        if self.record_elements:
            wrapper = ET.Element("RECORD-ELEMENTS")
            for item in self.record_elements:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SenderRecRecordTypeMapping":
        """Deserialize XML element to SenderRecRecordTypeMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SenderRecRecordTypeMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SenderRecRecordTypeMapping, cls).deserialize(element)

        # Parse record_elements (list from container "RECORD-ELEMENTS")
        obj.record_elements = []
        container = SerializationHelper.find_child_element(element, "RECORD-ELEMENTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.record_elements.append(child_value)

        return obj



class SenderRecRecordTypeMappingBuilder:
    """Builder for SenderRecRecordTypeMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SenderRecRecordTypeMapping = SenderRecRecordTypeMapping()

    def build(self) -> SenderRecRecordTypeMapping:
        """Build and return SenderRecRecordTypeMapping object.

        Returns:
            SenderRecRecordTypeMapping instance
        """
        # TODO: Add validation
        return self._obj
