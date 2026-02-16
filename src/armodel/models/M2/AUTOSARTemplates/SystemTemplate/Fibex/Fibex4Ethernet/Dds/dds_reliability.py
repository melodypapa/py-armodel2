"""DdsReliability AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Float,
)


class DdsReliability(ARObject):
    """AUTOSAR DdsReliability."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("reliability_kind", None, False, False, DdsReliabilityKindEnum),  # reliabilityKind
        ("reliability_max", None, True, False, None),  # reliabilityMax
    ]

    def __init__(self) -> None:
        """Initialize DdsReliability."""
        super().__init__()
        self.reliability_kind: Optional[DdsReliabilityKindEnum] = None
        self.reliability_max: Optional[Float] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DdsReliability to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DdsReliability":
        """Create DdsReliability from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DdsReliability instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DdsReliability since parent returns ARObject
        return cast("DdsReliability", obj)


class DdsReliabilityBuilder:
    """Builder for DdsReliability."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DdsReliability = DdsReliability()

    def build(self) -> DdsReliability:
        """Build and return DdsReliability object.

        Returns:
            DdsReliability instance
        """
        # TODO: Add validation
        return self._obj
