"""DiagnosticReadDataByIdentifierClass AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 113)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_DataByIdentifier.classes.json"""

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


class DiagnosticReadDataByIdentifierClass(DiagnosticServiceClass):
    """AUTOSAR DiagnosticReadDataByIdentifierClass."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "max_did_to_read": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # maxDidToRead
    }

    def __init__(self) -> None:
        """Initialize DiagnosticReadDataByIdentifierClass."""
        super().__init__()
        self.max_did_to_read: Optional[PositiveInteger] = None


class DiagnosticReadDataByIdentifierClassBuilder:
    """Builder for DiagnosticReadDataByIdentifierClass."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticReadDataByIdentifierClass = DiagnosticReadDataByIdentifierClass()

    def build(self) -> DiagnosticReadDataByIdentifierClass:
        """Build and return DiagnosticReadDataByIdentifierClass object.

        Returns:
            DiagnosticReadDataByIdentifierClass instance
        """
        # TODO: Add validation
        return self._obj
