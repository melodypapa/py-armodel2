"""DdsOwnershipStrength AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class DdsOwnershipStrength(ARObject):
    """AUTOSAR DdsOwnershipStrength."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("ownership", None, True, False, None),  # ownership
    ]

    def __init__(self) -> None:
        """Initialize DdsOwnershipStrength."""
        super().__init__()
        self.ownership: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DdsOwnershipStrength to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DdsOwnershipStrength":
        """Create DdsOwnershipStrength from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DdsOwnershipStrength instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DdsOwnershipStrength since parent returns ARObject
        return cast("DdsOwnershipStrength", obj)


class DdsOwnershipStrengthBuilder:
    """Builder for DdsOwnershipStrength."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DdsOwnershipStrength = DdsOwnershipStrength()

    def build(self) -> DdsOwnershipStrength:
        """Build and return DdsOwnershipStrength object.

        Returns:
            DdsOwnershipStrength instance
        """
        # TODO: Add validation
        return self._obj
