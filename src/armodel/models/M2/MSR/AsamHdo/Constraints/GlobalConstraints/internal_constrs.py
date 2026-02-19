"""InternalConstrs AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 407)

JSON Source: docs/json/packages/M2_MSR_AsamHdo_Constraints_GlobalConstraints.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    MonotonyEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Limit,
    Numerical,
)
from armodel.models.M2.MSR.AsamHdo.Constraints.GlobalConstraints.scale_constr import (
    ScaleConstr,
)


class InternalConstrs(ARObject):
    """AUTOSAR InternalConstrs."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    lower_limit: Optional[Limit]
    max_diff: Optional[Numerical]
    max_gradient: Optional[Numerical]
    monotony: Optional[MonotonyEnum]
    scale_constrs: list[ScaleConstr]
    upper_limit: Optional[Limit]
    def __init__(self) -> None:
        """Initialize InternalConstrs."""
        super().__init__()
        self.lower_limit: Optional[Limit] = None
        self.max_diff: Optional[Numerical] = None
        self.max_gradient: Optional[Numerical] = None
        self.monotony: Optional[MonotonyEnum] = None
        self.scale_constrs: list[ScaleConstr] = []
        self.upper_limit: Optional[Limit] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "InternalConstrs":
        """Deserialize XML element to InternalConstrs object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized InternalConstrs object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse lower_limit
        child = ARObject._find_child_element(element, "LOWER-LIMIT")
        if child is not None:
            lower_limit_value = child.text
            obj.lower_limit = lower_limit_value

        # Parse max_diff
        child = ARObject._find_child_element(element, "MAX-DIFF")
        if child is not None:
            max_diff_value = child.text
            obj.max_diff = max_diff_value

        # Parse max_gradient
        child = ARObject._find_child_element(element, "MAX-GRADIENT")
        if child is not None:
            max_gradient_value = child.text
            obj.max_gradient = max_gradient_value

        # Parse monotony
        child = ARObject._find_child_element(element, "MONOTONY")
        if child is not None:
            monotony_value = child.text
            obj.monotony = monotony_value

        # Parse scale_constrs (list)
        obj.scale_constrs = []
        for child in ARObject._find_all_child_elements(element, "SCALE-CONSTRS"):
            scale_constrs_value = ARObject._deserialize_by_tag(child, "ScaleConstr")
            obj.scale_constrs.append(scale_constrs_value)

        # Parse upper_limit
        child = ARObject._find_child_element(element, "UPPER-LIMIT")
        if child is not None:
            upper_limit_value = child.text
            obj.upper_limit = upper_limit_value

        return obj



class InternalConstrsBuilder:
    """Builder for InternalConstrs."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: InternalConstrs = InternalConstrs()

    def build(self) -> InternalConstrs:
        """Build and return InternalConstrs object.

        Returns:
            InternalConstrs instance
        """
        # TODO: Add validation
        return self._obj
