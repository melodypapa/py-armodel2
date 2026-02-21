"""MacMulticastConfiguration AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 467)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.network_endpoint_address import (
    NetworkEndpointAddress,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.mac_multicast_group import (
    MacMulticastGroup,
)


class MacMulticastConfiguration(NetworkEndpointAddress):
    """AUTOSAR MacMulticastConfiguration."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    mac_multicast_group_group_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize MacMulticastConfiguration."""
        super().__init__()
        self.mac_multicast_group_group_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize MacMulticastConfiguration to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(MacMulticastConfiguration, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize mac_multicast_group_group_ref
        if self.mac_multicast_group_group_ref is not None:
            serialized = SerializationHelper.serialize_item(self.mac_multicast_group_group_ref, "MacMulticastGroup")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAC-MULTICAST-GROUP-GROUP-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "MacMulticastConfiguration":
        """Deserialize XML element to MacMulticastConfiguration object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized MacMulticastConfiguration object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(MacMulticastConfiguration, cls).deserialize(element)

        # Parse mac_multicast_group_group_ref
        child = SerializationHelper.find_child_element(element, "MAC-MULTICAST-GROUP-GROUP-REF")
        if child is not None:
            mac_multicast_group_group_ref_value = ARRef.deserialize(child)
            obj.mac_multicast_group_group_ref = mac_multicast_group_group_ref_value

        return obj



class MacMulticastConfigurationBuilder:
    """Builder for MacMulticastConfiguration."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: MacMulticastConfiguration = MacMulticastConfiguration()

    def build(self) -> MacMulticastConfiguration:
        """Build and return MacMulticastConfiguration object.

        Returns:
            MacMulticastConfiguration instance
        """
        # TODO: Add validation
        return self._obj
