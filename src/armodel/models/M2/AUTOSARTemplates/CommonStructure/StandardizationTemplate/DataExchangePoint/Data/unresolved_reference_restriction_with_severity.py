"""UnresolvedReferenceRestrictionWithSeverity AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Common.restriction_with_severity import (
    RestrictionWithSeverity,
)


class UnresolvedReferenceRestrictionWithSeverity(RestrictionWithSeverity):
    """AUTOSAR UnresolvedReferenceRestrictionWithSeverity."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
    ]

    def __init__(self) -> None:
        """Initialize UnresolvedReferenceRestrictionWithSeverity."""
        super().__init__()

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert UnresolvedReferenceRestrictionWithSeverity to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "UnresolvedReferenceRestrictionWithSeverity":
        """Create UnresolvedReferenceRestrictionWithSeverity from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            UnresolvedReferenceRestrictionWithSeverity instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to UnresolvedReferenceRestrictionWithSeverity since parent returns ARObject
        return cast("UnresolvedReferenceRestrictionWithSeverity", obj)


class UnresolvedReferenceRestrictionWithSeverityBuilder:
    """Builder for UnresolvedReferenceRestrictionWithSeverity."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: UnresolvedReferenceRestrictionWithSeverity = UnresolvedReferenceRestrictionWithSeverity()

    def build(self) -> UnresolvedReferenceRestrictionWithSeverity:
        """Build and return UnresolvedReferenceRestrictionWithSeverity object.

        Returns:
            UnresolvedReferenceRestrictionWithSeverity instance
        """
        # TODO: Add validation
        return self._obj
