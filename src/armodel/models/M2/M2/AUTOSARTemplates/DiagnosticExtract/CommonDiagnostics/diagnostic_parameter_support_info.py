"""DiagnosticParameterSupportInfo AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 149)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_CommonDiagnostics.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class DiagnosticParameterSupportInfo(ARObject):
    """AUTOSAR DiagnosticParameterSupportInfo."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "support_info_bit": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # supportInfoBit
    }

    def __init__(self) -> None:
        """Initialize DiagnosticParameterSupportInfo."""
        super().__init__()
        self.support_info_bit: Optional[PositiveInteger] = None


class DiagnosticParameterSupportInfoBuilder:
    """Builder for DiagnosticParameterSupportInfo."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticParameterSupportInfo = DiagnosticParameterSupportInfo()

    def build(self) -> DiagnosticParameterSupportInfo:
        """Build and return DiagnosticParameterSupportInfo object.

        Returns:
            DiagnosticParameterSupportInfo instance
        """
        # TODO: Add validation
        return self._obj
