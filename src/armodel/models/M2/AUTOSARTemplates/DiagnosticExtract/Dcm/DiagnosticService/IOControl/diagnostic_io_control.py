"""DiagnosticIOControl AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 118)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_IOControl.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
    DiagnosticServiceInstance,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_data_identifier import (
    DiagnosticDataIdentifier,
)


class DiagnosticIOControl(DiagnosticServiceInstance):
    """AUTOSAR DiagnosticIOControl."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "control_enables": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=any (DiagnosticControl),
        ),  # controlEnables
        "data_identifier_identifier": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DiagnosticDataIdentifier,
        ),  # dataIdentifierIdentifier
        "freeze_current": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # freezeCurrent
        "io_control_class": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DiagnosticIOControl,
        ),  # ioControlClass
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
        """Initialize DiagnosticIOControl."""
        super().__init__()
        self.control_enables: list[Any] = []
        self.data_identifier_identifier: Optional[DiagnosticDataIdentifier] = None
        self.freeze_current: Optional[Boolean] = None
        self.io_control_class: Optional[DiagnosticIOControl] = None
        self.reset_to_default: Optional[Boolean] = None
        self.short_term: Optional[Boolean] = None


class DiagnosticIOControlBuilder:
    """Builder for DiagnosticIOControl."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticIOControl = DiagnosticIOControl()

    def build(self) -> DiagnosticIOControl:
        """Build and return DiagnosticIOControl object.

        Returns:
            DiagnosticIOControl instance
        """
        # TODO: Add validation
        return self._obj
