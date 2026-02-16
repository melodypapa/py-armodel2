"""DynamicPart AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.multiplexed_part import (
    MultiplexedPart,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.dynamic_part_alternative import (
    DynamicPartAlternative,
)


class DynamicPart(MultiplexedPart):
    """AUTOSAR DynamicPart."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("dynamic_parts", None, False, True, DynamicPartAlternative),  # dynamicParts
    ]

    def __init__(self) -> None:
        """Initialize DynamicPart."""
        super().__init__()
        self.dynamic_parts: list[DynamicPartAlternative] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DynamicPart to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DynamicPart":
        """Create DynamicPart from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DynamicPart instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DynamicPart since parent returns ARObject
        return cast("DynamicPart", obj)


class DynamicPartBuilder:
    """Builder for DynamicPart."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DynamicPart = DynamicPart()

    def build(self) -> DynamicPart:
        """Build and return DynamicPart object.

        Returns:
            DynamicPart instance
        """
        # TODO: Add validation
        return self._obj
