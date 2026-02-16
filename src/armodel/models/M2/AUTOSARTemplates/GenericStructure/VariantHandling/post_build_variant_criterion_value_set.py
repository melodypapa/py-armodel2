"""PostBuildVariantCriterionValueSet AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)


class PostBuildVariantCriterionValueSet(ARElement):
    """AUTOSAR PostBuildVariantCriterionValueSet."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("post_build_variants", None, False, True, any (PostBuildVariant)),  # postBuildVariants
    ]

    def __init__(self) -> None:
        """Initialize PostBuildVariantCriterionValueSet."""
        super().__init__()
        self.post_build_variants: list[Any] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert PostBuildVariantCriterionValueSet to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "PostBuildVariantCriterionValueSet":
        """Create PostBuildVariantCriterionValueSet from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            PostBuildVariantCriterionValueSet instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to PostBuildVariantCriterionValueSet since parent returns ARObject
        return cast("PostBuildVariantCriterionValueSet", obj)


class PostBuildVariantCriterionValueSetBuilder:
    """Builder for PostBuildVariantCriterionValueSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PostBuildVariantCriterionValueSet = PostBuildVariantCriterionValueSet()

    def build(self) -> PostBuildVariantCriterionValueSet:
        """Build and return PostBuildVariantCriterionValueSet object.

        Returns:
            PostBuildVariantCriterionValueSet instance
        """
        # TODO: Add validation
        return self._obj
