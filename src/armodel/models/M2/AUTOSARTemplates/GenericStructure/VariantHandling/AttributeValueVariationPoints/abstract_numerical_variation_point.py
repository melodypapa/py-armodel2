"""AbstractNumericalVariationPoint AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject


class AbstractNumericalVariationPoint(ARObject):
    """AUTOSAR AbstractNumericalVariationPoint."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
    ]

    def __init__(self) -> None:
        """Initialize AbstractNumericalVariationPoint."""
        super().__init__()

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert AbstractNumericalVariationPoint to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AbstractNumericalVariationPoint":
        """Create AbstractNumericalVariationPoint from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            AbstractNumericalVariationPoint instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to AbstractNumericalVariationPoint since parent returns ARObject
        return cast("AbstractNumericalVariationPoint", obj)


class AbstractNumericalVariationPointBuilder:
    """Builder for AbstractNumericalVariationPoint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AbstractNumericalVariationPoint = AbstractNumericalVariationPoint()

    def build(self) -> AbstractNumericalVariationPoint:
        """Build and return AbstractNumericalVariationPoint object.

        Returns:
            AbstractNumericalVariationPoint instance
        """
        # TODO: Add validation
        return self._obj
