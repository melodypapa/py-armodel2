"""SdgAbstractPrimitiveAttribute AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.SpecialDataDef.sdg_element_with_gid import (
    SdgElementWithGid,
)


class SdgAbstractPrimitiveAttribute(SdgElementWithGid):
    """AUTOSAR SdgAbstractPrimitiveAttribute."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
    ]

    def __init__(self) -> None:
        """Initialize SdgAbstractPrimitiveAttribute."""
        super().__init__()

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SdgAbstractPrimitiveAttribute to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SdgAbstractPrimitiveAttribute":
        """Create SdgAbstractPrimitiveAttribute from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SdgAbstractPrimitiveAttribute instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SdgAbstractPrimitiveAttribute since parent returns ARObject
        return cast("SdgAbstractPrimitiveAttribute", obj)


class SdgAbstractPrimitiveAttributeBuilder:
    """Builder for SdgAbstractPrimitiveAttribute."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SdgAbstractPrimitiveAttribute = SdgAbstractPrimitiveAttribute()

    def build(self) -> SdgAbstractPrimitiveAttribute:
        """Build and return SdgAbstractPrimitiveAttribute object.

        Returns:
            SdgAbstractPrimitiveAttribute instance
        """
        # TODO: Add validation
        return self._obj
