"""DoIpLogicTesterAddressProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 556)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_DoIP.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DoIP.abstract_do_ip_logic_address_props import (
    AbstractDoIpLogicAddressProps,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DoIP.do_ip_routing_activation import (
    DoIpRoutingActivation,
)


class DoIpLogicTesterAddressProps(AbstractDoIpLogicAddressProps):
    """AUTOSAR DoIpLogicTesterAddressProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    do_ip_testers: list[DoIpRoutingActivation]
    def __init__(self) -> None:
        """Initialize DoIpLogicTesterAddressProps."""
        super().__init__()
        self.do_ip_testers: list[DoIpRoutingActivation] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DoIpLogicTesterAddressProps":
        """Deserialize XML element to DoIpLogicTesterAddressProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DoIpLogicTesterAddressProps object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse do_ip_testers (list)
        obj.do_ip_testers = []
        for child in ARObject._find_all_child_elements(element, "DO-IP-TESTERS"):
            do_ip_testers_value = ARObject._deserialize_by_tag(child, "DoIpRoutingActivation")
            obj.do_ip_testers.append(do_ip_testers_value)

        return obj



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
