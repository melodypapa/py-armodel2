"""SdgPrimitiveAttribute AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.SpecialDataDef.sdg_abstract_primitive_attribute import (
    SdgAbstractPrimitiveAttribute,
)


class SdgPrimitiveAttribute(SdgAbstractPrimitiveAttribute):
    """AUTOSAR SdgPrimitiveAttribute."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
    ]

    def __init__(self) -> None:
        """Initialize SdgPrimitiveAttribute."""
        super().__init__()

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SdgPrimitiveAttribute to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SdgPrimitiveAttribute":
        """Create SdgPrimitiveAttribute from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SdgPrimitiveAttribute instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SdgPrimitiveAttribute since parent returns ARObject
        return cast("SdgPrimitiveAttribute", obj)


class SdgPrimitiveAttributeBuilder:
    """Builder for SdgPrimitiveAttribute."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SdgPrimitiveAttribute = SdgPrimitiveAttribute()

    def build(self) -> SdgPrimitiveAttribute:
        """Build and return SdgPrimitiveAttribute object.

        Returns:
            SdgPrimitiveAttribute instance
        """
        # TODO: Add validation
        return self._obj
