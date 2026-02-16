"""DoIpRoutingActivation AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DoIP.do_ip_logic_target_address_props import (
    DoIpLogicTargetAddressProps,
)


class DoIpRoutingActivation(Identifiable):
    """AUTOSAR DoIpRoutingActivation."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("do_ip_targets", None, False, True, DoIpLogicTargetAddressProps),  # doIpTargets
    ]

    def __init__(self) -> None:
        """Initialize DoIpRoutingActivation."""
        super().__init__()
        self.do_ip_targets: list[DoIpLogicTargetAddressProps] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DoIpRoutingActivation to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DoIpRoutingActivation":
        """Create DoIpRoutingActivation from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DoIpRoutingActivation instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DoIpRoutingActivation since parent returns ARObject
        return cast("DoIpRoutingActivation", obj)


class DoIpRoutingActivationBuilder:
    """Builder for DoIpRoutingActivation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DoIpRoutingActivation = DoIpRoutingActivation()

    def build(self) -> DoIpRoutingActivation:
        """Build and return DoIpRoutingActivation object.

        Returns:
            DoIpRoutingActivation instance
        """
        # TODO: Add validation
        return self._obj
