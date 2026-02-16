"""IntegerValueVariationPoint AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject


class IntegerValueVariationPoint(ARObject):
    """AUTOSAR IntegerValueVariationPoint."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
    ]

    def __init__(self) -> None:
        """Initialize IntegerValueVariationPoint."""
        super().__init__()

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert IntegerValueVariationPoint to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "IntegerValueVariationPoint":
        """Create IntegerValueVariationPoint from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            IntegerValueVariationPoint instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to IntegerValueVariationPoint since parent returns ARObject
        return cast("IntegerValueVariationPoint", obj)


class IntegerValueVariationPointBuilder:
    """Builder for IntegerValueVariationPoint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IntegerValueVariationPoint = IntegerValueVariationPoint()

    def build(self) -> IntegerValueVariationPoint:
        """Build and return IntegerValueVariationPoint object.

        Returns:
            IntegerValueVariationPoint instance
        """
        # TODO: Add validation
        return self._obj
