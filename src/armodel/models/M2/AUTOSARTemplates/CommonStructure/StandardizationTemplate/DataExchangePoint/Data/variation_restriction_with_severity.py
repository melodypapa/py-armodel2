"""VariationRestrictionWithSeverity AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Common.restriction_with_severity import (
    RestrictionWithSeverity,
)


class VariationRestrictionWithSeverity(RestrictionWithSeverity):
    """AUTOSAR VariationRestrictionWithSeverity."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
    ]

    def __init__(self) -> None:
        """Initialize VariationRestrictionWithSeverity."""
        super().__init__()

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert VariationRestrictionWithSeverity to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "VariationRestrictionWithSeverity":
        """Create VariationRestrictionWithSeverity from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            VariationRestrictionWithSeverity instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to VariationRestrictionWithSeverity since parent returns ARObject
        return cast("VariationRestrictionWithSeverity", obj)


class VariationRestrictionWithSeverityBuilder:
    """Builder for VariationRestrictionWithSeverity."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: VariationRestrictionWithSeverity = VariationRestrictionWithSeverity()

    def build(self) -> VariationRestrictionWithSeverity:
        """Build and return VariationRestrictionWithSeverity object.

        Returns:
            VariationRestrictionWithSeverity instance
        """
        # TODO: Add validation
        return self._obj
