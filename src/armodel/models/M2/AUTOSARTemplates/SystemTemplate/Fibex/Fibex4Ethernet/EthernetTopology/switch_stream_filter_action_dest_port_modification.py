"""SwitchStreamFilterActionDestPortModification AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.coupling_port import (
    CouplingPort,
)


class SwitchStreamFilterActionDestPortModification(Identifiable):
    """AUTOSAR SwitchStreamFilterActionDestPortModification."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("egress_ports", None, False, True, CouplingPort),  # egressPorts
        ("modification", None, False, False, any (SwitchStreamFilter)),  # modification
    ]

    def __init__(self) -> None:
        """Initialize SwitchStreamFilterActionDestPortModification."""
        super().__init__()
        self.egress_ports: list[CouplingPort] = []
        self.modification: Optional[Any] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SwitchStreamFilterActionDestPortModification to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwitchStreamFilterActionDestPortModification":
        """Create SwitchStreamFilterActionDestPortModification from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SwitchStreamFilterActionDestPortModification instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SwitchStreamFilterActionDestPortModification since parent returns ARObject
        return cast("SwitchStreamFilterActionDestPortModification", obj)


class SwitchStreamFilterActionDestPortModificationBuilder:
    """Builder for SwitchStreamFilterActionDestPortModification."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwitchStreamFilterActionDestPortModification = SwitchStreamFilterActionDestPortModification()

    def build(self) -> SwitchStreamFilterActionDestPortModification:
        """Build and return SwitchStreamFilterActionDestPortModification object.

        Returns:
            SwitchStreamFilterActionDestPortModification instance
        """
        # TODO: Add validation
        return self._obj
