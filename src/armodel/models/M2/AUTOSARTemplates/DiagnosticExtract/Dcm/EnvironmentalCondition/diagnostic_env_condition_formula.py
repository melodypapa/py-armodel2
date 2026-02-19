"""DiagnosticEnvConditionFormula AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 80)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_EnvironmentalCondition.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.EnvironmentalCondition.diagnostic_env_condition_formula_part import (
    DiagnosticEnvConditionFormulaPart,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.EnvironmentalCondition import (
    DiagnosticLogicalOperatorEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class DiagnosticEnvConditionFormula(DiagnosticEnvConditionFormulaPart):
    """AUTOSAR DiagnosticEnvConditionFormula."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    nrc_value: Optional[PositiveInteger]
    op: Optional[DiagnosticLogicalOperatorEnum]
    def __init__(self) -> None:
        """Initialize DiagnosticEnvConditionFormula."""
        super().__init__()
        self.nrc_value: Optional[PositiveInteger] = None
        self.op: Optional[DiagnosticLogicalOperatorEnum] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticEnvConditionFormula":
        """Deserialize XML element to DiagnosticEnvConditionFormula object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticEnvConditionFormula object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticEnvConditionFormula, cls).deserialize(element)

        # Parse nrc_value
        child = ARObject._find_child_element(element, "NRC-VALUE")
        if child is not None:
            nrc_value_value = child.text
            obj.nrc_value = nrc_value_value

        # Parse op
        child = ARObject._find_child_element(element, "OP")
        if child is not None:
            op_value = DiagnosticLogicalOperatorEnum.deserialize(child)
            obj.op = op_value

        return obj



class DiagnosticEnvConditionFormulaBuilder:
    """Builder for DiagnosticEnvConditionFormula."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticEnvConditionFormula = DiagnosticEnvConditionFormula()

    def build(self) -> DiagnosticEnvConditionFormula:
        """Build and return DiagnosticEnvConditionFormula object.

        Returns:
            DiagnosticEnvConditionFormula instance
        """
        # TODO: Add validation
        return self._obj
