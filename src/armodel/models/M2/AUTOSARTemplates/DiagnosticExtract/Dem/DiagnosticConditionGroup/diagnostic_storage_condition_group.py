"""DiagnosticStorageConditionGroup AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticConditionGroup.diagnostic_condition_group import (
    DiagnosticConditionGroup,
)


class DiagnosticStorageConditionGroup(DiagnosticConditionGroup):
    """AUTOSAR DiagnosticStorageConditionGroup."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("storages", None, False, True, any (DiagnosticStorage)),  # storages
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticStorageConditionGroup."""
        super().__init__()
        self.storages: list[Any] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticStorageConditionGroup to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticStorageConditionGroup":
        """Create DiagnosticStorageConditionGroup from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticStorageConditionGroup instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticStorageConditionGroup since parent returns ARObject
        return cast("DiagnosticStorageConditionGroup", obj)


class DiagnosticStorageConditionGroupBuilder:
    """Builder for DiagnosticStorageConditionGroup."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticStorageConditionGroup = DiagnosticStorageConditionGroup()

    def build(self) -> DiagnosticStorageConditionGroup:
        """Build and return DiagnosticStorageConditionGroup object.

        Returns:
            DiagnosticStorageConditionGroup instance
        """
        # TODO: Add validation
        return self._obj
