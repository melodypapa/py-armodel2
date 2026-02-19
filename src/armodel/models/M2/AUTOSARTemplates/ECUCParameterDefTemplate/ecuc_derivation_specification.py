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

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    calculation: Optional[Any]
    ecuc_queries: list[EcucQuery]
    informal_formula: Optional[MlFormula]
    def __init__(self) -> None:
        """Initialize EcucDerivationSpecification."""
        super().__init__()
        self.calculation: Optional[Any] = None
        self.ecuc_queries: list[EcucQuery] = []
        self.informal_formula: Optional[MlFormula] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucDerivationSpecification":
        """Deserialize XML element to EcucDerivationSpecification object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EcucDerivationSpecification object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse calculation
        child = ARObject._find_child_element(element, "CALCULATION")
        if child is not None:
            calculation_value = child.text
            obj.calculation = calculation_value

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
