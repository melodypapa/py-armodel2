"""DiagnosticCustomServiceClass AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 71)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_CommonService.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_class import (
    DiagnosticServiceClass,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class DiagnosticCustomServiceClass(DiagnosticServiceClass):
    """AUTOSAR DiagnosticCustomServiceClass."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "custom_service": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # customService
    }

    def __init__(self) -> None:
        """Initialize DiagnosticCustomServiceClass."""
        super().__init__()
        self.custom_service: Optional[PositiveInteger] = None


class DiagnosticCustomServiceClassBuilder:
    """Builder for DiagnosticCustomServiceClass."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticCustomServiceClass = DiagnosticCustomServiceClass()

    def build(self) -> DiagnosticCustomServiceClass:
        """Build and return DiagnosticCustomServiceClass object.

        Returns:
            DiagnosticCustomServiceClass instance
        """
        # TODO: Add validation
        return self._obj
