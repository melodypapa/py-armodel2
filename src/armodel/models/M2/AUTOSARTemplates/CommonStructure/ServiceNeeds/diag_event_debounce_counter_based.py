"""DiagEventDebounceCounterBased AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diag_event_debounce_algorithm import (
    DiagEventDebounceAlgorithm,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)


class DiagEventDebounceCounterBased(DiagEventDebounceAlgorithm):
    """AUTOSAR DiagEventDebounceCounterBased."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("counter_based", None, True, False, None),  # counterBased
        ("counter", None, True, False, None),  # counter
        ("counter_failed", None, True, False, None),  # counterFailed
        ("counter_jump", None, True, False, None),  # counterJump
        ("counter_jump_up", None, True, False, None),  # counterJumpUp
        ("counter_passed", None, True, False, None),  # counterPassed
    ]

    def __init__(self) -> None:
        """Initialize DiagEventDebounceCounterBased."""
        super().__init__()
        self.counter_based: Optional[Integer] = None
        self.counter: Optional[Integer] = None
        self.counter_failed: Optional[Integer] = None
        self.counter_jump: Optional[Integer] = None
        self.counter_jump_up: Optional[Integer] = None
        self.counter_passed: Optional[Integer] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagEventDebounceCounterBased to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagEventDebounceCounterBased":
        """Create DiagEventDebounceCounterBased from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagEventDebounceCounterBased instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagEventDebounceCounterBased since parent returns ARObject
        return cast("DiagEventDebounceCounterBased", obj)


class DiagEventDebounceCounterBasedBuilder:
    """Builder for DiagEventDebounceCounterBased."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagEventDebounceCounterBased = DiagEventDebounceCounterBased()

    def build(self) -> DiagEventDebounceCounterBased:
        """Build and return DiagEventDebounceCounterBased object.

        Returns:
            DiagEventDebounceCounterBased instance
        """
        # TODO: Add validation
        return self._obj
