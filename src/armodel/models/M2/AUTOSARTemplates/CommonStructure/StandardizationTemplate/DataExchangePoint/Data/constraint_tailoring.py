"""ConstraintTailoring AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Common.restriction_with_severity import (
    RestrictionWithSeverity,
)
from armodel.models.M2.MSR.Documentation.BlockElements.RequirementsTracing.traceable_text import (
    TraceableText,
)


class ConstraintTailoring(RestrictionWithSeverity):
    """AUTOSAR ConstraintTailoring."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("constraint", None, False, False, TraceableText),  # constraint
    ]

    def __init__(self) -> None:
        """Initialize ConstraintTailoring."""
        super().__init__()
        self.constraint: Optional[TraceableText] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ConstraintTailoring to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ConstraintTailoring":
        """Create ConstraintTailoring from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ConstraintTailoring instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ConstraintTailoring since parent returns ARObject
        return cast("ConstraintTailoring", obj)


class ConstraintTailoringBuilder:
    """Builder for ConstraintTailoring."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ConstraintTailoring = ConstraintTailoring()

    def build(self) -> ConstraintTailoring:
        """Build and return ConstraintTailoring object.

        Returns:
            ConstraintTailoring instance
        """
        # TODO: Add validation
        return self._obj
