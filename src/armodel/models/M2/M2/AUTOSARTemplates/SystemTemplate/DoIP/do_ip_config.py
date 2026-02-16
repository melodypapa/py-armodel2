"""DoIpConfig AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DoIP.do_ip_interface import (
    DoIpInterface,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.do_ip_logic_address import (
    DoIpLogicAddress,
)


class DoIpConfig(ARObject):
    """AUTOSAR DoIpConfig."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "doip_interfaces": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=DoIpInterface,
        ),  # doipInterfaces
        "logic_address": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DoIpLogicAddress,
        ),  # logicAddress
    }

    def __init__(self) -> None:
        """Initialize DoIpConfig."""
        super().__init__()
        self.doip_interfaces: list[DoIpInterface] = []
        self.logic_address: Optional[DoIpLogicAddress] = None


class DoIpConfigBuilder:
    """Builder for DoIpConfig."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DoIpConfig = DoIpConfig()

    def build(self) -> DoIpConfig:
        """Build and return DoIpConfig object.

        Returns:
            DoIpConfig instance
        """
        # TODO: Add validation
        return self._obj
