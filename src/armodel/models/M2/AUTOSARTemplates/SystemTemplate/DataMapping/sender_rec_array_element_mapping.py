"""SenderRecArrayElementMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 237)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_DataMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping.indexed_array_element import (
    IndexedArrayElement,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping.sender_rec_composite_type_mapping import (
    SenderRecCompositeTypeMapping,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.system_signal import (
    SystemSignal,
)


class SenderRecArrayElementMapping(ARObject):
    """AUTOSAR SenderRecArrayElementMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    complex_type: Optional[SenderRecCompositeTypeMapping]
    indexed_array: Optional[IndexedArrayElement]
    system_signal_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize SenderRecArrayElementMapping."""
        super().__init__()
        self.complex_type: Optional[SenderRecCompositeTypeMapping] = None
        self.indexed_array: Optional[IndexedArrayElement] = None
        self.system_signal_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize SenderRecArrayElementMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SenderRecArrayElementMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize complex_type
        if self.complex_type is not None:
            serialized = SerializationHelper.serialize_item(self.complex_type, "SenderRecCompositeTypeMapping")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COMPLEX-TYPE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize indexed_array
        if self.indexed_array is not None:
            serialized = SerializationHelper.serialize_item(self.indexed_array, "IndexedArrayElement")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("INDEXED-ARRAY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize system_signal_ref
        if self.system_signal_ref is not None:
            serialized = SerializationHelper.serialize_item(self.system_signal_ref, "SystemSignal")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SYSTEM-SIGNAL-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SenderRecArrayElementMapping":
        """Deserialize XML element to SenderRecArrayElementMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SenderRecArrayElementMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SenderRecArrayElementMapping, cls).deserialize(element)

        # Parse complex_type
        child = SerializationHelper.find_child_element(element, "COMPLEX-TYPE")
        if child is not None:
            complex_type_value = SerializationHelper.deserialize_by_tag(child, "SenderRecCompositeTypeMapping")
            obj.complex_type = complex_type_value

        # Parse indexed_array
        child = SerializationHelper.find_child_element(element, "INDEXED-ARRAY")
        if child is not None:
            indexed_array_value = SerializationHelper.deserialize_by_tag(child, "IndexedArrayElement")
            obj.indexed_array = indexed_array_value

        # Parse system_signal_ref
        child = SerializationHelper.find_child_element(element, "SYSTEM-SIGNAL-REF")
        if child is not None:
            system_signal_ref_value = ARRef.deserialize(child)
            obj.system_signal_ref = system_signal_ref_value

        return obj



class SenderRecArrayElementMappingBuilder:
    """Builder for SenderRecArrayElementMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SenderRecArrayElementMapping = SenderRecArrayElementMapping()

    def build(self) -> SenderRecArrayElementMapping:
        """Build and return SenderRecArrayElementMapping object.

        Returns:
            SenderRecArrayElementMapping instance
        """
        # TODO: Add validation
        return self._obj
