"""SdgAggregationWithVariation AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.SpecialDataDef.sdg_element_with_gid import (
    SdgElementWithGid,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.SpecialDataDef.sdg_class import (
    SdgClass,
)


class SdgAggregationWithVariation(SdgElementWithGid):
    """AUTOSAR SdgAggregationWithVariation."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("sub_sdg", None, False, False, SdgClass),  # subSdg
    ]

    def __init__(self) -> None:
        """Initialize SdgAggregationWithVariation."""
        super().__init__()
        self.sub_sdg: Optional[SdgClass] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SdgAggregationWithVariation to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SdgAggregationWithVariation":
        """Create SdgAggregationWithVariation from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SdgAggregationWithVariation instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SdgAggregationWithVariation since parent returns ARObject
        return cast("SdgAggregationWithVariation", obj)


class SdgAggregationWithVariationBuilder:
    """Builder for SdgAggregationWithVariation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SdgAggregationWithVariation = SdgAggregationWithVariation()

    def build(self) -> SdgAggregationWithVariation:
        """Build and return SdgAggregationWithVariation object.

        Returns:
            SdgAggregationWithVariation instance
        """
        # TODO: Add validation
        return self._obj
