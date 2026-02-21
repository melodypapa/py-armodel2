"""SenderRecArrayTypeMapping AUTOSAR element.

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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.text_table_mapping import (
    TextTableMapping,
)


class SenderRecArrayTypeMapping(SenderRecCompositeTypeMapping):
    """AUTOSAR SenderRecArrayTypeMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    array_elements: list[Any]
    sender_to_signal_ref: Optional[ARRef]
    signal_to_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize SenderRecArrayTypeMapping."""
        super().__init__()
        self.array_elements: list[Any] = []
        self.sender_to_signal_ref: Optional[ARRef] = None
        self.signal_to_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize SenderRecArrayTypeMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SenderRecArrayTypeMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize array_elements (list to container "ARRAY-ELEMENTS")
        if self.array_elements:
            wrapper = ET.Element("ARRAY-ELEMENTS")
            for item in self.array_elements:
                serialized = ARObject._serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize sender_to_signal_ref
        if self.sender_to_signal_ref is not None:
            serialized = ARObject._serialize_item(self.sender_to_signal_ref, "TextTableMapping")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SENDER-TO-SIGNAL-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize signal_to_ref
        if self.signal_to_ref is not None:
            serialized = ARObject._serialize_item(self.signal_to_ref, "TextTableMapping")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SIGNAL-TO-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SenderRecArrayTypeMapping":
        """Deserialize XML element to SenderRecArrayTypeMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SenderRecArrayTypeMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SenderRecArrayTypeMapping, cls).deserialize(element)

        # Parse array_elements (list from container "ARRAY-ELEMENTS")
        obj.array_elements = []
        container = ARObject._find_child_element(element, "ARRAY-ELEMENTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.array_elements.append(child_value)

        # Parse sender_to_signal_ref
        child = ARObject._find_child_element(element, "SENDER-TO-SIGNAL-REF")
        if child is not None:
            sender_to_signal_ref_value = ARRef.deserialize(child)
            obj.sender_to_signal_ref = sender_to_signal_ref_value

        # Parse signal_to_ref
        child = ARObject._find_child_element(element, "SIGNAL-TO-REF")
        if child is not None:
            signal_to_ref_value = ARRef.deserialize(child)
            obj.signal_to_ref = signal_to_ref_value

        return obj



class SenderRecArrayTypeMappingBuilder:
    """Builder for SenderRecArrayTypeMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SenderRecArrayTypeMapping = SenderRecArrayTypeMapping()

    def build(self) -> SenderRecArrayTypeMapping:
        """Build and return SenderRecArrayTypeMapping object.

        Returns:
            SenderRecArrayTypeMapping instance
        """
        # TODO: Add validation
        return self._obj
