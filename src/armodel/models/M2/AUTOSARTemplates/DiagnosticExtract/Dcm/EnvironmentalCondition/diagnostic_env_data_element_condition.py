"""DiagnosticEnvDataElementCondition AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 85)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_EnvironmentalCondition.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.EnvironmentalCondition.diagnostic_env_compare_condition import (
    DiagnosticEnvCompareCondition,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.data_prototype import (
    DataPrototype,
)

if TYPE_CHECKING:
    from armodel.models.M2.MSR.DataDictionary.DataDefProperties.sw_data_def_props import (
        SwDataDefProps,
    )
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.value_specification import (
        ValueSpecification,
    )



class DiagnosticEnvDataElementCondition(DiagnosticEnvCompareCondition):
    """AUTOSAR DiagnosticEnvDataElementCondition."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    compare_value: Optional[ValueSpecification]
    data_prototype: Optional[DataPrototype]
    sw_data_def: Optional[SwDataDefProps]
    def __init__(self) -> None:
        """Initialize DiagnosticEnvDataElementCondition."""
        super().__init__()
        self.compare_value: Optional[ValueSpecification] = None
        self.data_prototype: Optional[DataPrototype] = None
        self.sw_data_def: Optional[SwDataDefProps] = None


class DiagnosticEnvDataElementConditionBuilder:
    """Builder for DiagnosticEnvDataElementCondition."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticEnvDataElementCondition = DiagnosticEnvDataElementCondition()

    def build(self) -> DiagnosticEnvDataElementCondition:
        """Build and return DiagnosticEnvDataElementCondition object.

        Returns:
            DiagnosticEnvDataElementCondition instance
        """
        # TODO: Add validation
        return self._obj
