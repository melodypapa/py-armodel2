"""DiagnosticExtendedDataRecord AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 190)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticExtendedDataRecord.classes.json"""

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
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_parameter import (
    DiagnosticParameter,
)


class DiagnosticExtendedDataRecord(DiagnosticCommonElement):
    """AUTOSAR DiagnosticExtendedDataRecord."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    custom_trigger: Optional[String]
    record_elements: list[DiagnosticParameter]
    record_number: Optional[PositiveInteger]
    trigger: Optional[DiagnosticRecordTriggerEnum]
    update: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize DiagnosticExtendedDataRecord."""
        super().__init__()
        self.custom_trigger: Optional[String] = None
        self.record_elements: list[DiagnosticParameter] = []
        self.record_number: Optional[PositiveInteger] = None
        self.trigger: Optional[DiagnosticRecordTriggerEnum] = None
        self.update: Optional[Boolean] = None


class DiagnosticExtendedDataRecordBuilder:
    """Builder for DiagnosticExtendedDataRecord."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticExtendedDataRecord = DiagnosticExtendedDataRecord()

    def build(self) -> DiagnosticExtendedDataRecord:
        """Build and return DiagnosticExtendedDataRecord object.

        Returns:
            DiagnosticExtendedDataRecord instance
        """
        # TODO: Add validation
        return self._obj
