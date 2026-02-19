"""EthernetPhysicalChannel AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 314)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 105)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.physical_channel import (
    PhysicalChannel,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.network_endpoint import (
    NetworkEndpoint,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.so_ad_config import (
    SoAdConfig,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.vlan_config import (
    VlanConfig,
)


class EthernetPhysicalChannel(PhysicalChannel):
    """AUTOSAR EthernetPhysicalChannel."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    network_endpoints: list[NetworkEndpoint]
    so_ad_config: Optional[SoAdConfig]
    vlan: Optional[VlanConfig]
    def __init__(self) -> None:
        """Initialize EthernetPhysicalChannel."""
        super().__init__()
        self.network_endpoints: list[NetworkEndpoint] = []
        self.so_ad_config: Optional[SoAdConfig] = None
        self.vlan: Optional[VlanConfig] = None
    def serialize(self) -> ET.Element:
        """Serialize EthernetPhysicalChannel to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EthernetPhysicalChannel, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize network_endpoints (list to container "NETWORK-ENDPOINTS")
        if self.network_endpoints:
            wrapper = ET.Element("NETWORK-ENDPOINTS")
            for item in self.network_endpoints:
                serialized = ARObject._serialize_item(item, "NetworkEndpoint")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize so_ad_config
        if self.so_ad_config is not None:
            serialized = ARObject._serialize_item(self.so_ad_config, "SoAdConfig")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SO-AD-CONFIG")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize vlan
        if self.vlan is not None:
            serialized = ARObject._serialize_item(self.vlan, "VlanConfig")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VLAN")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EthernetPhysicalChannel":
        """Deserialize XML element to EthernetPhysicalChannel object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EthernetPhysicalChannel object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EthernetPhysicalChannel, cls).deserialize(element)

        # Parse network_endpoints (list from container "NETWORK-ENDPOINTS")
        obj.network_endpoints = []
        container = ARObject._find_child_element(element, "NETWORK-ENDPOINTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.network_endpoints.append(child_value)

        # Parse so_ad_config
        child = ARObject._find_child_element(element, "SO-AD-CONFIG")
        if child is not None:
            so_ad_config_value = ARObject._deserialize_by_tag(child, "SoAdConfig")
            obj.so_ad_config = so_ad_config_value

        # Parse vlan
        child = ARObject._find_child_element(element, "VLAN")
        if child is not None:
            vlan_value = ARObject._deserialize_by_tag(child, "VlanConfig")
            obj.vlan = vlan_value

        return obj



class EthernetPhysicalChannelBuilder:
    """Builder for EthernetPhysicalChannel."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EthernetPhysicalChannel = EthernetPhysicalChannel()

    def build(self) -> EthernetPhysicalChannel:
        """Build and return EthernetPhysicalChannel object.

        Returns:
            EthernetPhysicalChannel instance
        """
        # TODO: Add validation
        return self._obj
