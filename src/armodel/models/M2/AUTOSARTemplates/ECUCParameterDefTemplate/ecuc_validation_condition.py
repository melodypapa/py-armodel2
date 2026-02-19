"""EcucValidationCondition AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 103)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCParameterDefTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_condition_formula import (
        EcucConditionFormula,
    )
    from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_query import (
        EcucQuery,
    )



class EcucValidationCondition(Identifiable):
    """AUTOSAR EcucValidationCondition."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    ecuc_queries: list[EcucQuery]
    validation: Optional[EcucConditionFormula]
    def __init__(self) -> None:
        """Initialize EcucValidationCondition."""
        super().__init__()
        self.ecuc_queries: list[EcucQuery] = []
        self.validation: Optional[EcucConditionFormula] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucValidationCondition":
        """Deserialize XML element to EcucValidationCondition object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EcucValidationCondition object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse ecuc_queries (list)
        obj.ecuc_queries = []
        for child in ARObject._find_all_child_elements(element, "ECUC-QUERIES"):
            ecuc_queries_value = ARObject._deserialize_by_tag(child, "EcucQuery")
            obj.ecuc_queries.append(ecuc_queries_value)

        # Parse validation
        child = ARObject._find_child_element(element, "VALIDATION")
        if child is not None:
            validation_value = ARObject._deserialize_by_tag(child, "EcucConditionFormula")
            obj.validation = validation_value

        return obj



class EcucValidationConditionBuilder:
    """Builder for EcucValidationCondition."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucValidationCondition = EcucValidationCondition()

    def build(self) -> EcucValidationCondition:
        """Build and return EcucValidationCondition object.

        Returns:
            EcucValidationCondition instance
        """
        # TODO: Add validation
        return self._obj
