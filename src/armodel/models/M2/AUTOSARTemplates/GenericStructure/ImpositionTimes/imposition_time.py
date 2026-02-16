"""ImpositionTime AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)


class ImpositionTime(Identifiable):
    """AUTOSAR ImpositionTime."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
    ]

    def __init__(self) -> None:
        """Initialize ImpositionTime."""
        super().__init__()

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ImpositionTime to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ImpositionTime":
        """Create ImpositionTime from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ImpositionTime instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ImpositionTime since parent returns ARObject
        return cast("ImpositionTime", obj)


class ImpositionTimeBuilder:
    """Builder for ImpositionTime."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ImpositionTime = ImpositionTime()

    def build(self) -> ImpositionTime:
        """Build and return ImpositionTime object.

        Returns:
            ImpositionTime instance
        """
        # TODO: Add validation
        return self._obj
