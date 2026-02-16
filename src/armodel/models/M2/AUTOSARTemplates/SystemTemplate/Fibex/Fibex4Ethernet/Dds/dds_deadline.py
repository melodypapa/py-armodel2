"""DdsDeadline AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Float,
)


class DdsDeadline(ARObject):
    """AUTOSAR DdsDeadline."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("deadline_period", None, True, False, None),  # deadlinePeriod
    ]

    def __init__(self) -> None:
        """Initialize DdsDeadline."""
        super().__init__()
        self.deadline_period: Optional[Float] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DdsDeadline to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DdsDeadline":
        """Create DdsDeadline from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DdsDeadline instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DdsDeadline since parent returns ARObject
        return cast("DdsDeadline", obj)


class DdsDeadlineBuilder:
    """Builder for DdsDeadline."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DdsDeadline = DdsDeadline()

    def build(self) -> DdsDeadline:
        """Build and return DdsDeadline object.

        Returns:
            DdsDeadline instance
        """
        # TODO: Add validation
        return self._obj
