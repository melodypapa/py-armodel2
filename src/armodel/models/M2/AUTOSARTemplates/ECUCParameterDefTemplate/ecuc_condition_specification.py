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
    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucConditionSpecification":
        """Deserialize XML element to EcucConditionSpecification object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EcucConditionSpecification object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse condition
        child = ARObject._find_child_element(element, "CONDITION")
        if child is not None:
            condition_value = ARObject._deserialize_by_tag(child, "EcucConditionFormula")
            obj.condition = condition_value

        # Parse ecuc_queries (list)
        obj.ecuc_queries = []
        for child in ARObject._find_all_child_elements(element, "ECUC-QUERIES"):
            ecuc_queries_value = ARObject._deserialize_by_tag(child, "EcucQuery")
            obj.ecuc_queries.append(ecuc_queries_value)

        # Parse informal_formula
        child = ARObject._find_child_element(element, "INFORMAL-FORMULA")
        if child is not None:
            informal_formula_value = ARObject._deserialize_by_tag(child, "MlFormula")
            obj.informal_formula = informal_formula_value

        return obj



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
