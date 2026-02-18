"""DiagnosticEnvDataCondition AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 84)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_EnvironmentalCondition.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.EnvironmentalCondition.diagnostic_env_compare_condition import (
    DiagnosticEnvCompareCondition,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_data_element import (
    DiagnosticDataElement,
)

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.value_specification import (
        ValueSpecification,
    )



class DiagnosticEnvDataCondition(DiagnosticEnvCompareCondition):
    """AUTOSAR DiagnosticEnvDataCondition."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    compare_value: Optional[ValueSpecification]
    data_element: Optional[DiagnosticDataElement]
    def __init__(self) -> None:
        """Initialize DiagnosticEnvDataCondition."""
        super().__init__()
        self.compare_value: Optional[ValueSpecification] = None
        self.data_element: Optional[DiagnosticDataElement] = None


class DiagnosticEnvDataConditionBuilder:
    """Builder for DiagnosticEnvDataCondition."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticEnvDataCondition = DiagnosticEnvDataCondition()

    def build(self) -> DiagnosticEnvDataCondition:
        """Build and return DiagnosticEnvDataCondition object.

        Returns:
            DiagnosticEnvDataCondition instance
        """
        # TODO: Add validation
        return self._obj
