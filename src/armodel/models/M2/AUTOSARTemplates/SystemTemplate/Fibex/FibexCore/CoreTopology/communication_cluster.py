"""CommunicationCluster AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 107)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 57)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
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
        """Serialize CommunicationCluster to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize baudrate
        if self.baudrate is not None:
            serialized = ARObject._serialize_item(self.baudrate, "PositiveUnlimitedInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BAUDRATE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize physical_channels (list to container "PHYSICAL-CHANNELS")
        if self.physical_channels:
            wrapper = ET.Element("PHYSICAL-CHANNELS")
            for item in self.physical_channels:
                serialized = ARObject._serialize_item(item, "PhysicalChannel")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize protocol_name
        if self.protocol_name is not None:
            serialized = ARObject._serialize_item(self.protocol_name, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PROTOCOL-NAME")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize protocol_version
        if self.protocol_version is not None:
            serialized = ARObject._serialize_item(self.protocol_version, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PROTOCOL-VERSION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CommunicationCluster":
        """Deserialize XML element to CommunicationCluster object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CommunicationCluster object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse baudrate
        child = ARObject._find_child_element(element, "BAUDRATE")
        if child is not None:
            baudrate_value = child.text
            obj.baudrate = baudrate_value

        # Parse physical_channels (list from container "PHYSICAL-CHANNELS")
        obj.physical_channels = []
        container = ARObject._find_child_element(element, "PHYSICAL-CHANNELS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.physical_channels.append(child_value)

        # Parse protocol_name
        child = ARObject._find_child_element(element, "PROTOCOL-NAME")
        if child is not None:
            protocol_name_value = child.text
            obj.protocol_name = protocol_name_value

        # Parse protocol_version
        child = ARObject._find_child_element(element, "PROTOCOL-VERSION")
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
