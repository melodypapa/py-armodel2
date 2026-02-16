"""SpecElementScope AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Common.spec_element_reference import (
    SpecElementReference,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)


class SpecElementScope(SpecElementReference):
    """AUTOSAR SpecElementScope."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("in_scope", None, True, False, None),  # inScope
    ]

    def __init__(self) -> None:
        """Initialize SpecElementScope."""
        super().__init__()
        self.in_scope: Optional[Boolean] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SpecElementScope to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SpecElementScope":
        """Create SpecElementScope from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SpecElementScope instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SpecElementScope since parent returns ARObject
        return cast("SpecElementScope", obj)


class SpecElementScopeBuilder:
    """Builder for SpecElementScope."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SpecElementScope = SpecElementScope()

    def build(self) -> SpecElementScope:
        """Build and return SpecElementScope object.

        Returns:
            SpecElementScope instance
        """
        # TODO: Add validation
        return self._obj
