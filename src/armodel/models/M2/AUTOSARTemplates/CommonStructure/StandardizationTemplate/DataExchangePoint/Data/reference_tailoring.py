"""ReferenceTailoring AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.attribute_tailoring import (
    AttributeTailoring,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.class_tailoring import (
    ClassTailoring,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.unresolved_reference_restriction_with_severity import (
    UnresolvedReferenceRestrictionWithSeverity,
)


class ReferenceTailoring(AttributeTailoring):
    """AUTOSAR ReferenceTailoring."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("type_tailorings", None, False, True, ClassTailoring),  # typeTailorings
        ("unresolved_restriction", None, False, False, UnresolvedReferenceRestrictionWithSeverity),  # unresolvedRestriction
    ]

    def __init__(self) -> None:
        """Initialize ReferenceTailoring."""
        super().__init__()
        self.type_tailorings: list[ClassTailoring] = []
        self.unresolved_restriction: Optional[UnresolvedReferenceRestrictionWithSeverity] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ReferenceTailoring to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ReferenceTailoring":
        """Create ReferenceTailoring from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ReferenceTailoring instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ReferenceTailoring since parent returns ARObject
        return cast("ReferenceTailoring", obj)


class ReferenceTailoringBuilder:
    """Builder for ReferenceTailoring."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ReferenceTailoring = ReferenceTailoring()

    def build(self) -> ReferenceTailoring:
        """Build and return ReferenceTailoring object.

        Returns:
            ReferenceTailoring instance
        """
        # TODO: Add validation
        return self._obj
