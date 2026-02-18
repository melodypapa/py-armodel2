"""EcucConditionSpecification AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 100)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCParameterDefTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_condition_formula import (
    EcucConditionFormula,
)
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_query import (
    EcucQuery,
)
from armodel.models.M2.MSR.Documentation.BlockElements.Formula.ml_formula import (
    MlFormula,
)


class EcucConditionSpecification(ARObject):
    """AUTOSAR EcucConditionSpecification."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    condition: Optional[EcucConditionFormula]
    ecuc_queries: list[EcucQuery]
    informal_formula: Optional[MlFormula]
    def __init__(self) -> None:
        """Initialize EcucConditionSpecification."""
        super().__init__()
        self.condition: Optional[EcucConditionFormula] = None
        self.ecuc_queries: list[EcucQuery] = []
        self.informal_formula: Optional[MlFormula] = None


class EcucConditionSpecificationBuilder:
    """Builder for EcucConditionSpecification."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucConditionSpecification = EcucConditionSpecification()

    def build(self) -> EcucConditionSpecification:
        """Build and return EcucConditionSpecification object.

        Returns:
            EcucConditionSpecification instance
        """
        # TODO: Add validation
        return self._obj
