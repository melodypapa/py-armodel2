"""NetworkSegmentIdentification AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class NetworkSegmentIdentification(ARObject):
    """AUTOSAR NetworkSegmentIdentification."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("network", None, True, False, None),  # network
    ]

    def __init__(self) -> None:
        """Initialize NetworkSegmentIdentification."""
        super().__init__()
        self.network: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert NetworkSegmentIdentification to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "NetworkSegmentIdentification":
        """Create NetworkSegmentIdentification from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            NetworkSegmentIdentification instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to NetworkSegmentIdentification since parent returns ARObject
        return cast("NetworkSegmentIdentification", obj)


class NetworkSegmentIdentificationBuilder:
    """Builder for NetworkSegmentIdentification."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: NetworkSegmentIdentification = NetworkSegmentIdentification()

    def build(self) -> NetworkSegmentIdentification:
        """Build and return NetworkSegmentIdentification object.

        Returns:
            NetworkSegmentIdentification instance
        """
        # TODO: Add validation
        return self._obj
