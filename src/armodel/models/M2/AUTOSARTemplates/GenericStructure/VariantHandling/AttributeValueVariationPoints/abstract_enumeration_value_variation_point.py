"""AbstractEnumerationValueVariationPoint AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
    Ref,
)


class AbstractEnumerationValueVariationPoint(ARObject):
    """AUTOSAR AbstractEnumerationValueVariationPoint."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("base", None, True, False, None),  # base
        ("enum_table", None, True, False, None),  # enumTable
    ]

    def __init__(self) -> None:
        """Initialize AbstractEnumerationValueVariationPoint."""
        super().__init__()
        self.base: Optional[Identifier] = None
        self.enum_table: Optional[Ref] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert AbstractEnumerationValueVariationPoint to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AbstractEnumerationValueVariationPoint":
        """Create AbstractEnumerationValueVariationPoint from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            AbstractEnumerationValueVariationPoint instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to AbstractEnumerationValueVariationPoint since parent returns ARObject
        return cast("AbstractEnumerationValueVariationPoint", obj)


class AbstractEnumerationValueVariationPointBuilder:
    """Builder for AbstractEnumerationValueVariationPoint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AbstractEnumerationValueVariationPoint = AbstractEnumerationValueVariationPoint()

    def build(self) -> AbstractEnumerationValueVariationPoint:
        """Build and return AbstractEnumerationValueVariationPoint object.

        Returns:
            AbstractEnumerationValueVariationPoint instance
        """
        # TODO: Add validation
        return self._obj
