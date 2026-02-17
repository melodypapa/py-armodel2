"""DiagnosticSessionControlClass AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 93)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_SessionControl.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_class import (
    DiagnosticServiceClass,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)


class DiagnosticSessionControlClass(DiagnosticServiceClass):
    """AUTOSAR DiagnosticSessionControlClass."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "s3_server": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # s3Server
    }

    def __init__(self) -> None:
        """Initialize DiagnosticSessionControlClass."""
        super().__init__()
        self.s3_server: Optional[TimeValue] = None


class DiagnosticSessionControlClassBuilder:
    """Builder for DiagnosticSessionControlClass."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticSessionControlClass = DiagnosticSessionControlClass()

    def build(self) -> DiagnosticSessionControlClass:
        """Build and return DiagnosticSessionControlClass object.

        Returns:
            DiagnosticSessionControlClass instance
        """
        # TODO: Add validation
        return self._obj
