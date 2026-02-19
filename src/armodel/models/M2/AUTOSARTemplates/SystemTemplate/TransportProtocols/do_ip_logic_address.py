"""DoIpLogicAddress AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 555)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DoIP.abstract_do_ip_logic_address_props import (
    AbstractDoIpLogicAddressProps,
)


class DoIpLogicAddress(Identifiable):
    """AUTOSAR DoIpLogicAddress."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    address: Optional[Integer]
    do_ip_logic: Optional[AbstractDoIpLogicAddressProps]
    def __init__(self) -> None:
        """Initialize DoIpLogicAddress."""
        super().__init__()
        self.address: Optional[Integer] = None
        self.do_ip_logic: Optional[AbstractDoIpLogicAddressProps] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DoIpLogicAddress":
        """Deserialize XML element to DoIpLogicAddress object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DoIpLogicAddress object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DoIpLogicAddress, cls).deserialize(element)

        # Parse address
        child = ARObject._find_child_element(element, "ADDRESS")
        if child is not None:
            address_value = child.text
            obj.address = address_value

        # Parse do_ip_logic
        child = ARObject._find_child_element(element, "DO-IP-LOGIC")
        if child is not None:
            do_ip_logic_value = ARObject._deserialize_by_tag(child, "AbstractDoIpLogicAddressProps")
            obj.do_ip_logic = do_ip_logic_value

        return obj



class DoIpLogicAddressBuilder:
    """Builder for DoIpLogicAddress."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DoIpLogicAddress = DoIpLogicAddress()

    def build(self) -> DoIpLogicAddress:
        """Build and return DoIpLogicAddress object.

        Returns:
            DoIpLogicAddress instance
        """
        # TODO: Add validation
        return self._obj
