"""ReferenceCondition AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.attribute_condition import (
    AttributeCondition,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.reference_tailoring import (
    ReferenceTailoring,
)


class ReferenceCondition(AttributeCondition):
    """AUTOSAR ReferenceCondition."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("reference", None, False, False, ReferenceTailoring),  # reference
    ]

    def __init__(self) -> None:
        """Initialize ReferenceCondition."""
        super().__init__()
        self.reference: ReferenceTailoring = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ReferenceCondition to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ReferenceCondition":
        """Create ReferenceCondition from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ReferenceCondition instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ReferenceCondition since parent returns ARObject
        return cast("ReferenceCondition", obj)


class ReferenceConditionBuilder:
    """Builder for ReferenceCondition."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ReferenceCondition = ReferenceCondition()

    def build(self) -> ReferenceCondition:
        """Build and return ReferenceCondition object.

        Returns:
            ReferenceCondition instance
        """
        # TODO: Add validation
        return self._obj
