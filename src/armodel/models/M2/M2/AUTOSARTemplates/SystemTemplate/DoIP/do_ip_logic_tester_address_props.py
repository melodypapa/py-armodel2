"""DoIpLogicTesterAddressProps AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DoIP.abstract_do_ip_logic_address_props import (
    AbstractDoIpLogicAddressProps,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DoIP.do_ip_routing_activation import (
    DoIpRoutingActivation,
)


class DoIpLogicTesterAddressProps(AbstractDoIpLogicAddressProps):
    """AUTOSAR DoIpLogicTesterAddressProps."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "do_ip_testers": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=DoIpRoutingActivation,
        ),  # doIpTesters
    }

    def __init__(self) -> None:
        """Initialize DoIpLogicTesterAddressProps."""
        super().__init__()
        self.do_ip_testers: list[DoIpRoutingActivation] = []


class DoIpLogicTesterAddressPropsBuilder:
    """Builder for DoIpLogicTesterAddressProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DoIpLogicTesterAddressProps = DoIpLogicTesterAddressProps()

    def build(self) -> DoIpLogicTesterAddressProps:
        """Build and return DoIpLogicTesterAddressProps object.

        Returns:
            DoIpLogicTesterAddressProps instance
        """
        # TODO: Add validation
        return self._obj
