"""DiagnosticFreezeFrame AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 192)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticFreezeFrame.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticFreezeFrame import (
    DiagnosticRecordTriggerEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
    String,
)


class DiagnosticFreezeFrame(DiagnosticCommonElement):
    """AUTOSAR DiagnosticFreezeFrame."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    custom_trigger: Optional[String]
    record_number: Optional[PositiveInteger]
    trigger: Optional[DiagnosticRecordTriggerEnum]
    update: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize DiagnosticFreezeFrame."""
        super().__init__()
        self.custom_trigger: Optional[String] = None
        self.record_number: Optional[PositiveInteger] = None
        self.trigger: Optional[DiagnosticRecordTriggerEnum] = None
        self.update: Optional[Boolean] = None


class DiagnosticFreezeFrameBuilder:
    """Builder for DiagnosticFreezeFrame."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticFreezeFrame = DiagnosticFreezeFrame()

    def build(self) -> DiagnosticFreezeFrame:
        """Build and return DiagnosticFreezeFrame object.

        Returns:
            DiagnosticFreezeFrame instance
        """
        # TODO: Add validation
        return self._obj
