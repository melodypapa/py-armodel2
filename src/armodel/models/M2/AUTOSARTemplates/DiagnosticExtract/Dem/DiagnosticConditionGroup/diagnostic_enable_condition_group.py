"""DiagnosticEnableConditionGroup AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticConditionGroup.diagnostic_condition_group import (
    DiagnosticConditionGroup,
)


class DiagnosticEnableConditionGroup(DiagnosticConditionGroup):
    """AUTOSAR DiagnosticEnableConditionGroup."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("enable_conditions", None, False, True, any (DiagnosticEnable)),  # enableConditions
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticEnableConditionGroup."""
        super().__init__()
        self.enable_conditions: list[Any] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticEnableConditionGroup to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticEnableConditionGroup":
        """Create DiagnosticEnableConditionGroup from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticEnableConditionGroup instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticEnableConditionGroup since parent returns ARObject
        return cast("DiagnosticEnableConditionGroup", obj)


class DiagnosticEnableConditionGroupBuilder:
    """Builder for DiagnosticEnableConditionGroup."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticEnableConditionGroup = DiagnosticEnableConditionGroup()

    def build(self) -> DiagnosticEnableConditionGroup:
        """Build and return DiagnosticEnableConditionGroup object.

        Returns:
            DiagnosticEnableConditionGroup instance
        """
        # TODO: Add validation
        return self._obj
