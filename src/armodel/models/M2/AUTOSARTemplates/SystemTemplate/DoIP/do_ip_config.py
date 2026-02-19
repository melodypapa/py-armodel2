"""DoIpConfig AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 551)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_DoIP.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DoIP.do_ip_interface import (
    DoIpInterface,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.do_ip_logic_address import (
    DoIpLogicAddress,
)


class DoIpConfig(ARObject):
    """AUTOSAR DoIpConfig."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    doip_interfaces: list[DoIpInterface]
    logic_address: Optional[DoIpLogicAddress]
    def __init__(self) -> None:
        """Initialize DoIpConfig."""
        super().__init__()
        self.doip_interfaces: list[DoIpInterface] = []
        self.logic_address: Optional[DoIpLogicAddress] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DoIpConfig":
        """Deserialize XML element to DoIpConfig object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DoIpConfig object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse doip_interfaces (list)
        obj.doip_interfaces = []
        for child in ARObject._find_all_child_elements(element, "DOIP-INTERFACES"):
            doip_interfaces_value = ARObject._deserialize_by_tag(child, "DoIpInterface")
            obj.doip_interfaces.append(doip_interfaces_value)

        # Parse logic_address
        child = ARObject._find_child_element(element, "LOGIC-ADDRESS")
        if child is not None:
            logic_address_value = ARObject._deserialize_by_tag(child, "DoIpLogicAddress")
            obj.logic_address = logic_address_value

        return obj



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
