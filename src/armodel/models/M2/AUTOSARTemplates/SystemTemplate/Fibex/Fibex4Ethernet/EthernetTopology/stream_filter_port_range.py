"""StreamFilterPortRange AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class StreamFilterPortRange(ARObject):
    """AUTOSAR StreamFilterPortRange."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("max", None, True, False, None),  # max
        ("min", None, True, False, None),  # min
    ]

    def __init__(self) -> None:
        """Initialize StreamFilterPortRange."""
        super().__init__()
        self.max: Optional[PositiveInteger] = None
        self.min: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert StreamFilterPortRange to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "StreamFilterPortRange":
        """Create StreamFilterPortRange from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            StreamFilterPortRange instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to StreamFilterPortRange since parent returns ARObject
        return cast("StreamFilterPortRange", obj)


class StreamFilterPortRangeBuilder:
    """Builder for StreamFilterPortRange."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: StreamFilterPortRange = StreamFilterPortRange()

    def build(self) -> StreamFilterPortRange:
        """Build and return StreamFilterPortRange object.

        Returns:
            StreamFilterPortRange instance
        """
        # TODO: Add validation
        return self._obj
