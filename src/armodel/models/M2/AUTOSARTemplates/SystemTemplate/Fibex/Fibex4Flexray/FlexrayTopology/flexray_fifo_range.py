"""FlexrayFifoRange AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)


class FlexrayFifoRange(ARObject):
    """AUTOSAR FlexrayFifoRange."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("range_max", None, True, False, None),  # rangeMax
        ("range_min", None, True, False, None),  # rangeMin
    ]

    def __init__(self) -> None:
        """Initialize FlexrayFifoRange."""
        super().__init__()
        self.range_max: Optional[Integer] = None
        self.range_min: Optional[Integer] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert FlexrayFifoRange to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FlexrayFifoRange":
        """Create FlexrayFifoRange from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            FlexrayFifoRange instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to FlexrayFifoRange since parent returns ARObject
        return cast("FlexrayFifoRange", obj)


class FlexrayFifoRangeBuilder:
    """Builder for FlexrayFifoRange."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FlexrayFifoRange = FlexrayFifoRange()

    def build(self) -> FlexrayFifoRange:
        """Build and return FlexrayFifoRange object.

        Returns:
            FlexrayFifoRange instance
        """
        # TODO: Add validation
        return self._obj
