"""MultiplicityRestrictionWithSeverity AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Common.restriction_with_severity import (
    RestrictionWithSeverity,
)


class MultiplicityRestrictionWithSeverity(RestrictionWithSeverity):
    """AUTOSAR MultiplicityRestrictionWithSeverity."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
    ]

    def __init__(self) -> None:
        """Initialize MultiplicityRestrictionWithSeverity."""
        super().__init__()

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert MultiplicityRestrictionWithSeverity to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "MultiplicityRestrictionWithSeverity":
        """Create MultiplicityRestrictionWithSeverity from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            MultiplicityRestrictionWithSeverity instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to MultiplicityRestrictionWithSeverity since parent returns ARObject
        return cast("MultiplicityRestrictionWithSeverity", obj)


class MultiplicityRestrictionWithSeverityBuilder:
    """Builder for MultiplicityRestrictionWithSeverity."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: MultiplicityRestrictionWithSeverity = MultiplicityRestrictionWithSeverity()

    def build(self) -> MultiplicityRestrictionWithSeverity:
        """Build and return MultiplicityRestrictionWithSeverity object.

        Returns:
            MultiplicityRestrictionWithSeverity instance
        """
        # TODO: Add validation
        return self._obj
