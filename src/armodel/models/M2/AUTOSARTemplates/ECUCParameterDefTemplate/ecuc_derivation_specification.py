"""EcucDerivationSpecification AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 87)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCParameterDefTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_query import (
    EcucQuery,
)
from armodel.models.M2.MSR.Documentation.BlockElements.Formula.ml_formula import (
    MlFormula,
)


class EcucDerivationSpecification(ARObject):
    """AUTOSAR EcucDerivationSpecification."""

    def __init__(self) -> None:
        """Initialize EcucDerivationSpecification."""
        super().__init__()
        self.calculation: Optional[Any] = None
        self.ecuc_queries: list[EcucQuery] = []
        self.informal_formula: Optional[MlFormula] = None


class EcucDerivationSpecificationBuilder:
    """Builder for EcucDerivationSpecification."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucDerivationSpecification = EcucDerivationSpecification()

    def build(self) -> EcucDerivationSpecification:
        """Build and return EcucDerivationSpecification object.

        Returns:
            EcucDerivationSpecification instance
        """
        # TODO: Add validation
        return self._obj
