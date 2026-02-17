"""DiagnosticControlEnableMaskBit AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 119)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_IOControl.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_data_element import (
    DiagnosticDataElement,
)


class DiagnosticControlEnableMaskBit(ARObject):
    """AUTOSAR DiagnosticControlEnableMaskBit."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "bit_number": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # bitNumber
        "controlled_datas": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=DiagnosticDataElement,
        ),  # controlledDatas
    }

    def __init__(self) -> None:
        """Initialize DiagnosticControlEnableMaskBit."""
        super().__init__()
        self.bit_number: Optional[PositiveInteger] = None
        self.controlled_datas: list[DiagnosticDataElement] = []


class DiagnosticControlEnableMaskBitBuilder:
    """Builder for DiagnosticControlEnableMaskBit."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticControlEnableMaskBit = DiagnosticControlEnableMaskBit()

    def build(self) -> DiagnosticControlEnableMaskBit:
        """Build and return DiagnosticControlEnableMaskBit object.

        Returns:
            DiagnosticControlEnableMaskBit instance
        """
        # TODO: Add validation
        return self._obj
