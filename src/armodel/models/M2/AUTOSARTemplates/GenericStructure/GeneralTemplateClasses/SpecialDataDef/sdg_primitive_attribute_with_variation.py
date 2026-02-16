"""SdgPrimitiveAttributeWithVariation AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.SpecialDataDef.sdg_abstract_primitive_attribute import (
    SdgAbstractPrimitiveAttribute,
)


class SdgPrimitiveAttributeWithVariation(SdgAbstractPrimitiveAttribute):
    """AUTOSAR SdgPrimitiveAttributeWithVariation."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
    ]

    def __init__(self) -> None:
        """Initialize SdgPrimitiveAttributeWithVariation."""
        super().__init__()

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SdgPrimitiveAttributeWithVariation to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SdgPrimitiveAttributeWithVariation":
        """Create SdgPrimitiveAttributeWithVariation from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SdgPrimitiveAttributeWithVariation instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SdgPrimitiveAttributeWithVariation since parent returns ARObject
        return cast("SdgPrimitiveAttributeWithVariation", obj)


class SdgPrimitiveAttributeWithVariationBuilder:
    """Builder for SdgPrimitiveAttributeWithVariation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SdgPrimitiveAttributeWithVariation = SdgPrimitiveAttributeWithVariation()

    def build(self) -> SdgPrimitiveAttributeWithVariation:
        """Build and return SdgPrimitiveAttributeWithVariation object.

        Returns:
            SdgPrimitiveAttributeWithVariation instance
        """
        # TODO: Add validation
        return self._obj
