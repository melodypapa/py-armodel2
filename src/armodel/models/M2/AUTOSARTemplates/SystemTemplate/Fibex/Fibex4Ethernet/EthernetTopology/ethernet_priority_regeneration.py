"""EthernetPriorityRegeneration AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.referrable import (
    Referrable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class EthernetPriorityRegeneration(Referrable):
    """AUTOSAR EthernetPriorityRegeneration."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("ingress_priority", None, True, False, None),  # ingressPriority
        ("regenerated", None, True, False, None),  # regenerated
    ]

    def __init__(self) -> None:
        """Initialize EthernetPriorityRegeneration."""
        super().__init__()
        self.ingress_priority: Optional[PositiveInteger] = None
        self.regenerated: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert EthernetPriorityRegeneration to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EthernetPriorityRegeneration":
        """Create EthernetPriorityRegeneration from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            EthernetPriorityRegeneration instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to EthernetPriorityRegeneration since parent returns ARObject
        return cast("EthernetPriorityRegeneration", obj)


class EthernetPriorityRegenerationBuilder:
    """Builder for EthernetPriorityRegeneration."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EthernetPriorityRegeneration = EthernetPriorityRegeneration()

    def build(self) -> EthernetPriorityRegeneration:
        """Build and return EthernetPriorityRegeneration object.

        Returns:
            EthernetPriorityRegeneration instance
        """
        # TODO: Add validation
        return self._obj
