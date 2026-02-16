"""FloatValueVariationPoint AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject


class FloatValueVariationPoint(ARObject):
    """AUTOSAR FloatValueVariationPoint."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
    ]

    def __init__(self) -> None:
        """Initialize FloatValueVariationPoint."""
        super().__init__()

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert FloatValueVariationPoint to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FloatValueVariationPoint":
        """Create FloatValueVariationPoint from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            FloatValueVariationPoint instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to FloatValueVariationPoint since parent returns ARObject
        return cast("FloatValueVariationPoint", obj)


class FloatValueVariationPointBuilder:
    """Builder for FloatValueVariationPoint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FloatValueVariationPoint = FloatValueVariationPoint()

    def build(self) -> FloatValueVariationPoint:
        """Build and return FloatValueVariationPoint object.

        Returns:
            FloatValueVariationPoint instance
        """
        # TODO: Add validation
        return self._obj
