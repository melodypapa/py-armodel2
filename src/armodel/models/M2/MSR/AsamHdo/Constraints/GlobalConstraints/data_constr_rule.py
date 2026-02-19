"""DataConstrRule AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 405)
  - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (page 45)

JSON Source: docs/json/packages/M2_MSR_AsamHdo_Constraints_GlobalConstraints.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)
from armodel.models.M2.MSR.AsamHdo.Constraints.GlobalConstraints.internal_constrs import (
    InternalConstrs,
)
from armodel.models.M2.MSR.AsamHdo.Constraints.GlobalConstraints.phys_constrs import (
    PhysConstrs,
)


class DataConstrRule(ARObject):
    """AUTOSAR DataConstrRule."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    constr_level: Optional[Integer]
    internal_constrs: Optional[InternalConstrs]
    phys_constrs: Optional[PhysConstrs]
    def __init__(self) -> None:
        """Initialize DataConstrRule."""
        super().__init__()
        self.constr_level: Optional[Integer] = None
        self.internal_constrs: Optional[InternalConstrs] = None
        self.phys_constrs: Optional[PhysConstrs] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DataConstrRule":
        """Deserialize XML element to DataConstrRule object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DataConstrRule object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse constr_level
        child = ARObject._find_child_element(element, "CONSTR-LEVEL")
        if child is not None:
            constr_level_value = child.text
            obj.constr_level = constr_level_value

        # Parse internal_constrs
        child = ARObject._find_child_element(element, "INTERNAL-CONSTRS")
        if child is not None:
            internal_constrs_value = ARObject._deserialize_by_tag(child, "InternalConstrs")
            obj.internal_constrs = internal_constrs_value

        # Parse phys_constrs
        child = ARObject._find_child_element(element, "PHYS-CONSTRS")
        if child is not None:
            phys_constrs_value = ARObject._deserialize_by_tag(child, "PhysConstrs")
            obj.phys_constrs = phys_constrs_value

        return obj



class DataConstrRuleBuilder:
    """Builder for DataConstrRule."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DataConstrRule = DataConstrRule()

    def build(self) -> DataConstrRule:
        """Build and return DataConstrRule object.

        Returns:
            DataConstrRule instance
        """
        # TODO: Add validation
        return self._obj
