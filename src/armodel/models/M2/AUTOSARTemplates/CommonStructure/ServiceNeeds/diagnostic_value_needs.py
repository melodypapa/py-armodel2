"""DiagnosticValueNeeds AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 245)
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 114)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 782)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_capability_element import (
    DiagnosticCapabilityElement,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import (
    DiagnosticProcessingStyleEnum,
    DiagnosticValueAccessEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)


class DiagnosticValueNeeds(DiagnosticCapabilityElement):
    """AUTOSAR DiagnosticValueNeeds."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "data_length": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # dataLength
        "diagnostic_value_access": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DiagnosticValueAccessEnum,
        ),  # diagnosticValueAccess
        "fixed_length": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # fixedLength
        "processing_style": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DiagnosticProcessingStyleEnum,
        ),  # processingStyle
    }

    def __init__(self) -> None:
        """Initialize DiagnosticValueNeeds."""
        super().__init__()
        self.data_length: Optional[PositiveInteger] = None
        self.diagnostic_value_access: Optional[DiagnosticValueAccessEnum] = None
        self.fixed_length: Optional[Boolean] = None
        self.processing_style: Optional[DiagnosticProcessingStyleEnum] = None


class DiagnosticValueNeedsBuilder:
    """Builder for DiagnosticValueNeeds."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticValueNeeds = DiagnosticValueNeeds()

    def build(self) -> DiagnosticValueNeeds:
        """Build and return DiagnosticValueNeeds object.

        Returns:
            DiagnosticValueNeeds instance
        """
        # TODO: Add validation
        return self._obj
