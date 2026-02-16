"""SdgForeignReferenceWithVariation AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.SpecialDataDef.sdg_abstract_foreign_reference import (
    SdgAbstractForeignReference,
)


class SdgForeignReferenceWithVariation(SdgAbstractForeignReference):
    """AUTOSAR SdgForeignReferenceWithVariation."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
    ]

    def __init__(self) -> None:
        """Initialize SdgForeignReferenceWithVariation."""
        super().__init__()

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SdgForeignReferenceWithVariation to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SdgForeignReferenceWithVariation":
        """Create SdgForeignReferenceWithVariation from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SdgForeignReferenceWithVariation instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SdgForeignReferenceWithVariation since parent returns ARObject
        return cast("SdgForeignReferenceWithVariation", obj)


class SdgForeignReferenceWithVariationBuilder:
    """Builder for SdgForeignReferenceWithVariation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SdgForeignReferenceWithVariation = SdgForeignReferenceWithVariation()

    def build(self) -> SdgForeignReferenceWithVariation:
        """Build and return SdgForeignReferenceWithVariation object.

        Returns:
            SdgForeignReferenceWithVariation instance
        """
        # TODO: Add validation
        return self._obj
