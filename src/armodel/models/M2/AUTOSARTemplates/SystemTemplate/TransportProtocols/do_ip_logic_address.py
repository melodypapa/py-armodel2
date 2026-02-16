"""DoIpLogicAddress AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DoIP.abstract_do_ip_logic_address_props import (
    AbstractDoIpLogicAddressProps,
)


class DoIpLogicAddress(Identifiable):
    """AUTOSAR DoIpLogicAddress."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("address", None, True, False, None),  # address
        ("do_ip_logic", None, False, False, AbstractDoIpLogicAddressProps),  # doIpLogic
    ]

    def __init__(self) -> None:
        """Initialize DoIpLogicAddress."""
        super().__init__()
        self.address: Optional[Integer] = None
        self.do_ip_logic: Optional[AbstractDoIpLogicAddressProps] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DoIpLogicAddress to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DoIpLogicAddress":
        """Create DoIpLogicAddress from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DoIpLogicAddress instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DoIpLogicAddress since parent returns ARObject
        return cast("DoIpLogicAddress", obj)


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
