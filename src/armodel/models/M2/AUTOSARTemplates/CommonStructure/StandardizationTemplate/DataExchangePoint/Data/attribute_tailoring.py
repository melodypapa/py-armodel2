"""AttributeTailoring AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.data_format_element_scope import (
    DataFormatElementScope,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.variation_restriction_with_severity import (
    VariationRestrictionWithSeverity,
)


class AttributeTailoring(DataFormatElementScope):
    """AUTOSAR AttributeTailoring."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("multiplicity", None, False, False, any (MultiplicityRestriction)),  # multiplicity
        ("variation", None, False, False, VariationRestrictionWithSeverity),  # variation
    ]

    def __init__(self) -> None:
        """Initialize AttributeTailoring."""
        super().__init__()
        self.multiplicity: Optional[Any] = None
        self.variation: Optional[VariationRestrictionWithSeverity] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert AttributeTailoring to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AttributeTailoring":
        """Create AttributeTailoring from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            AttributeTailoring instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to AttributeTailoring since parent returns ARObject
        return cast("AttributeTailoring", obj)


class AttributeTailoringBuilder:
    """Builder for AttributeTailoring."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AttributeTailoring = AttributeTailoring()

    def build(self) -> AttributeTailoring:
        """Build and return AttributeTailoring object.

        Returns:
            AttributeTailoring instance
        """
        # TODO: Add validation
        return self._obj
