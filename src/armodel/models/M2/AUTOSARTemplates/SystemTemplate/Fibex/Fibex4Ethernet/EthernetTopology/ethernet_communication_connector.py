"""EthernetCommunicationConnector AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 117)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.communication_connector import (
    CommunicationConnector,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.eth_ip_props import (
    EthIpProps,
)


class EthernetCommunicationConnector(CommunicationConnector):
    """AUTOSAR EthernetCommunicationConnector."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    eth_ip_props: Optional[EthIpProps]
    maximum: Optional[PositiveInteger]
    neighbor_cache: Optional[PositiveInteger]
    path_mtu: Optional[Boolean]
    path_mtu_timeout: Optional[TimeValue]
    def __init__(self) -> None:
        """Initialize EthernetCommunicationConnector."""
        super().__init__()
        self.eth_ip_props: Optional[EthIpProps] = None
        self.maximum: Optional[PositiveInteger] = None
        self.neighbor_cache: Optional[PositiveInteger] = None
        self.path_mtu: Optional[Boolean] = None
        self.path_mtu_timeout: Optional[TimeValue] = None

    def serialize(self) -> ET.Element:
        """Serialize EthernetCommunicationConnector to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EthernetCommunicationConnector, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize eth_ip_props
        if self.eth_ip_props is not None:
            serialized = ARObject._serialize_item(self.eth_ip_props, "EthIpProps")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ETH-IP-PROPS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize maximum
        if self.maximum is not None:
            serialized = ARObject._serialize_item(self.maximum, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAXIMUM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize neighbor_cache
        if self.neighbor_cache is not None:
            serialized = ARObject._serialize_item(self.neighbor_cache, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NEIGHBOR-CACHE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize path_mtu
        if self.path_mtu is not None:
            serialized = ARObject._serialize_item(self.path_mtu, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PATH-MTU")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize path_mtu_timeout
        if self.path_mtu_timeout is not None:
            serialized = ARObject._serialize_item(self.path_mtu_timeout, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PATH-MTU-TIMEOUT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EthernetCommunicationConnector":
        """Deserialize XML element to EthernetCommunicationConnector object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EthernetCommunicationConnector object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EthernetCommunicationConnector, cls).deserialize(element)

        # Parse eth_ip_props
        child = ARObject._find_child_element(element, "ETH-IP-PROPS")
        if child is not None:
            eth_ip_props_value = ARObject._deserialize_by_tag(child, "EthIpProps")
            obj.eth_ip_props = eth_ip_props_value

        # Parse maximum
        child = ARObject._find_child_element(element, "MAXIMUM")
        if child is not None:
            maximum_value = child.text
            obj.maximum = maximum_value

        # Parse neighbor_cache
        child = ARObject._find_child_element(element, "NEIGHBOR-CACHE")
        if child is not None:
            neighbor_cache_value = child.text
            obj.neighbor_cache = neighbor_cache_value

        # Parse path_mtu
        child = ARObject._find_child_element(element, "PATH-MTU")
        if child is not None:
            path_mtu_value = child.text
            obj.path_mtu = path_mtu_value

        # Parse path_mtu_timeout
        child = ARObject._find_child_element(element, "PATH-MTU-TIMEOUT")
        if child is not None:
            path_mtu_timeout_value = child.text
            obj.path_mtu_timeout = path_mtu_timeout_value

        return obj



class EthernetCommunicationConnectorBuilder:
    """Builder for EthernetCommunicationConnector."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EthernetCommunicationConnector = EthernetCommunicationConnector()

    def build(self) -> EthernetCommunicationConnector:
        """Build and return EthernetCommunicationConnector object.

        Returns:
            EthernetCommunicationConnector instance
        """
        # TODO: Add validation
        return self._obj
