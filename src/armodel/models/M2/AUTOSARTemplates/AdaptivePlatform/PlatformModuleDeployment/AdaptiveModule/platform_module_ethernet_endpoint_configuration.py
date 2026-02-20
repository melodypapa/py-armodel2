"""PlatformModuleEthernetEndpointConfiguration AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 65)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_AdaptivePlatform_PlatformModuleDeployment_AdaptiveModule.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Ip4AddressString,
    Ip6AddressString,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.ethernet_communication_connector import (
    EthernetCommunicationConnector,
)


class PlatformModuleEthernetEndpointConfiguration(ARElement):
    """AUTOSAR PlatformModuleEthernetEndpointConfiguration."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    communication_connector_ref: Optional[ARRef]
    ipv4_multicast_ip_address: Optional[Ip4AddressString]
    ipv6_multicast_ip_address: Optional[Ip6AddressString]
    def __init__(self) -> None:
        """Initialize PlatformModuleEthernetEndpointConfiguration."""
        super().__init__()
        self.communication_connector_ref: Optional[ARRef] = None
        self.ipv4_multicast_ip_address: Optional[Ip4AddressString] = None
        self.ipv6_multicast_ip_address: Optional[Ip6AddressString] = None

    def serialize(self) -> ET.Element:
        """Serialize PlatformModuleEthernetEndpointConfiguration to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(PlatformModuleEthernetEndpointConfiguration, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize communication_connector_ref
        if self.communication_connector_ref is not None:
            serialized = ARObject._serialize_item(self.communication_connector_ref, "EthernetCommunicationConnector")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COMMUNICATION-CONNECTOR-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize ipv4_multicast_ip_address
        if self.ipv4_multicast_ip_address is not None:
            serialized = ARObject._serialize_item(self.ipv4_multicast_ip_address, "Ip4AddressString")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IPV4-MULTICAST-IP-ADDRESS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize ipv6_multicast_ip_address
        if self.ipv6_multicast_ip_address is not None:
            serialized = ARObject._serialize_item(self.ipv6_multicast_ip_address, "Ip6AddressString")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IPV6-MULTICAST-IP-ADDRESS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "PlatformModuleEthernetEndpointConfiguration":
        """Deserialize XML element to PlatformModuleEthernetEndpointConfiguration object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized PlatformModuleEthernetEndpointConfiguration object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(PlatformModuleEthernetEndpointConfiguration, cls).deserialize(element)

        # Parse communication_connector_ref
        child = ARObject._find_child_element(element, "COMMUNICATION-CONNECTOR-REF")
        if child is not None:
            communication_connector_ref_value = ARRef.deserialize(child)
            obj.communication_connector_ref = communication_connector_ref_value

        # Parse ipv4_multicast_ip_address
        child = ARObject._find_child_element(element, "IPV4-MULTICAST-IP-ADDRESS")
        if child is not None:
            ipv4_multicast_ip_address_value = child.text
            obj.ipv4_multicast_ip_address = ipv4_multicast_ip_address_value

        # Parse ipv6_multicast_ip_address
        child = ARObject._find_child_element(element, "IPV6-MULTICAST-IP-ADDRESS")
        if child is not None:
            ipv6_multicast_ip_address_value = child.text
            obj.ipv6_multicast_ip_address = ipv6_multicast_ip_address_value

        return obj



class PlatformModuleEthernetEndpointConfigurationBuilder:
    """Builder for PlatformModuleEthernetEndpointConfiguration."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PlatformModuleEthernetEndpointConfiguration = PlatformModuleEthernetEndpointConfiguration()

    def build(self) -> PlatformModuleEthernetEndpointConfiguration:
        """Build and return PlatformModuleEthernetEndpointConfiguration object.

        Returns:
            PlatformModuleEthernetEndpointConfiguration instance
        """
        # TODO: Add validation
        return self._obj
