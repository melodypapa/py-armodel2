"""CommunicationCluster AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 107)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 57)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization.decorators import atp_variant

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveUnlimitedInteger,
    String,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.physical_channel import (
    PhysicalChannel,
)
from abc import ABC, abstractmethod


class CommunicationCluster(ARObject, ABC):
    """AUTOSAR CommunicationCluster."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    baudrate: Optional[PositiveUnlimitedInteger]
    physical_channels: list[PhysicalChannel]
    protocol_name: Optional[String]
    protocol_version: Optional[String]
    def __init__(self) -> None:
        """Initialize CommunicationCluster."""
        super().__init__()
        self.baudrate: Optional[PositiveUnlimitedInteger] = None
        self.physical_channels: list[PhysicalChannel] = []
        self.protocol_name: Optional[String] = None
        self.protocol_version: Optional[String] = None

    def serialize(self) -> ET.Element:
        """Serialize CommunicationCluster to XML element with atp_variant wrapper.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(CommunicationCluster, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Create inner element to hold attributes before wrapping
        inner_elem = ET.Element("INNER")

        # Serialize baudrate
        if self.baudrate is not None:
            serialized = SerializationHelper.serialize_item(self.baudrate, "PositiveUnlimitedInteger")
            if serialized is not None:
                wrapped = ET.Element("BAUDRATE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize physical_channels (list from container "PHYSICAL-CHANNELS")
        if self.physical_channels:
            container = ET.Element("PHYSICAL-CHANNELS")
            for item in self.physical_channels:
                if is_ref:
                    # For reference lists, serialize as reference
                    if hasattr(item, "serialize"):
                        container.append(item.serialize())
                elif is_primitive_type("PhysicalChannel", package_data):
                    # Simple primitive type
                    child = ET.Element("PHYSICAL-CHANNEL")
                    child.text = str(item)
                    container.append(child)
                elif is_enum_type("PhysicalChannel", package_data):
                    # Enum type - use serialize method
                    if hasattr(item, "serialize"):
                        container.append(item.serialize())
                else:
                    # Complex object type
                    if hasattr(item, "serialize"):
                        container.append(item.serialize())
            inner_elem.append(container)

        # Serialize protocol_name
        if self.protocol_name is not None:
            serialized = SerializationHelper.serialize_item(self.protocol_name, "String")
            if serialized is not None:
                wrapped = ET.Element("PROTOCOL-NAME")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize protocol_version
        if self.protocol_version is not None:
            serialized = SerializationHelper.serialize_item(self.protocol_version, "String")
            if serialized is not None:
                wrapped = ET.Element("PROTOCOL-VERSION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Wrap inner element in atp_variant VARIANTS/CONDITIONAL structure
        wrapped = SerializationHelper.serialize_with_atp_variant(inner_elem, "CommunicationCluster")
        elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CommunicationCluster":
        """Deserialize XML element to CommunicationCluster object with atp_variant unwrapping.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CommunicationCluster object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CommunicationCluster, cls).deserialize(element)

        # Unwrap atp_variant VARIANTS/CONDITIONAL structure
        inner_elem = SerializationHelper.deserialize_from_atp_variant(element, "CommunicationCluster")
        if inner_elem is None:
            # No wrapper structure found, return object with default values
            return obj

        # Parse baudrate
        child = SerializationHelper.find_child_element(inner_elem, "BAUDRATE")
        if child is not None:
            baudrate_value = child.text
            obj.baudrate = baudrate_value

        # Parse physical_channels (list from container "PHYSICAL-CHANNELS")
        obj.physical_channels = []
        container = SerializationHelper.find_child_element(inner_elem, "PHYSICAL-CHANNELS")
        if container is not None:
            for child in container:
                if is_ref:
                    child_tag = SerializationHelper.strip_namespace(child.tag)
                    if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                        child_value = ARRef.deserialize(child)
                    else:
                        child_value = SerializationHelper.deserialize_by_tag(child, None)
                elif is_primitive_type("PhysicalChannel", package_data):
                    child_value = child.text
                elif is_enum_type("PhysicalChannel", package_data):
                    child_value = PhysicalChannel.deserialize(child)
                else:
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.physical_channels.append(child_value)

        # Parse protocol_name
        child = SerializationHelper.find_child_element(inner_elem, "PROTOCOL-NAME")
        if child is not None:
            protocol_name_value = child.text
            obj.protocol_name = protocol_name_value

        # Parse protocol_version
        child = SerializationHelper.find_child_element(inner_elem, "PROTOCOL-VERSION")
        if child is not None:
            protocol_version_value = child.text
            obj.protocol_version = protocol_version_value

        return obj



class CommunicationClusterBuilder:
    """Builder for CommunicationCluster."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CommunicationCluster = CommunicationCluster()

    def build(self) -> CommunicationCluster:
        """Build and return CommunicationCluster object.

        Returns:
            CommunicationCluster instance
        """
        # TODO: Add validation
        return self._obj
