"""AtpType AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)


class AtpType(Identifiable):
    """AUTOSAR AtpType."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
    ]

    def __init__(self) -> None:
        """Initialize AtpType."""
        super().__init__()

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert AtpType to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AtpType":
        """Create AtpType from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            AtpType instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to AtpType since parent returns ARObject
        return cast("AtpType", obj)


class AtpTypeBuilder:
    """Builder for AtpType."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AtpType = AtpType()

    def build(self) -> AtpType:
        """Build and return AtpType object.

        Returns:
            AtpType instance
        """
        # TODO: Add validation
        return self._obj
