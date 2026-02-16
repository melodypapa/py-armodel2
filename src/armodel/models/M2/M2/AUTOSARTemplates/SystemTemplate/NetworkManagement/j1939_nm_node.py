"""J1939NmNode AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.nm_node import (
    NmNode,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.j1939_node_name import (
    J1939NodeName,
)


class J1939NmNode(NmNode):
    """AUTOSAR J1939NmNode."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "address": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=J1939NmAddressConfigurationCapabilityEnum,
        ),  # address
        "node_name": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=J1939NodeName,
        ),  # nodeName
    }

    def __init__(self) -> None:
        """Initialize J1939NmNode."""
        super().__init__()
        self.address: Optional[J1939NmAddressConfigurationCapabilityEnum] = None
        self.node_name: Optional[J1939NodeName] = None


class J1939NmNodeBuilder:
    """Builder for J1939NmNode."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: J1939NmNode = J1939NmNode()

    def build(self) -> J1939NmNode:
        """Build and return J1939NmNode object.

        Returns:
            J1939NmNode instance
        """
        # TODO: Add validation
        return self._obj
