"""PostBuildVariantCondition AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)


class PostBuildVariantCondition(ARObject):
    """AUTOSAR PostBuildVariantCondition."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("matching", None, False, False, any (PostBuildVariant)),  # matching
        ("value", None, True, False, None),  # value
    ]

    def __init__(self) -> None:
        """Initialize PostBuildVariantCondition."""
        super().__init__()
        self.matching: Any = None
        self.value: Integer = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert PostBuildVariantCondition to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "PostBuildVariantCondition":
        """Create PostBuildVariantCondition from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            PostBuildVariantCondition instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to PostBuildVariantCondition since parent returns ARObject
        return cast("PostBuildVariantCondition", obj)


class PostBuildVariantConditionBuilder:
    """Builder for PostBuildVariantCondition."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PostBuildVariantCondition = PostBuildVariantCondition()

    def build(self) -> PostBuildVariantCondition:
        """Build and return PostBuildVariantCondition object.

        Returns:
            PostBuildVariantCondition instance
        """
        # TODO: Add validation
        return self._obj
