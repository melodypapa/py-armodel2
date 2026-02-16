"""DiagEventDebounceTimeBased AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diag_event_debounce_algorithm import (
    DiagEventDebounceAlgorithm,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)


class DiagEventDebounceTimeBased(DiagEventDebounceAlgorithm):
    """AUTOSAR DiagEventDebounceTimeBased."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("time_based_fdc", None, True, False, None),  # timeBasedFdc
        ("time_failed", None, True, False, None),  # timeFailed
        ("time_passed", None, True, False, None),  # timePassed
    ]

    def __init__(self) -> None:
        """Initialize DiagEventDebounceTimeBased."""
        super().__init__()
        self.time_based_fdc: Optional[TimeValue] = None
        self.time_failed: Optional[TimeValue] = None
        self.time_passed: Optional[TimeValue] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagEventDebounceTimeBased to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagEventDebounceTimeBased":
        """Create DiagEventDebounceTimeBased from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagEventDebounceTimeBased instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagEventDebounceTimeBased since parent returns ARObject
        return cast("DiagEventDebounceTimeBased", obj)


class DiagEventDebounceTimeBasedBuilder:
    """Builder for DiagEventDebounceTimeBased."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagEventDebounceTimeBased = DiagEventDebounceTimeBased()

    def build(self) -> DiagEventDebounceTimeBased:
        """Build and return DiagEventDebounceTimeBased object.

        Returns:
            DiagEventDebounceTimeBased instance
        """
        # TODO: Add validation
        return self._obj
