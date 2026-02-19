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
    @classmethod
    def deserialize(cls, element: ET.Element) -> "MacMulticastConfiguration":
        """Deserialize XML element to MacMulticastConfiguration object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized MacMulticastConfiguration object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse mac_multicast_group_group_ref
        child = ARObject._find_child_element(element, "MAC-MULTICAST-GROUP-GROUP")
        if child is not None:
            mac_multicast_group_group_ref_value = ARObject._deserialize_by_tag(child, "MacMulticastGroup")
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
