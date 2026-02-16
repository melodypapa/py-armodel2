"""TransformationPropsSet AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.transformation_props import (
    TransformationProps,
)


class TransformationPropsSet(ARElement):
    """AUTOSAR TransformationPropsSet."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("transformation_props_propses", None, False, True, TransformationProps),  # transformationPropsPropses
    ]

    def __init__(self) -> None:
        """Initialize TransformationPropsSet."""
        super().__init__()
        self.transformation_props_propses: list[TransformationProps] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert TransformationPropsSet to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TransformationPropsSet":
        """Create TransformationPropsSet from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            TransformationPropsSet instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to TransformationPropsSet since parent returns ARObject
        return cast("TransformationPropsSet", obj)


class TransformationPropsSetBuilder:
    """Builder for TransformationPropsSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TransformationPropsSet = TransformationPropsSet()

    def build(self) -> TransformationPropsSet:
        """Build and return TransformationPropsSet object.

        Returns:
            TransformationPropsSet instance
        """
        # TODO: Add validation
        return self._obj
