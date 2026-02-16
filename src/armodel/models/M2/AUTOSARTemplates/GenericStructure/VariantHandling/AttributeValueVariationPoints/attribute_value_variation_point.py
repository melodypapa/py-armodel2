"""AttributeValueVariationPoint AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PrimitiveIdentifier,
    String,
)


class AttributeValueVariationPoint(ARObject):
    """AUTOSAR AttributeValueVariationPoint."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("binding_time_enum", None, False, False, BindingTimeEnum),  # bindingTimeEnum
        ("blueprint_value", None, True, False, None),  # blueprintValue
        ("sd", None, True, False, None),  # sd
        ("short_label", None, True, False, None),  # shortLabel
    ]

    def __init__(self) -> None:
        """Initialize AttributeValueVariationPoint."""
        super().__init__()
        self.binding_time_enum: Optional[BindingTimeEnum] = None
        self.blueprint_value: Optional[String] = None
        self.sd: Optional[String] = None
        self.short_label: Optional[PrimitiveIdentifier] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert AttributeValueVariationPoint to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AttributeValueVariationPoint":
        """Create AttributeValueVariationPoint from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            AttributeValueVariationPoint instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to AttributeValueVariationPoint since parent returns ARObject
        return cast("AttributeValueVariationPoint", obj)


class AttributeValueVariationPointBuilder:
    """Builder for AttributeValueVariationPoint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AttributeValueVariationPoint = AttributeValueVariationPoint()

    def build(self) -> AttributeValueVariationPoint:
        """Build and return AttributeValueVariationPoint object.

        Returns:
            AttributeValueVariationPoint instance
        """
        # TODO: Add validation
        return self._obj
