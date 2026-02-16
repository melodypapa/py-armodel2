"""ExclusiveArea AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)


class ExclusiveArea(Identifiable):
    """AUTOSAR ExclusiveArea."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
    ]

    def __init__(self) -> None:
        """Initialize ExclusiveArea."""
        super().__init__()

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ExclusiveArea to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ExclusiveArea":
        """Create ExclusiveArea from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ExclusiveArea instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ExclusiveArea since parent returns ARObject
        return cast("ExclusiveArea", obj)


class ExclusiveAreaBuilder:
    """Builder for ExclusiveArea."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ExclusiveArea = ExclusiveArea()

    def build(self) -> ExclusiveArea:
        """Build and return ExclusiveArea object.

        Returns:
            ExclusiveArea instance
        """
        # TODO: Add validation
        return self._obj
