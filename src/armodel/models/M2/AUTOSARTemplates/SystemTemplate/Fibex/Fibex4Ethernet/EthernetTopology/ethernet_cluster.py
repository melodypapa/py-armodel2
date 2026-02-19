"""EthernetCluster AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 103)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.mac_multicast_group import (
    MacMulticastGroup,
)


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
    @classmethod
    def deserialize(cls, element: ET.Element) -> "EthernetCluster":
        """Deserialize XML element to EthernetCluster object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EthernetCluster object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse coupling_port
        child = ARObject._find_child_element(element, "COUPLING-PORT")
        if child is not None:
            coupling_port_value = child.text
            obj.coupling_port = coupling_port_value

        # Parse mac_multicast_group_refs (list)
        obj.mac_multicast_group_refs = []
        for child in ARObject._find_all_child_elements(element, "MAC-MULTICAST-GROUPS"):
            mac_multicast_group_refs_value = ARObject._deserialize_by_tag(child, "MacMulticastGroup")
            obj.mac_multicast_group_refs.append(mac_multicast_group_refs_value)

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
