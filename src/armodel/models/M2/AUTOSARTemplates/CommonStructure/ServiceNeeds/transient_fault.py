"""TransientFault AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.traced_failure import (
    TracedFailure,
)


class TransientFault(TracedFailure):
    """AUTOSAR TransientFault."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("possible_error_reactions", None, False, True, any (PossibleErrorReaction)),  # possibleErrorReactions
    ]

    def __init__(self) -> None:
        """Initialize TransientFault."""
        super().__init__()
        self.possible_error_reactions: list[Any] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert TransientFault to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TransientFault":
        """Create TransientFault from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            TransientFault instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to TransientFault since parent returns ARObject
        return cast("TransientFault", obj)


class TransientFaultBuilder:
    """Builder for TransientFault."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TransientFault = TransientFault()

    def build(self) -> TransientFault:
        """Build and return TransientFault object.

        Returns:
            TransientFault instance
        """
        # TODO: Add validation
        return self._obj
