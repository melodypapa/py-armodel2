"""DdsLiveliness AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Float,
)


class DdsLiveliness(ARObject):
    """AUTOSAR DdsLiveliness."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("liveliness_lease", None, True, False, None),  # livelinessLease
        ("liveness_kind", None, False, False, DdsLivenessKindEnum),  # livenessKind
    ]

    def __init__(self) -> None:
        """Initialize DdsLiveliness."""
        super().__init__()
        self.liveliness_lease: Optional[Float] = None
        self.liveness_kind: Optional[DdsLivenessKindEnum] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DdsLiveliness to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DdsLiveliness":
        """Create DdsLiveliness from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DdsLiveliness instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DdsLiveliness since parent returns ARObject
        return cast("DdsLiveliness", obj)


class DdsLivelinessBuilder:
    """Builder for DdsLiveliness."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DdsLiveliness = DdsLiveliness()

    def build(self) -> DdsLiveliness:
        """Build and return DdsLiveliness object.

        Returns:
            DdsLiveliness instance
        """
        # TODO: Add validation
        return self._obj
