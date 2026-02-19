"""NetworkEndpoint AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 463)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    String,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.infrastructure_services import (
    InfrastructureServices,
)

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication.ip_sec_config import (
        IPSecConfig,
    )



class NetworkEndpoint(Identifiable):
    """AUTOSAR NetworkEndpoint."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    fully_qualified: Optional[String]
    infrastructure_services: Optional[InfrastructureServices]
    ip_sec_config: Optional[IPSecConfig]
    network_endpoints: list[NetworkEndpoint]
    priority: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize NetworkEndpoint."""
        super().__init__()
        self.fully_qualified: Optional[String] = None
        self.infrastructure_services: Optional[InfrastructureServices] = None
        self.ip_sec_config: Optional[IPSecConfig] = None
        self.network_endpoints: list[NetworkEndpoint] = []
        self.priority: Optional[PositiveInteger] = None
    def serialize(self) -> ET.Element:
        """Serialize NetworkEndpoint to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(NetworkEndpoint, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize fully_qualified
        if self.fully_qualified is not None:
            serialized = ARObject._serialize_item(self.fully_qualified, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FULLY-QUALIFIED")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize infrastructure_services
        if self.infrastructure_services is not None:
            serialized = ARObject._serialize_item(self.infrastructure_services, "InfrastructureServices")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("INFRASTRUCTURE-SERVICES")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize ip_sec_config
        if self.ip_sec_config is not None:
            serialized = ARObject._serialize_item(self.ip_sec_config, "IPSecConfig")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IP-SEC-CONFIG")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize network_endpoints (list to container "NETWORK-ENDPOINTS")
        if self.network_endpoints:
            wrapper = ET.Element("NETWORK-ENDPOINTS")
            for item in self.network_endpoints:
                serialized = ARObject._serialize_item(item, "NetworkEndpoint")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize priority
        if self.priority is not None:
            serialized = ARObject._serialize_item(self.priority, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PRIORITY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "NetworkEndpoint":
        """Deserialize XML element to NetworkEndpoint object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized NetworkEndpoint object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(NetworkEndpoint, cls).deserialize(element)

        # Parse fully_qualified
        child = ARObject._find_child_element(element, "FULLY-QUALIFIED")
        if child is not None:
            fully_qualified_value = child.text
            obj.fully_qualified = fully_qualified_value

        # Parse infrastructure_services
        child = ARObject._find_child_element(element, "INFRASTRUCTURE-SERVICES")
        if child is not None:
            infrastructure_services_value = ARObject._deserialize_by_tag(child, "InfrastructureServices")
            obj.infrastructure_services = infrastructure_services_value

        # Parse ip_sec_config
        child = ARObject._find_child_element(element, "IP-SEC-CONFIG")
        if child is not None:
            ip_sec_config_value = ARObject._deserialize_by_tag(child, "IPSecConfig")
            obj.ip_sec_config = ip_sec_config_value

        # Parse network_endpoints (list from container "NETWORK-ENDPOINTS")
        obj.network_endpoints = []
        container = ARObject._find_child_element(element, "NETWORK-ENDPOINTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.network_endpoints.append(child_value)

        # Parse priority
        child = ARObject._find_child_element(element, "PRIORITY")
        if child is not None:
            priority_value = child.text
            obj.priority = priority_value

        return obj



class NetworkEndpointBuilder:
    """Builder for NetworkEndpoint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: NetworkEndpoint = NetworkEndpoint()

    def build(self) -> NetworkEndpoint:
        """Build and return NetworkEndpoint object.

        Returns:
            NetworkEndpoint instance
        """
        # TODO: Add validation
        return self._obj
