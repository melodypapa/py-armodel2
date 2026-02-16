"""PduActivationRoutingGroup AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.so_con_i_pdu_identifier import (
    SoConIPduIdentifier,
)


class PduActivationRoutingGroup(Identifiable):
    """AUTOSAR PduActivationRoutingGroup."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("event_group", None, False, False, EventGroupControlTypeEnum),  # eventGroup
        ("i_pdu_identifiers", None, False, True, SoConIPduIdentifier),  # iPduIdentifiers
    ]

    def __init__(self) -> None:
        """Initialize PduActivationRoutingGroup."""
        super().__init__()
        self.event_group: Optional[EventGroupControlTypeEnum] = None
        self.i_pdu_identifiers: list[SoConIPduIdentifier] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert PduActivationRoutingGroup to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "PduActivationRoutingGroup":
        """Create PduActivationRoutingGroup from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            PduActivationRoutingGroup instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to PduActivationRoutingGroup since parent returns ARObject
        return cast("PduActivationRoutingGroup", obj)


class PduActivationRoutingGroupBuilder:
    """Builder for PduActivationRoutingGroup."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PduActivationRoutingGroup = PduActivationRoutingGroup()

    def build(self) -> PduActivationRoutingGroup:
        """Build and return PduActivationRoutingGroup object.

        Returns:
            PduActivationRoutingGroup instance
        """
        # TODO: Add validation
        return self._obj
