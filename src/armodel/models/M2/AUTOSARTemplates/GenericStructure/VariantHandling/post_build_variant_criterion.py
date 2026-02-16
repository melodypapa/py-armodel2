"""PostBuildVariantCriterion AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.MSR.AsamHdo.ComputationMethod.compu_method import (
    CompuMethod,
)


class PostBuildVariantCriterion(ARElement):
    """AUTOSAR PostBuildVariantCriterion."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("compu_method", None, False, False, CompuMethod),  # compuMethod
    ]

    def __init__(self) -> None:
        """Initialize PostBuildVariantCriterion."""
        super().__init__()
        self.compu_method: CompuMethod = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert PostBuildVariantCriterion to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "PostBuildVariantCriterion":
        """Create PostBuildVariantCriterion from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            PostBuildVariantCriterion instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to PostBuildVariantCriterion since parent returns ARObject
        return cast("PostBuildVariantCriterion", obj)


class PostBuildVariantCriterionBuilder:
    """Builder for PostBuildVariantCriterion."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PostBuildVariantCriterion = PostBuildVariantCriterion()

    def build(self) -> PostBuildVariantCriterion:
        """Build and return PostBuildVariantCriterion object.

        Returns:
            PostBuildVariantCriterion instance
        """
        # TODO: Add validation
        return self._obj
