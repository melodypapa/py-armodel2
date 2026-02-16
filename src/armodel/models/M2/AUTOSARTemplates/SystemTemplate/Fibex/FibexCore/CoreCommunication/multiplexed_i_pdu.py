"""MultiplexedIPdu AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_pdu import (
    IPdu,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.dynamic_part import (
    DynamicPart,
)


class MultiplexedIPdu(IPdu):
    """AUTOSAR MultiplexedIPdu."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("dynamic_part", None, False, False, DynamicPart),  # dynamicPart
        ("selector_field", None, True, False, None),  # selectorField
        ("unused_bit", None, True, False, None),  # unusedBit
    ]

    def __init__(self) -> None:
        """Initialize MultiplexedIPdu."""
        super().__init__()
        self.dynamic_part: Optional[DynamicPart] = None
        self.selector_field: Optional[Integer] = None
        self.unused_bit: Optional[Integer] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert MultiplexedIPdu to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "MultiplexedIPdu":
        """Create MultiplexedIPdu from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            MultiplexedIPdu instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to MultiplexedIPdu since parent returns ARObject
        return cast("MultiplexedIPdu", obj)


class MultiplexedIPduBuilder:
    """Builder for MultiplexedIPdu."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: MultiplexedIPdu = MultiplexedIPdu()

    def build(self) -> MultiplexedIPdu:
        """Build and return MultiplexedIPdu object.

        Returns:
            MultiplexedIPdu instance
        """
        # TODO: Add validation
        return self._obj
