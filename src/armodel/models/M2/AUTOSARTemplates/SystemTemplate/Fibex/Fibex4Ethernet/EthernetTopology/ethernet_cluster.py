"""EthernetCluster AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.mac_multicast_group import (
    MacMulticastGroup,
)


class EthernetCluster(ARObject):
    """AUTOSAR EthernetCluster."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "coupling_port": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # couplingPort
        "mac_multicast_groups": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=MacMulticastGroup,
        ),  # macMulticastGroups
    }

    def __init__(self) -> None:
        """Initialize EthernetCluster."""
        super().__init__()
        self.coupling_port: Optional[TimeValue] = None
        self.mac_multicast_groups: list[MacMulticastGroup] = []


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
