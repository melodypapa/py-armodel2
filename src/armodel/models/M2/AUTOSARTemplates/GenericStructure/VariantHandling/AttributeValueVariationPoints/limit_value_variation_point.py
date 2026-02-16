"""LimitValueVariationPoint AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject


class LimitValueVariationPoint(ARObject):
    """AUTOSAR LimitValueVariationPoint."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("interval_type_enum", None, False, False, IntervalTypeEnum),  # intervalTypeEnum
    ]

    def __init__(self) -> None:
        """Initialize LimitValueVariationPoint."""
        super().__init__()
        self.interval_type_enum: Optional[IntervalTypeEnum] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert LimitValueVariationPoint to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "LimitValueVariationPoint":
        """Create LimitValueVariationPoint from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            LimitValueVariationPoint instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to LimitValueVariationPoint since parent returns ARObject
        return cast("LimitValueVariationPoint", obj)


class LimitValueVariationPointBuilder:
    """Builder for LimitValueVariationPoint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: LimitValueVariationPoint = LimitValueVariationPoint()

    def build(self) -> LimitValueVariationPoint:
        """Build and return LimitValueVariationPoint object.

        Returns:
            LimitValueVariationPoint instance
        """
        # TODO: Add validation
        return self._obj
