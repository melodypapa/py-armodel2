"""DiagEventDebounceMonitorInternal AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diag_event_debounce_algorithm import (
    DiagEventDebounceAlgorithm,
)


class DiagEventDebounceMonitorInternal(DiagEventDebounceAlgorithm):
    """AUTOSAR DiagEventDebounceMonitorInternal."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
    ]

    def __init__(self) -> None:
        """Initialize DiagEventDebounceMonitorInternal."""
        super().__init__()

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagEventDebounceMonitorInternal to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagEventDebounceMonitorInternal":
        """Create DiagEventDebounceMonitorInternal from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagEventDebounceMonitorInternal instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagEventDebounceMonitorInternal since parent returns ARObject
        return cast("DiagEventDebounceMonitorInternal", obj)


class DiagEventDebounceMonitorInternalBuilder:
    """Builder for DiagEventDebounceMonitorInternal."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagEventDebounceMonitorInternal = DiagEventDebounceMonitorInternal()

    def build(self) -> DiagEventDebounceMonitorInternal:
        """Build and return DiagEventDebounceMonitorInternal object.

        Returns:
            DiagEventDebounceMonitorInternal instance
        """
        # TODO: Add validation
        return self._obj
