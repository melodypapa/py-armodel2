"""DiagnosticIoControlNeeds AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_capability_element import (
    DiagnosticCapabilityElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_value_needs import (
    DiagnosticValueNeeds,
)


class DiagnosticIoControlNeeds(DiagnosticCapabilityElement):
    """AUTOSAR DiagnosticIoControlNeeds."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "current_value": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DiagnosticValueNeeds,
        ),  # currentValue
        "freeze_current": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # freezeCurrent
        "reset_to_default": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # resetToDefault
        "short_term": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # shortTerm
    }

    def __init__(self) -> None:
        """Initialize DiagnosticIoControlNeeds."""
        super().__init__()
        self.current_value: Optional[DiagnosticValueNeeds] = None
        self.freeze_current: Optional[Boolean] = None
        self.reset_to_default: Optional[Boolean] = None
        self.short_term: Optional[Boolean] = None


class DiagnosticIoControlNeedsBuilder:
    """Builder for DiagnosticIoControlNeeds."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticIoControlNeeds = DiagnosticIoControlNeeds()

    def build(self) -> DiagnosticIoControlNeeds:
        """Build and return DiagnosticIoControlNeeds object.

        Returns:
            DiagnosticIoControlNeeds instance
        """
        # TODO: Add validation
        return self._obj
