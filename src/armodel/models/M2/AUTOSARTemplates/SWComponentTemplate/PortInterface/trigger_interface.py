"""TriggerInterface AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.port_interface import (
    PortInterface,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration.trigger import (
    Trigger,
)


class TriggerInterface(PortInterface):
    """AUTOSAR TriggerInterface."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("triggers", None, False, True, Trigger),  # triggers
    ]

    def __init__(self) -> None:
        """Initialize TriggerInterface."""
        super().__init__()
        self.triggers: list[Trigger] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert TriggerInterface to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TriggerInterface":
        """Create TriggerInterface from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            TriggerInterface instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to TriggerInterface since parent returns ARObject
        return cast("TriggerInterface", obj)


class TriggerInterfaceBuilder:
    """Builder for TriggerInterface."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TriggerInterface = TriggerInterface()

    def build(self) -> TriggerInterface:
        """Build and return TriggerInterface object.

        Returns:
            TriggerInterface instance
        """
        # TODO: Add validation
        return self._obj
