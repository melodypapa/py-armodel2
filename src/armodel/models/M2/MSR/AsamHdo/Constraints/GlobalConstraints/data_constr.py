"""DataConstr AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 310)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 405)
  - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (page 44)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 179)

JSON Source: docs/json/packages/M2_MSR_AsamHdo_Constraints_GlobalConstraints.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.MSR.AsamHdo.Constraints.GlobalConstraints.data_constr_rule import (
    DataConstrRule,
)


class DataConstr(ARElement):
    """AUTOSAR DataConstr."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    data_constr_rules: list[DataConstrRule]
    def __init__(self) -> None:
        """Initialize DataConstr."""
        super().__init__()
        self.data_constr_rules: list[DataConstrRule] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DataConstr":
        """Deserialize XML element to DataConstr object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DataConstr object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse data_constr_rules (list)
        obj.data_constr_rules = []
        for child in ARObject._find_all_child_elements(element, "DATA-CONSTR-RULES"):
            data_constr_rules_value = ARObject._deserialize_by_tag(child, "DataConstrRule")
            obj.data_constr_rules.append(data_constr_rules_value)

        return obj



class DataConstrBuilder:
    """Builder for DataConstr."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DataConstr = DataConstr()

    def build(self) -> DataConstr:
        """Build and return DataConstr object.

        Returns:
            DataConstr instance
        """
        # TODO: Add validation
        return self._obj
