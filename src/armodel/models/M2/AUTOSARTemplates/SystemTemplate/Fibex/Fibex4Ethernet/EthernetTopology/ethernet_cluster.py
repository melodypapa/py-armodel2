"""EthernetCluster AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 103)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization.decorators import atp_variant

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.mac_multicast_group import (
    MacMulticastGroup,
)


@atp_variant()

class EthernetCluster(ARObject):
    """AUTOSAR EthernetCluster."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    coupling_port: Optional[TimeValue]
    mac_multicast_group_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize EthernetCluster."""
        super().__init__()
        self.coupling_port: Optional[TimeValue] = None
        self.mac_multicast_group_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize EthernetCluster to XML element with atp_variant wrapper.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # Create inner element to hold attributes before wrapping
        inner_elem = ET.Element("INNER")

        # Serialize coupling_port
        if self.coupling_port is not None:
            serialized = SerializationHelper.serialize_item(self.coupling_port, "TimeValue")
            if serialized is not None:
                wrapped = ET.Element("COUPLING-PORT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize mac_multicast_group_refs (list from container "MAC-MULTICAST-GROUP-REFS")
        if self.mac_multicast_group_refs:
            container = ET.Element("MAC-MULTICAST-GROUP-REFS")
            for item in self.mac_multicast_group_refs:
                if is_ref:
                    # For reference lists, serialize as reference
                    if hasattr(item, "serialize"):
                        container.append(item.serialize())
                elif is_primitive_type("MacMulticastGroup", package_data):
                    # Simple primitive type
                    child = ET.Element("MAC-MULTICAST-GROUP")
                    child.text = str(item)
                    container.append(child)
                elif is_enum_type("MacMulticastGroup", package_data):
                    # Enum type - use serialize method
                    if hasattr(item, "serialize"):
                        container.append(item.serialize())
                else:
                    # Complex object type
                    if hasattr(item, "serialize"):
                        container.append(item.serialize())
            inner_elem.append(container)

        # Wrap inner element in atp_variant VARIANTS/CONDITIONAL structure
        wrapped = SerializationHelper.serialize_with_atp_variant(inner_elem, "EthernetCluster")
        elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EthernetCluster":
        """Deserialize XML element to EthernetCluster object with atp_variant unwrapping.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EthernetCluster object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Handle ARObject inherited attributes (checksum and timestamp)
        # Parse timestamp (XML attribute 'T')
        timestamp_value = element.get("T")
        if timestamp_value is not None:
            obj.timestamp = timestamp_value

        # Parse checksum (child element)
        checksum_elem = SerializationHelper.find_child_element(element, "CHECKSUM")
        if checksum_elem is not None:
            checksum_value = checksum_elem.text
            if checksum_value is not None:
                obj.checksum = checksum_value

        # Unwrap atp_variant VARIANTS/CONDITIONAL structure
        inner_elem = SerializationHelper.deserialize_from_atp_variant(element, "EthernetCluster")
        if inner_elem is None:
            # No wrapper structure found, return object with default values
            return obj

        # Parse coupling_port
        child = SerializationHelper.find_child_element(inner_elem, "COUPLING-PORT")
        if child is not None:
            coupling_port_value = child.text
            obj.coupling_port = coupling_port_value

        # Parse mac_multicast_group_refs (list from container "MAC-MULTICAST-GROUP-REFS")
        obj.mac_multicast_group_refs = []
        container = SerializationHelper.find_child_element(inner_elem, "MAC-MULTICAST-GROUP-REFS")
        if container is not None:
            for child in container:
                if is_ref:
                    child_tag = SerializationHelper.strip_namespace(child.tag)
                    if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                        child_value = ARRef.deserialize(child)
                    else:
                        child_value = SerializationHelper.deserialize_by_tag(child, None)
                elif is_primitive_type("MacMulticastGroup", package_data):
                    child_value = child.text
                elif is_enum_type("MacMulticastGroup", package_data):
                    child_value = MacMulticastGroup.deserialize(child)
                else:
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.mac_multicast_group_refs.append(child_value)

        return obj



class EthernetClusterBuilder:
    """Builder for EthernetCluster."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EthernetCluster = EthernetCluster()

    def build(self) -> EthernetCluster:
        """Build and return EthernetCluster object.

        Returns:
            EthernetCluster instance
        """
        # TODO: Add validation
        return self._obj
