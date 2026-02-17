"""CompuMethod AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 310)
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 308)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 380)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2010)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 436)
  - AUTOSAR_FO_TPS_LogAndTraceExtract.pdf (page 30)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 176)

JSON Source: docs/json/packages/M2_MSR_AsamHdo_ComputationMethod.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    DisplayFormatString,
)
from armodel.models.M2.MSR.AsamHdo.ComputationMethod.compu import (
    Compu,
)
from armodel.models.M2.MSR.AsamHdo.Units.unit import (
    Unit,
)


class CompuMethod(ARElement):
    """AUTOSAR CompuMethod."""

    compu_internal_to_phys: Optional[Compu]
    compu_phys_to_internal: Optional[Compu]
    display_format: Optional[DisplayFormatString]
    unit: Optional[Unit]
    def __init__(self) -> None:
        """Initialize CompuMethod."""
        super().__init__()
        self.compu_internal_to_phys: Optional[Compu] = None
        self.compu_phys_to_internal: Optional[Compu] = None
        self.display_format: Optional[DisplayFormatString] = None
        self.unit: Optional[Unit] = None


class CompuMethodBuilder:
    """Builder for CompuMethod."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CompuMethod = CompuMethod()

    def build(self) -> CompuMethod:
        """Build and return CompuMethod object.

        Returns:
            CompuMethod instance
        """
        # TODO: Add validation
        return self._obj
