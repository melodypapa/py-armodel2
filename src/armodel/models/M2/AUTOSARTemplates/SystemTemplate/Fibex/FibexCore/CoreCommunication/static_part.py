"""StaticPart AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.multiplexed_part import (
    MultiplexedPart,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_signal_i_pdu import (
    ISignalIPdu,
)


class StaticPart(MultiplexedPart):
    """AUTOSAR StaticPart."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("i_pdu", None, False, False, ISignalIPdu),  # iPdu
    ]

    def __init__(self) -> None:
        """Initialize StaticPart."""
        super().__init__()
        self.i_pdu: Optional[ISignalIPdu] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert StaticPart to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "StaticPart":
        """Create StaticPart from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            StaticPart instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to StaticPart since parent returns ARObject
        return cast("StaticPart", obj)


class StaticPartBuilder:
    """Builder for StaticPart."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: StaticPart = StaticPart()

    def build(self) -> StaticPart:
        """Build and return StaticPart object.

        Returns:
            StaticPart instance
        """
        # TODO: Add validation
        return self._obj
