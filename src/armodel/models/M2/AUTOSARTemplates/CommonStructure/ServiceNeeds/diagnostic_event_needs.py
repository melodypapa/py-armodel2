"""DiagnosticEventNeeds AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

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
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "deferring_fids": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=FunctionInhibitionNeeds,
        ),  # deferringFids
        "diag_event_debounce": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (DiagEventDebounce),
        ),  # diagEventDebounce
        "inhibiting_fid": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=FunctionInhibitionNeeds,
        ),  # inhibitingFid
        "inhibitings": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=FunctionInhibitionNeeds,
        ),  # inhibitings
        "prestored": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # prestored
        "uses_monitor": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # usesMonitor
    }

    def __init__(self) -> None:
        """Initialize DiagnosticEventNeeds."""
        super().__init__()
        self.deferring_fids: list[FunctionInhibitionNeeds] = []
        self.diag_event_debounce: Optional[Any] = None
        self.inhibiting_fid: Optional[FunctionInhibitionNeeds] = None
        self.inhibitings: list[FunctionInhibitionNeeds] = []
        self.prestored: Optional[Boolean] = None
        self.uses_monitor: Optional[Boolean] = None


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
