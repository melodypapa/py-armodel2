"""PrimitiveAttributeTailoring AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.attribute_tailoring import (
    AttributeTailoring,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.value_restriction_with_severity import (
    ValueRestrictionWithSeverity,
)


class PrimitiveAttributeTailoring(AttributeTailoring):
    """AUTOSAR PrimitiveAttributeTailoring."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("default_value", None, False, False, DefaultValueApplicationStrategyEnum),  # defaultValue
        ("sub_attributes", None, False, True, any (PrimitiveAttribute)),  # subAttributes
        ("value_restriction_with_severity", None, False, False, ValueRestrictionWithSeverity),  # valueRestrictionWithSeverity
    ]

    def __init__(self) -> None:
        """Initialize PrimitiveAttributeTailoring."""
        super().__init__()
        self.default_value: Optional[DefaultValueApplicationStrategyEnum] = None
        self.sub_attributes: list[Any] = []
        self.value_restriction_with_severity: Optional[ValueRestrictionWithSeverity] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert PrimitiveAttributeTailoring to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "PrimitiveAttributeTailoring":
        """Create PrimitiveAttributeTailoring from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            PrimitiveAttributeTailoring instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to PrimitiveAttributeTailoring since parent returns ARObject
        return cast("PrimitiveAttributeTailoring", obj)


class PrimitiveAttributeTailoringBuilder:
    """Builder for PrimitiveAttributeTailoring."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PrimitiveAttributeTailoring = PrimitiveAttributeTailoring()

    def build(self) -> PrimitiveAttributeTailoring:
        """Build and return PrimitiveAttributeTailoring object.

        Returns:
            PrimitiveAttributeTailoring instance
        """
        # TODO: Add validation
        return self._obj
