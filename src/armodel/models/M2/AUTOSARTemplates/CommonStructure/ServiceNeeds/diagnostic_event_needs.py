"""DiagnosticEventNeeds AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_capability_element import (
    DiagnosticCapabilityElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.function_inhibition_needs import (
    FunctionInhibitionNeeds,
)


class DiagnosticEventNeeds(DiagnosticCapabilityElement):
    """AUTOSAR DiagnosticEventNeeds."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("deferring_fids", None, False, True, FunctionInhibitionNeeds),  # deferringFids
        ("diag_event_debounce", None, False, False, any (DiagEventDebounce)),  # diagEventDebounce
        ("inhibiting_fid", None, False, False, FunctionInhibitionNeeds),  # inhibitingFid
        ("inhibitings", None, False, True, FunctionInhibitionNeeds),  # inhibitings
        ("prestored", None, True, False, None),  # prestored
        ("uses_monitor", None, True, False, None),  # usesMonitor
    ]

    def __init__(self) -> None:
        """Initialize DiagnosticEventNeeds."""
        super().__init__()
        self.deferring_fids: list[FunctionInhibitionNeeds] = []
        self.diag_event_debounce: Optional[Any] = None
        self.inhibiting_fid: Optional[FunctionInhibitionNeeds] = None
        self.inhibitings: list[FunctionInhibitionNeeds] = []
        self.prestored: Optional[Boolean] = None
        self.uses_monitor: Optional[Boolean] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DiagnosticEventNeeds to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticEventNeeds":
        """Create DiagnosticEventNeeds from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DiagnosticEventNeeds instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DiagnosticEventNeeds since parent returns ARObject
        return cast("DiagnosticEventNeeds", obj)


class DiagnosticEventNeedsBuilder:
    """Builder for DiagnosticEventNeeds."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticEventNeeds = DiagnosticEventNeeds()

    def build(self) -> DiagnosticEventNeeds:
        """Build and return DiagnosticEventNeeds object.

        Returns:
            DiagnosticEventNeeds instance
        """
        # TODO: Add validation
        return self._obj
