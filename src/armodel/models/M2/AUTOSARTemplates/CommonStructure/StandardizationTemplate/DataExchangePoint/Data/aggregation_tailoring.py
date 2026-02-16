"""AggregationTailoring AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.attribute_tailoring import (
    AttributeTailoring,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.class_tailoring import (
    ClassTailoring,
)


class AggregationTailoring(AttributeTailoring):
    """AUTOSAR AggregationTailoring."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("type_tailorings", None, False, True, ClassTailoring),  # typeTailorings
    ]

    def __init__(self) -> None:
        """Initialize AggregationTailoring."""
        super().__init__()
        self.type_tailorings: list[ClassTailoring] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert AggregationTailoring to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AggregationTailoring":
        """Create AggregationTailoring from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            AggregationTailoring instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to AggregationTailoring since parent returns ARObject
        return cast("AggregationTailoring", obj)


class AggregationTailoringBuilder:
    """Builder for AggregationTailoring."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AggregationTailoring = AggregationTailoring()

    def build(self) -> AggregationTailoring:
        """Build and return AggregationTailoring object.

        Returns:
            AggregationTailoring instance
        """
        # TODO: Add validation
        return self._obj
