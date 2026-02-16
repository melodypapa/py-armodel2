"""DdsTransportPriority AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class DdsTransportPriority(ARObject):
    """AUTOSAR DdsTransportPriority."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("transport_priority", None, True, False, None),  # transportPriority
    ]

    def __init__(self) -> None:
        """Initialize DdsTransportPriority."""
        super().__init__()
        self.transport_priority: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DdsTransportPriority to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DdsTransportPriority":
        """Create DdsTransportPriority from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DdsTransportPriority instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DdsTransportPriority since parent returns ARObject
        return cast("DdsTransportPriority", obj)


class DdsTransportPriorityBuilder:
    """Builder for DdsTransportPriority."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DdsTransportPriority = DdsTransportPriority()

    def build(self) -> DdsTransportPriority:
        """Build and return DdsTransportPriority object.

        Returns:
            DdsTransportPriority instance
        """
        # TODO: Add validation
        return self._obj
