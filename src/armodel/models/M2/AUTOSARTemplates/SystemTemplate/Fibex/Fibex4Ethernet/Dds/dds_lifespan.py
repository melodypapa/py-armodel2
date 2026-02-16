"""DdsLifespan AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Float,
)


class DdsLifespan(ARObject):
    """AUTOSAR DdsLifespan."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("lifespan_duration", None, True, False, None),  # lifespanDuration
    ]

    def __init__(self) -> None:
        """Initialize DdsLifespan."""
        super().__init__()
        self.lifespan_duration: Optional[Float] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DdsLifespan to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DdsLifespan":
        """Create DdsLifespan from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DdsLifespan instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DdsLifespan since parent returns ARObject
        return cast("DdsLifespan", obj)


class DdsLifespanBuilder:
    """Builder for DdsLifespan."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DdsLifespan = DdsLifespan()

    def build(self) -> DdsLifespan:
        """Build and return DdsLifespan object.

        Returns:
            DdsLifespan instance
        """
        # TODO: Add validation
        return self._obj
