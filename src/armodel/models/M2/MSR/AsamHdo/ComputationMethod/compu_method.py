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
from armodel.serialization.decorators import xml_element_tag


class CompuMethod(ARElement):
    """AUTOSAR CompuMethod."""

    compu_internal_to_phys: Optional[Compu]
    compu_phys_to_internal: Optional[Compu]
    display_format: Optional[DisplayFormatString]
    unit: Optional[Unit]

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize CompuMethod."""
        super().__init__()
        self._compu_internal_to_phys: Optional[Compu] = None
        self._compu_phys_to_internal: Optional[Compu] = None
        self.display_format: Optional[DisplayFormatString] = None
        self.unit: Optional[Unit] = None

    @property
    @xml_element_tag("COMPU-INTERNAL-TO-PHYS", Compu)
    def compu_internal_to_phys(self) -> Optional[Compu]:
        """Get compu_internal_to_phys value."""
        return self._compu_internal_to_phys

    @compu_internal_to_phys.setter
    def compu_internal_to_phys(self, value: Optional[Compu]) -> None:
        """Set compu_internal_to_phys value."""
        self._compu_internal_to_phys = value

    @property
    @xml_element_tag("COMPU-PHYS-TO-INTERNAL", Compu)
    def compu_phys_to_internal(self) -> Optional[Compu]:
        """Get compu_phys_to_internal value."""
        return self._compu_phys_to_internal

    @compu_phys_to_internal.setter
    def compu_phys_to_internal(self, value: Optional[Compu]) -> None:
        """Set compu_phys_to_internal value."""
        self._compu_phys_to_internal = value


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
